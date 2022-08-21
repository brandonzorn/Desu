import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from const.icons import app_icon_path
from desureader.utils.file_manager import init_app_paths
from desureader.windows.main_window import ParentWindow


class App(ParentWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(self.screen().size().width() // 2, self.screen().size().height() // 2))
        self.setWindowTitle('Desu')
        self.show()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    QApplication.setStyle('Fusion')
    app = QApplication(sys.argv)
    app_paths = ['Desu']
    init_app_paths(app_paths)
    a = App()
    QApplication.setWindowIcon(QIcon(app_icon_path))
    sys.exit(app.exec())
