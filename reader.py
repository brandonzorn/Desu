import os
from pathlib import Path
from threading import Thread
from PySide2.QtCore import *
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import *
from const import URL_API
from database import db
from desu_readerUI import Ui_Dialog
from static import get_html


class Reader(QWidget):
    def __init__(self, manga, chapters, parent, cur_chapter=1):
        super().__init__()
        self.ui_re = Ui_Dialog()
        self.ui_re.setupUi(self)
        app_icon_path = os.path.join(Path(__file__).parent, "images/icon.png")
        self.setWindowIcon(QIcon(app_icon_path))
        self.ui_re.prev_page.clicked.connect(lambda: self.press_key('prev_page'))
        self.ui_re.next_page.clicked.connect(lambda: self.press_key('next_page'))
        self.ui_re.prev_chp.clicked.connect(lambda: self.press_key('prev_ch'))
        self.ui_re.next_chp.clicked.connect(lambda: self.press_key('next_ch'))
        self.cur_chapter: int = cur_chapter
        self.max_chapters: int = len(chapters)
        self.cur_page: int = 1
        self.max_page: int = 1
        self.manga = manga
        self.chapters = chapters
        self.images = []
        self.db = db
        self.wd = os.getcwd()
        self.setWindowTitle(self.manga.name)
        self.showFullScreen()
        self.change_chapter()

    def close_reader(self):
        self.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close_reader()
        if event.key() == Qt.Key_Left:
            self.press_key('prev_page')
        if event.key() == Qt.Key_Right:
            self.press_key('next_page')
        if event.key() == Qt.Key_Down:
            self.press_key('prev_ch')
        if event.key() == Qt.Key_Up:
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
        if page == '+':
            if self.cur_page == self.max_page and self.cur_chapter == self.max_chapters:
                return
            elif self.cur_page == self.max_page:
                self.press_key('next_ch')
            else:
                self.cur_page += 1
        elif page == '-':
            if self.cur_page > 1:
                self.cur_page -= 1
            elif self.cur_page == 1 and self.cur_chapter == 1:
                return
            else:
                self.press_key('prev_ch')
        pixmap = self.get_pixmap()
        self.ui_re.img.setPixmap(pixmap)
        self.ui_re.lbl_page.setText(f'Страница {self.cur_page} / {self.max_page}')

    def change_chapter(self, page=None):
        if page == '+':
            if self.cur_chapter != self.max_chapters:
                self.cur_chapter += 1
            else:
                return
        elif page == '-':
            if self.cur_chapter > 1:
                self.cur_chapter -= 1
            elif self.cur_chapter == 1:
                return
        self.cur_page = 1
        self.get_images()
        self.change_page()
        self.ui_re.lbl_chp.setText(self.chapters[self.cur_chapter - 1].get_name())

    def get_image(self, chapter, image) -> str:
        if not os.path.exists(f'{self.wd}/Desu/images/{self.manga.id}/{chapter.id}/{image.page}.jpg'):
            os.makedirs(f'{self.wd}/Desu/images/{self.manga.id}/{chapter.id}', exist_ok=True)
            img = get_html(image.img)
            with open(f'{self.wd}/Desu/images/{self.manga.id}/{chapter.id}/{image.page}.jpg', 'wb') as f:
                f.write(img.content)
        return f'{self.wd}/Desu/images/{self.manga.id}/{chapter.id}/{image.page}.jpg'

    def get_pixmap(self):
        size = self.screen().size()
        self.resize(size)
        self.showFullScreen()
        pixmap = QPixmap(self.get_image(self.chapters[self.cur_chapter - 1], self.images[self.cur_page - 1]))
        if pixmap.isNull():
            return QPixmap()
        pixmap = pixmap.scaled(size - QSize(20, 80), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return pixmap

    def get_images(self):
        chapter = self.chapters[self.cur_chapter - 1]
        current_url = f'{URL_API}/{self.manga.id}/chapter/{chapter.id}'
        html = get_html(current_url)
        self.images = []
        if html and html.status_code == 200:
            if len(html.json()) == 0:
                return
            images = html.json().get('response').get('pages').get('list')
            for i in images:
                self.db.add_images(i, chapter.id, images.index(i))
        self.images = self.db.get_images(chapter.id)
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
                img = get_html(images[image.page - 1].img)
                with open(f'{self.wd}/Desu/images/{self.manga.id}/{chapter.id}/{image.page}.jpg', 'wb') as f:
                    f.write(img.content)
