from PySide6.QtWidgets import QListWidgetItem

from const.colors import ItemsColors
from data.ui.history import Ui_Form
from items import HistoryNote
from nlightreader.utils import Database
from nlightreader.widgets.BaseWidget import BaseWidget


class FormHistory(BaseWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db: Database = Database()
        self.ui.delete_btn.clicked.connect(self.delete_note)
        self.notes: list[HistoryNote] = []

    def setup(self):
        self.get_content()

    def get_current_manga(self):
        return self.notes[self.ui.items_list.currentIndex().row()].manga

    def delete_note(self):
        if self.ui.items_list.currentIndex().row() >= 0:
            self.db.del_history_note(self.notes[self.ui.items_list.currentIndex().row()].chapter)
            self.setup()

    def get_content(self):
        self.ui.items_list.clear()
        self.notes: list[HistoryNote] = self.db.get_history_notes()
        for note in self.notes:
            item = QListWidgetItem(note.get_name())
            if note.is_completed:
                item.setBackground(ItemsColors.READ)
            else:
                item.setBackground(ItemsColors.UNREAD)
            self.ui.items_list.addItem(item)
