import logging

import requests
from PySide6.QtWidgets import QApplication
from requests_oauthlib import OAuth2Session

from nlightreader.consts.urls import URL_SHIKIMORI_API, SHIKIMORI_HEADERS, URL_SHIKIMORI, URL_SHIKIMORI_TOKEN
from nlightreader.consts.enums import Nl
from nlightreader.consts.items import ShikimoriItems
from nlightreader.items import Manga, RequestForm, Genre, Kind, User, UserRate, Character, Order
from nlightreader.parsers.catalog import AbstractCatalog, LibParser
from nlightreader.parsers.catalogs_base import AbstractMangaCatalog, AbstractRanobeCatalog
from nlightreader.utils.decorators import singleton
from nlightreader.utils.token import TokenManager
from nlightreader.utils.utils import get_html

try:
    from keys import SHIKIMORI_CLIENT_SECRET, SHIKIMORI_CLIENT_ID
except (ModuleNotFoundError, ImportError):
    logging.info("Shikimori API keys not found")
    SHIKIMORI_CLIENT_SECRET, SHIKIMORI_CLIENT_ID = "", ""


class ShikimoriBase(AbstractCatalog):
    CATALOG_ID = 1
    CATALOG_NAME = "Shikimori"

    def __init__(self):
        super().__init__()
        self.url = URL_SHIKIMORI
        self.url_api = URL_SHIKIMORI_API
        self.headers = SHIKIMORI_HEADERS
        self.is_primary = True

    def setup_manga(self, data: dict) -> Manga:
        return Manga(data.get("id"), self.CATALOG_ID, data.get("name"), data.get("russian"))

    def get_manga(self, manga: Manga) -> Manga:
        url = f"{self.url_api}/mangas/{manga.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            data = response
            manga.kind = Nl.MangaKind.from_str(data.get("kind"))
            manga.score = float(data.get("score"))
            manga.status = data.get("status")
            if data.get("volumes"):
                manga.volumes = int(data.get("volumes"))
            if data.get("chapters"):
                manga.chapters = int(data.get("chapters"))

            manga.add_description(Nl.Language.undefined, data.get("description"))
        return manga

    def get_character(self, character: Character) -> Character:
        url = f"{self.url_api}/characters/{character.content_id}"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            character.description = response.get("description")
        return character

    def get_preview(self, manga: Manga):
        return get_html(f"{self.url}/system/mangas/preview/{manga.content_id}.jpg", content_type="content")

    def get_character_preview(self, character: Character):
        return get_html(f"{self.url}/system/characters/preview/{character.content_id}.jpg").content

    def get_genres(self):
        url = f"{self.url_api}/genres"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            return [Genre(str(i.get("id")), self.CATALOG_ID, i.get("name"), i.get("russian")) for i in response]
        return []

    def get_orders(self) -> list[Order]:
        return [Order(i["value"], self.CATALOG_ID, i["name"], i["russian"]) for i in ShikimoriItems.ORDERS]

    def get_relations(self, manga: Manga) -> list[Manga]:
        mangas = []
        url = f"{self.url_api}/mangas/{manga.content_id}/related"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            for i in response:
                if i.get("manga"):
                    i = i.get("manga")
                    mangas.append(self.setup_manga(i))
        return mangas

    def get_characters(self, manga: Manga) -> list[Character]:
        characters = []
        url = f"{self.url_api}/mangas/{manga.content_id}/roles"
        response = get_html(url, headers=self.headers, content_type="json")
        if response:
            for i in response:
                if i.get("roles"):
                    role = i.get("roles")[0]
                    if role in ["Supporting", "Main"]:
                        data = i.get("character")
                        if data:
                            characters.append(Character(data.get("id"), self.CATALOG_ID, data.get("name"),
                                                        data.get("russian"), "", role))
            characters.sort(key=lambda x: x.role)
        return characters

    def get_manga_url(self, manga: Manga) -> str:
        return f"{self.url}/mangas/{manga.content_id}"


