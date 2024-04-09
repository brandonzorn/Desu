from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from data.ui.containers.text_area import Ui_Form
from nlightreader.widgets.NlightContainers.content_container import AbstractContentContainer


class TextArea(QWidget, AbstractContentContainer):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.size_slider.valueChanged.connect(self.__update_text_size)

    @Slot()
    def __update_text_size(self):
        font = self.ui.text_browser.font()
        font.setPointSize(self.ui.size_slider.value())
        self.ui.text_browser.setFont(font)

    def _reset_area(self):
        self.ui.text_browser.clear()

    def clear(self):
        self._reset_area()

    def set_content(self, content: str):
        self._reset_area()
        self.ui.text_browser.setHtml(content)

    def get_content_widget(self) -> QWidget:
        return self.ui.text_browser
