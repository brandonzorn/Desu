from PySide6.QtWidgets import QWidget, QListWidgetItem

from forms.library import Ui_Form
from items import Manga, RequestForm
from parser.LocalLib import LocalLib


class FormLibrary(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mangas: list[Manga] = []
        self.request_params = RequestForm()
        self.catalog = LocalLib()
        self.ui.planned_btn.clicked.connect(lambda: self.change_list('planned'))
        self.ui.reading_btn.clicked.connect(lambda: self.change_list('watching'))
        self.ui.on_hold_btn.clicked.connect(lambda: self.change_list('on_hold'))
        self.ui.completed_btn.clicked.connect(lambda: self.change_list('completed'))
        self.ui.dropped_btn.clicked.connect(lambda: self.change_list('dropped'))
        self.ui.re_reading_btn.clicked.connect(lambda: self.change_list('rewatching'))

    def get_current_manga(self) -> Manga:
        return self.mangas[self.ui.items_list.currentIndex().row()]

    def change_list(self, list_name: str):
        self.request_params.mylist = list_name
        self.update_list()

    def update_list(self):
        self.ui.items_list.clear()
        self.mangas = self.catalog.search_manga(self.request_params)
        for manga in self.mangas:
            item = QListWidgetItem(manga.get_name())
            self.ui.items_list.addItem(item)