class ShikimoriManga(ShikimoriBase, AbstractMangaCatalog):
    CATALOG_NAME = "Shikimori(Manga)"

    def search_manga(self, form: RequestForm):
        url = f"{self.url_api}/mangas"
        params = {
            "limit": form.limit,
            "search": form.search,
            "page": form.page,
            "order": form.get_order_id(),
            "genre": ",".join(form.get_genre_ids()),
            "kind": ",".join(form.get_kind_ids()),
        }
        response = get_html(url, headers=self.headers, params=params, content_type="json")
        mangas = []
        if response:
            for i in response:
                mangas.append(self.setup_manga(i))
        return mangas

    def get_kinds(self):
        return [Kind(i["value"], self.CATALOG_ID, i["name"], i["russian"]) for i in ShikimoriItems.KINDS]


class ShikimoriRanobe(ShikimoriBase, AbstractRanobeCatalog):
    CATALOG_NAME = "Shikimori(Ranobe)"

    def search_manga(self, form: RequestForm):
        url = f"{self.url_api}/ranobe"
        params = {
            "limit": form.limit,
            "search": form.search,
            "page": form.page,
            "order": form.get_order_id(),
            "genre": ",".join(form.get_genre_ids()),
            "kind": ",".join(form.get_kind_ids()),
        }
        response = get_html(url, headers=self.headers, params=params, content_type="json")
        mangas = []
        if response:
            for i in response:
                mangas.append(self.setup_manga(i))
        return mangas


class ShikimoriLib(ShikimoriBase, LibParser):
    def __init__(self):
        super().__init__()
        self.fields = 1
        self.session: Auth = Auth()

    def search_manga(self, form: RequestForm):
        url = f"{self.url_api}/users/{self.session.user.id}/manga_rates"
        params = {"limit": 50, "page": form.page}
        response = self.session.request("GET", url, params=params)
        mangas = []
        lib_list = form.lib_list
        if lib_list == Nl.LibList.reading:
            lib_list = "watching"
        elif lib_list == Nl.LibList.re_reading:
            lib_list = "rewatching"
        else:
            lib_list = form.lib_list.name
        if response and (resp_json := response.json()):
            for i in resp_json:
                if not i.get("status") == lib_list:
                    continue
                i = i.get("manga")
                mangas.append(self.setup_manga(i))
        return mangas

    def get_user(self):
        response = self.session.request("GET", f"{self.url_api}/users/whoami")
        self.session.user = User(None, None, None)
        if response and (resp_json := response.json()):
            self.session.user = User(resp_json.get("id"), resp_json.get("nickname"), resp_json.get("avatar"))
        return self.session.user

    def create_user_rate(self, manga: Manga):
        url = f"{self.url_api}/v2/user_rates"
        data = {
            "user_rate": {
                "target_type": "Manga",
                "user_id": self.session.user.id,
                "target_id": manga.content_id,
            },
        }
        self.session.request("POST", url, json=data)

    def check_user_rate(self, manga: Manga):
        url = f"{self.url_api}/v2/user_rates"
        params = {
            "target_type": "Manga",
            "user_id": self.session.user.id,
            "target_id": manga.content_id,
        }
        response = self.session.request("GET", url, params=params)
        if response and (resp_json := response.json()):
            for i in resp_json:
                if manga.content_id == i.get("target_id"):
                    return True
        return False

    def delete_user_rate(self, user_rate: UserRate):
        url = f"{self.url_api}/v2/user_rates/{user_rate.id}"
        self.session.request("DELETE", url)

    def get_user_rate(self, manga: Manga):
        url = f"{self.url_api}/v2/user_rates"
        params = {
            "target_type": "Manga",
            "user_id": self.session.user.id,
            "target_id": manga.content_id,
        }
        response = self.session.request("GET", url, params=params)
        if response and (resp_json := response.json()):
            for i in resp_json:
                return UserRate(
                    i.get("id"), i.get("user_id"), i.get("target_id"),
                    i.get("score"), Nl.LibList.from_str(i.get("status")), i.get("chapters"),
                )

    def update_user_rate(self, user_rate: UserRate):
        url = f"{self.url_api}/v2/user_rates/{user_rate.id}"
        status = user_rate.status.to_str()
        if user_rate.status == Nl.LibList.reading:
            status = "watching"
        elif user_rate.status == Nl.LibList.re_reading:
            status = "rewatching"
        elif user_rate.status == Nl.LibList.on_hold:
            status = "on_hold"
        data = {
            "user_rate": {
                "chapters": f"{user_rate.chapters}",
                "score": f"{user_rate.score}",
                "status": status,
            },
        }
        self.session.request("PATCH", url, json=data)


