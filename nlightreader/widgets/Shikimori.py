import webbrowser

from PySide6.QtWidgets import QListWidgetItem

from const.lists import LibList
from data.ui.shikimori import Ui_Form
from nlightreader.contexts.LibraryManga import LibraryMangaMenu
from nlightreader.dialogs import FormAuth
from nlightreader.items import Manga, RequestForm, User
from nlightreader.parsers import ShikimoriLib
from nlightreader.utils import Database, lock_ui, get_catalog, translate, Worker
from nlightreader.widgets.BaseWidget import BaseWidget


class FormShikimori(BaseWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mangas: list[Manga] = []
        self.catalog = ShikimoriLib()
        self.Form_auth = FormAuth(self.catalog)
        self.request_params = RequestForm()
        self.db: Database = Database()
        self.ui.planned_btn.clicked.connect(lambda: self.change_list(LibList.planned))
        self.ui.reading_btn.clicked.connect(lambda: self.change_list(LibList.watching))
        self.ui.on_hold_btn.clicked.connect(lambda: self.change_list(LibList.on_hold))
        self.ui.completed_btn.clicked.connect(lambda: self.change_list(LibList.completed))
        self.ui.dropped_btn.clicked.connect(lambda: self.change_list(LibList.dropped))
        self.ui.re_reading_btn.clicked.connect(lambda: self.change_list(LibList.rewatching))
        self.ui.prev_btn.clicked.connect(lambda: self.change_page('-'))
        self.ui.next_btn.clicked.connect(lambda: self.change_page('+'))
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.auth_btn.clicked.connect(self.authorize)
        self.Form_auth.accepted.connect(self.auth_accept)
        self.ui.items_list.customContextMenuRequested.connect(self.on_context_menu)
        self.get_content()

    def on_context_menu(self, pos):
        def open_in_browser():
            webbrowser.open_new_tab(get_catalog(selected_manga.catalog_id)().get_manga_url(selected_manga))

        menu = LibraryMangaMenu()
        selected_item = self.ui.items_list.itemAt(pos)
        selected_manga = self.mangas[selected_item.listWidget().indexFromItem(selected_item).row()]
        menu.set_mode(2)
        menu.open_in_browser.triggered.connect(open_in_browser)
        menu.exec(self.ui.items_list.mapToGlobal(pos))

    def setup(self):
        whoami = self.get_whoami()
        if whoami.nickname:
            self.ui.auth_btn.setText(whoami.nickname)
        else:
            self.ui.auth_btn.setText(translate("Other", "Sign in"))

    def get_current_manga(self):
        return self.catalog.get_manga(self.mangas[self.ui.items_list.currentIndex().row()])

    def auth_accept(self):
        self.catalog.session.auth_login(self.Form_auth.get_user_data())
        whoami = self.get_whoami()
        if whoami.nickname:
            self.ui.auth_btn.setText(whoami.nickname)
        else:
            self.ui.auth_btn.setText(translate("Other", "Sign in"))

    def authorize(self):
        self.Form_auth.hide()
        self.Form_auth.show()

    def get_whoami(self) -> User:
        return self.catalog.get_user()

    def change_page(self, page):
        match page:
            case '+':
                self.request_params.page += 1
            case '-':
                if self.request_params.page == 1:
                    return
                self.request_params.page -= 1
        self.ui.page_label.setText(f"{translate('Other', 'Page')} {self.request_params.page}")
        Worker(self.get_content).start()

    def search(self):
        self.request_params.page = 1
        self.request_params.search = self.ui.title_line.text()
        self.get_content()

    def change_list(self, lib_list: LibList):
        self.request_params.lib_list = lib_list
        self.get_content()

    def get_content(self):
        ui_to_lock = [self]
        with lock_ui(ui_to_lock):
            self.ui.items_list.clear()
            self.mangas = self.catalog.search_manga(self.request_params)
            self.ui.page_label.setText(f"{translate('Other', 'Page')} {self.request_params.page}")
            for manga in self.mangas:
                item = QListWidgetItem(manga.get_name())
                self.ui.items_list.addItem(item)
