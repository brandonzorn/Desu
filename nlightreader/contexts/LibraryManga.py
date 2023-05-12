from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu, QApplication

from nlightreader.utils import translate


class LibraryMangaMenu(QMenu):
    def __init__(self):
        super().__init__()
        self.add_to_lib = QAction(translate("Menu", "Add to Library"))
        self.remove_from_lib = QAction(translate("Menu", "Remove from library"))
        self.open_in_browser = QAction(translate("Menu", "Open in browser"))
        self.remove_files = QAction(translate("Menu", "Clear local files"))
        self.open_local_files = QAction(translate("Menu", "Open local files"))

    def set_mode(self, mode: int):
        self.addAction(self.open_in_browser)
        match mode:
            case 0:
                self.addAction(self.add_to_lib)
            case 1:
                self.addAction(self.remove_from_lib)
        if "beta_features" in QApplication.arguments():
            self.addAction(self.open_local_files)
            self.addAction(self.remove_files)
