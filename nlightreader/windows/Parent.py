from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from data.ui.mainWindow import Ui_MainWindow
from nlightreader.items import Manga
from nlightreader.widgets import FormFacial, FormLibrary, FormShikimori, FormHistory, FormInfo


class ParentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Form_facial = FormFacial()
        self.Form_library = FormLibrary()
        self.Form_shikimori = FormShikimori()
        self.Form_history = FormHistory()

        self.ui.btn_main.clicked.connect(lambda: self.change_widget(self.Form_facial))
        self.ui.btn_library.clicked.connect(lambda: self.change_widget(self.Form_library))
        self.ui.btn_shikimori.clicked.connect(lambda: self.change_widget(self.Form_shikimori))
        self.ui.btn_history.clicked.connect(lambda: self.change_widget(self.Form_history))

        self.Form_facial.manga_open.connect(self.open_info)
        self.Form_library.manga_open.connect(self.open_info)
        self.Form_shikimori.manga_open.connect(self.open_info)
        self.Form_history.manga_open.connect(self.open_info)

        self.ui.top_item.currentChanged.connect(self.widgets_checker)

        self.change_widget(self.Form_facial)

    def change_widget(self, widget):
        if self.ui.top_item.currentWidget() == widget:
            return
        widget.setup()
        if self.ui.top_item.currentWidget():
            self.ui.top_item.removeWidget(self.ui.top_item.currentWidget())
        self.ui.top_item.addWidget(widget)
        self.ui.top_item.setCurrentWidget(widget)

    @Slot(Manga)
    def open_info(self, manga: Manga):
        def set_info_widget():
            self.ui.top_item.addWidget(info)
            self.ui.top_item.setCurrentWidget(info)
        info = FormInfo()
        info.opened_related_manga.connect(self.open_info)
        info.setup_done.connect(set_info_widget)
        info.setup(manga)

    @Slot()
    def widgets_checker(self):
        count = self.ui.top_item.count()
        if count == 1 and self.ui.side_menu_widget.isHidden():
            self.ui.top_item.currentWidget().update_content()
            self.ui.side_menu_widget.show()
        elif count > 1 and self.ui.side_menu_widget.isVisible():
            self.ui.side_menu_widget.hide()
