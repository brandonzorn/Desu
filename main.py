import sys
import locale
import darkdetect
from PySide6.QtCore import QSize, Qt, QTranslator
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from const.app import APP_NAME, APP_VERSION
from const.icons import app_icon_path
from nlightreader import ParentWindow
from nlightreader.utils import init_app_paths, get_locale_path


class App(ParentWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(self.screen().size().width() // 2, self.screen().size().height() // 2))
        self.setWindowTitle(APP_NAME)
        self.update_style()
        self.show()

    def update_style(self):
        dark = open("data/styles/dark/widget_dark.qss").read()
        light = open("data/styles/light/widget_light.qss").read()
        if darkdetect.isDark():
            self.setStyleSheet(dark)
        else:
            self.setStyleSheet(light)


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    QApplication.setStyle('Fusion')
    app = QApplication(sys.argv)
    trans = QTranslator()
    trans.load(get_locale_path(locale.getlocale()[0]))
    app.installTranslator(trans)
    app.setApplicationDisplayName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setWindowIcon(QIcon(app_icon_path))
    app_paths = [APP_NAME]
    init_app_paths(app_paths)
    a = App()
    sys.exit(app.exec())
