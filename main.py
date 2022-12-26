import sys
import darkdetect
from PySide6.QtCore import QSize, Qt, QTranslator, QLocale
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from const.app import APP_NAME, APP_VERSION
from const.icons import app_icon_path
from const.styles import dark_style, light_style
from nlightreader import ParentWindow
from nlightreader.utils import init_app_paths, get_locale_path


class App(ParentWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(self.screen().size().width() // 2, self.screen().size().height() // 2))
        self.setWindowTitle(APP_NAME)
        self.show()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    QApplication.setStyle('Fusion')
    app = QApplication(sys.argv)
    trans = QTranslator()
    trans.load(get_locale_path(QLocale().language()))
    dark = open(dark_style).read()
    light = open(light_style).read()
    themes = {"Dark": dark, "Light": light}
    app.installTranslator(trans)
    app.setApplicationDisplayName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setWindowIcon(QIcon(app_icon_path))
    app.setStyleSheet(themes[darkdetect.theme()])
    app_paths = [APP_NAME]
    init_app_paths(app_paths)
    a = App()
    sys.exit(app.exec())
