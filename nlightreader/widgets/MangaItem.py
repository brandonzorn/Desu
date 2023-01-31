import webbrowser

from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtWidgets import QWidget

from data.ui.manga_item import Ui_Form
from nlightreader.contexts import LibraryMangaMenu
from nlightreader.items import Manga
from nlightreader.utils import Worker, get_catalog, get_manga_preview


class Signals(QObject):
    manga_clicked = Signal(Manga)
    remove_from_lib = Signal(QWidget)


class MangaItem(QWidget):
    def __init__(self, manga: Manga):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setStyleSheet(
            "QFrame#frame, QLabel#name_lbl {"
            "border-radius: 10px;background-color: rgba(84.000, 86.000, 86.000, 0.737);}")
        self.manga = manga
        self.manga_pixmap = None
        self.signals = Signals()
        self.ui.frame.customContextMenuRequested.connect(self.on_context_menu)
        self.ui.name_lbl.setText(self.manga.get_name())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.signals.manga_clicked.emit(self.manga)
        event.accept()

    def on_context_menu(self, pos):
        def add_to_lib():
            self.db.add_manga(manga)
            self.db.add_manga_library(manga)

        def remove_from_lib():
            self.signals.remove_from_lib.emit(self)
            self.deleteLater()

        def open_in_browser():
            webbrowser.open_new_tab(get_catalog(self.manga.catalog_id)().get_manga_url(self.manga))

        menu = LibraryMangaMenu()
        menu.set_mode(1)
        menu.remove_from_lib.triggered.connect(remove_from_lib)
        menu.open_in_browser.triggered.connect(open_in_browser)
        menu.exec(self.ui.frame.mapToGlobal(pos))

    def set_size(self, size: int):
        self.setMaximumWidth(size)
        self.setFixedSize(self.maximumWidth(), self.maximumWidth() * 2)
        self.ui.image.setMaximumSize(self.maximumWidth(), self.maximumWidth() * 2)
        self.update_image()

    def update_image(self):
        def get_image():
            if not self.manga_pixmap:
                catalog = get_catalog(self.manga.catalog_id)()
                self.manga_pixmap = get_manga_preview(self.manga, catalog)

        def set_image():
            pixmap = self.manga_pixmap.scaled(self.ui.image.maximumSize(), Qt.AspectRatioMode.KeepAspectRatio,
                                              Qt.TransformationMode.SmoothTransformation)
            self.ui.image.setPixmap(pixmap)
        Worker(target=get_image, callback=set_image).start()