@singleton
class Auth:
    def __init__(self, token=None, scope=None):
        self.client_id = SHIKIMORI_CLIENT_ID
        self.client_secret = SHIKIMORI_CLIENT_SECRET
        self.redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
        self.extra = {"client_id": self.client_id, "client_secret": self.client_secret}
        self.tokens = TokenManager.load_token(ShikimoriLib.CATALOG_NAME)
        self.headers = {"User-Agent": "Shikimori", "Authorization": f"Bearer {self.tokens.get('access_token')}"}
        self.client = self.get_client(scope, self.redirect_uri, token)
        self.refresh_token()
        self.user: User = User(None, None, None)
        self.is_authorized = False
        if self.token:
            self.check_auth()

    def auth_login(self, params):
        self.fetch_token(params["token"])
        self.check_auth()

    def get_client(self, scope, redirect_uri, token):
        client = OAuth2Session(self.client_id, auto_refresh_url=URL_SHIKIMORI_TOKEN, auto_refresh_kwargs=self.extra,
                               scope=scope, redirect_uri=redirect_uri, token=token,
                               token_updater=TokenManager.save_token)
        client.headers.update(self.headers)
        return client

    def get_auth_url(self):
        auth_url = URL_SHIKIMORI + "/oauth/authorize"
        return self.client.authorization_url(auth_url)[0]

    def fetch_token(self, code):
        try:
            self.client.fetch_token(URL_SHIKIMORI_TOKEN, code, client_secret=self.client_secret)
        except Exception as e:
            logging.error(e)
        TokenManager.save_token(self.token, ShikimoriLib.CATALOG_NAME)
        return self.token

    def update_token(self, token):
        if token and "access_token" in token and "refresh_token" in token:
            token = {"access_token": token["access_token"], "refresh_token": token["refresh_token"]}
            TokenManager.save_token(token, catalog_name=ShikimoriLib.CATALOG_NAME)
            self.tokens = token

    def refresh_token(self):
        if not TokenManager.load_token(ShikimoriLib.CATALOG_NAME):
            return False
        try:
            self.client.headers.clear()
            self.client.headers.update(SHIKIMORI_HEADERS)
            self.client.refresh_token(URL_SHIKIMORI_TOKEN, refresh_token=TokenManager.load_token(
                ShikimoriLib.CATALOG_NAME).get("refresh_token"))
            self.update_token(self.token)
            self.client.headers.update({
                "Authorization": f"Bearer {TokenManager.load_token(ShikimoriLib.CATALOG_NAME).get('access_token')}"})
            return self.token
        except Exception as e:
            logging.error(e)

    def request(self, method, url, *, params=None, json=None, ignore_authorize=False):
        if ((not ignore_authorize and not self.is_authorized) or
                "test" in QApplication.arguments() or
                "noshiki" in QApplication.arguments()):
            return
        try:
            response = self.client.request(method, url, params=params, json=json)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logging.error(
                f"\n\tError fetching URL: {url}\n"
                f"\t\tReason: {e}\n"
                f"\t\tHeaders: {self.client.headers}\n"
                f"\t\tParams: {params}\n"
                f"\t\tCookies: {self.client.cookies}\n"
                f"\t\tJson: {json}\n",
            )

    def check_auth(self):
        url = f"{URL_SHIKIMORI_API}/users/whoami"
        whoami = self.request("GET", url, ignore_authorize=True)
        self.is_authorized = whoami and whoami.json()
        return self.is_authorized

    @property
    def token(self):
        return self.client.token
