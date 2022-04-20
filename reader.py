import os
from pathlib import Path
from threading import Thread
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from database import Database
from form.desu_readerUI import Ui_Dialog
from items import Image, Manga, Chapter
from parser.Desu import Desu


class Reader(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_re = Ui_Dialog()
        self.ui_re.setupUi(self)
        app_icon_path = os.path.join(Path(__file__).parent, "images/icon.png")
        self.setWindowIcon(QIcon(app_icon_path))
        self.ui_re.prev_page.clicked.connect(lambda: self.press_key('prev_page'))
        self.ui_re.next_page.clicked.connect(lambda: self.press_key('next_page'))
        self.ui_re.prev_chp.clicked.connect(lambda: self.press_key('prev_ch'))
        self.ui_re.next_chp.clicked.connect(lambda: self.press_key('next_ch'))
        self.wd = os.getcwd()
        self.db = Database()
        self.lay = QVBoxLayout(self.ui_re.scrollAreaWidgetContents)
        self.lay.addWidget(self.ui_re.img)
        self.manga: Manga = Manga({})
        self.chapters: [Chapter] = [Chapter({})]
        self.images: [Image] = [Image({})]
        self.cur_chapter: int = 1
        self.max_chapters: int = 1
        self.cur_page: int = 1
        self.max_page: int = 1

    def setup(self, manga, chapters, cur_chapter=1):
        self.cur_chapter = cur_chapter
        self.max_chapters = len(chapters)
        self.manga = manga
        self.chapters = chapters
        self.setWindowTitle(self.manga.name)
        self.showFullScreen()
        self.change_chapter()

    def close_reader(self):
        self.hide()

    def keyPressEvent(self, event):
        match event.key():
            case Qt.Key_Escape:
                self.close_reader()
            case Qt.Key_Left:
                self.press_key('prev_page')
            case Qt.Key_Right:
                self.press_key('next_page')
            case Qt.Key_Down:
                self.press_key('prev_ch')
            case Qt.Key_Up:
                self.press_key('next_ch')
        event.accept()

    def press_key(self, e):
        if self.isActiveWindow():
            match e:
                case 'next_page':
                    self.change_page('+')
                case 'prev_page':
                    self.change_page('-')
                case 'next_ch':
                    self.change_chapter('+')
                case 'prev_ch':
                    self.change_chapter('-')

    def change_page(self, page=None):
        match page:
            case '+':
                if self.cur_page == self.max_page:
                    self.press_key('next_ch')
                else:
                    self.cur_page += 1
            case '-':
                if self.cur_page == 1:
                    self.press_key('prev_ch')
                else:
                    self.cur_page -= 1
        self.attach_image()
        self.ui_re.lbl_page.setText(f'Страница {self.cur_page} / {self.max_page}')

    def change_chapter(self, page=None):
        match page:
            case '+':
                if self.cur_chapter == self.max_chapters:
                    self.close_reader()
                else:
                    self.cur_chapter += 1
            case '-':
                if self.cur_chapter == 1:
                    return
                else:
                    self.cur_chapter -= 1
        self.cur_page = 1
        self.get_images()
        self.change_page()
        self.ui_re.lbl_chp.setText(self.chapters[self.cur_chapter - 1].get_name())

    def attach_image(self):
        pixmap = self.get_pixmap(self.chapters[self.cur_chapter - 1], self.images[self.cur_page - 1])
        self.ui_re.img.setPixmap(pixmap)
        self.resize(self.screen().size())
        self.ui_re.scrollArea.verticalScrollBar().setValue(0)
        self.ui_re.scrollArea.horizontalScrollBar().setValue(0)
        self.showFullScreen()
        # self.ui_re.scrollArea.setWidgetResizable(True)

    def get_image(self, chapter, image) -> str:
        if not os.path.exists(f'{self.wd}/Desu/images/{self.manga.id}/{chapter.id}/{image.page}.jpg'):
            os.makedirs(f'{self.wd}/Desu/images/{self.manga.id}/{chapter.id}', exist_ok=True)
            img = Desu().get_image(image)
            if img:
                with open(f'{self.wd}/Desu/images/{self.manga.id}/{chapter.id}/{image.page}.jpg', 'wb') as f:
                    f.write(img.content)
        return f'{self.wd}/Desu/images/{self.manga.id}/{chapter.id}/{image.page}.jpg'

    def get_pixmap(self, chapter, image):
        pixmap = QPixmap(self.get_image(chapter, image))
        if pixmap.isNull():
            return QPixmap()
        if self.manga.kind in ['manga', 'manhua', 'one_shot']:
            pixmap = pixmap.scaled(self.ui_re.img.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return pixmap

    def get_images(self):
        chapter = self.chapters[self.cur_chapter - 1]
        self.images = Desu().get_images(self.manga, chapter)
        for i in self.images:
            self.db.add_image(i, chapter)
        self.images = self.db.get_images(chapter)
        if not self.images:
            self.images = [Image({'page': 1})]
        self.max_page = self.get_images_pages()
        Thread(target=lambda: self.download(self)).start()

    def get_images_pages(self) -> int:
        if not self.images:
            return 1
        return self.images[-1].page

    def download(self, form):
        images = self.images
        chapter = self.chapters[self.cur_chapter - 1]
        for image in images:
            if form.isHidden() or chapter.id != self.chapters[self.cur_chapter - 1].id:
                break
            self.get_image(chapter, image)
            if not os.path.exists(f'{self.wd}/Desu/images/{self.manga.id}/{chapter.id}/{image.page}.jpg'):
                img = Desu().get_image(images[image.page - 1])
                if img:
                    with open(f'{self.wd}/Desu/images/{self.manga.id}/{chapter.id}/{image.page}.jpg', 'wb') as f:
                        f.write(img.content)
