import webbrowser

from PySide6 import QtGui
from PySide6.QtCore import Qt, Signal, QSize, QRect
from PySide6.QtGui import QImage, QPainter, QPixmap, QColor
from PySide6.QtWidgets import QWidget
from qfluentwidgets import InfoBar

from data.ui.manga_item import Ui_Form
from nlightreader.contexts import LibraryMangaMenu
from nlightreader.items import Manga
from nlightreader.utils import Worker, get_catalog, FileManager, Database, translate


class MangaItem(QWidget):
    manga_clicked = Signal(Manga)
    manga_changed = Signal()

    def __init__(self, manga: Manga, *, is_added_to_lib=True, pool=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.manga = manga
        self._catalog = get_catalog(self.manga.catalog_id)()
        self.manga_pixmap = None
        self._is_added_to_lib = is_added_to_lib
        self._db: Database = Database()
        self._pool = pool
        self.customContextMenuRequested.connect(self.on_context_menu)
        self.ui.name_lbl.setText(self.manga.get_name())

    def enterEvent(self, event):
        super().enterEvent(event)
        if self.isEnabled():
            self.set_image(0.3)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.set_image(1.0)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            if self.rect().contains(event.pos()):
                self.manga_clicked.emit(self.manga)

    def on_context_menu(self, pos):
        catalog = get_catalog(self.manga.catalog_id)()
        manga_title = self.manga.get_name()
        info_bar_parent = self.parentWidget().parentWidget()
        info_bar_duration = 2000

        def add_to_lib():
            self._db.add_manga(self.manga)
            self._db.add_manga_library(self.manga)
            InfoBar.success(
                title=manga_title,
                content=translate(
                    "Message", "Manga {} has been added.",
                ).format(self.manga.get_name()),
                duration=info_bar_duration,
                parent=info_bar_parent,
            )

        def remove_from_lib():
            self._db.rem_manga_library(self.manga)
            InfoBar.success(
                title=manga_title,
                content=translate(
                    "Message", "Manga {} has been deleted.",
                ).format(self.manga.get_name()),
                duration=info_bar_duration,
                parent=info_bar_parent,
            )
            self.manga_changed.emit()

        def open_in_browser():
            webbrowser.open_new_tab(catalog.get_manga_url(self.manga))

        def remove_files():
            FileManager.remove_manga_files(self.manga, catalog)
            InfoBar.success(
                title=manga_title,
                content=translate(
                    "Message", "Files {} have been removed.",
                ).format(self.manga.get_name()),
                duration=info_bar_duration,
                parent=info_bar_parent,
            )

        def open_local_files():
            FileManager.open_dir_in_explorer(self.manga, catalog)

        menu = LibraryMangaMenu()
        if self._is_added_to_lib and not self._catalog.is_primary:
            if self._db.check_manga_library(self.manga):
                menu.set_mode(1)
            else:
                menu.set_mode(0)
        else:
            menu.set_mode(2)
        menu.add_to_lib.triggered.connect(add_to_lib)
        menu.remove_from_lib.triggered.connect(remove_from_lib)
        menu.open_in_browser.triggered.connect(open_in_browser)
        menu.remove_files.triggered.connect(remove_files)
        menu.open_local_files.triggered.connect(open_local_files)
        menu.exec(self.mapToGlobal(pos))

    def set_size(self, size: int):
        current_size = self.size()
        max_size = QSize(size, int(size * 1.5))
        if current_size != max_size:
            self.setFixedWidth(max_size.width())
            self.ui.image_card.setFixedSize(max_size)
            self.ui.image.setMaximumSize(max_size)
        if self.manga_pixmap:
            self.set_image()

    def get_image(self):
        self.manga_pixmap = FileManager.get_manga_preview(self.manga, self._catalog)

    def set_image(self, opacity: float = 1.0):
        if not self.manga_pixmap:
            return

        image = QImage(self.ui.image.maximumSize(), QImage.Format_ARGB32)
        image.fill(QColor(0, 0, 0, 0))

        painter = QPainter(image)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QtGui.QPainterPath()
        path.addRoundedRect(QRect(0, 0, image.width(), image.height()), 10, 10)

        painter.setClipPath(path)
        painter.setOpacity(opacity if opacity else 1.0)
        painter.drawPixmap(0, 0, self.manga_pixmap.scaled(self.ui.image.maximumSize()))
        painter.end()

        self.ui.image.setPixmap(QPixmap.fromImage(image))

    def update_image(self):
        Worker(target=self.get_image, callback=self.set_image).start(self._pool)
