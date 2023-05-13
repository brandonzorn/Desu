import requests
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QApplication

from nlightreader.consts import DEFAULT_HEADERS, MangaKinds
from nlightreader.consts.files import LangIcons, Translations, Styles


def get_html(url: str, headers: dict = DEFAULT_HEADERS, params=None, json=None, cookies=None, content_type=None):
    try:
        assert "test" not in QApplication.arguments(), "Test mode"
        response = requests.get(url, headers=headers, params=params, json=json, cookies=cookies)
        if content_type:
            if not response or response.status_code != 200:
                return
            if content_type == 'content':
                return response.content
            if content_type == 'json':
                return response.json()
        return response
    except Exception as e:
        print(f"{e=}", f"{url=}", f"{params=}", f"{headers=}", sep="\n")


def get_language_icon(language: str):
    match language:
        case 'ru':
            return LangIcons.Ru
        case 'en':
            return LangIcons.Gb
        case 'jp':
            return LangIcons.Jp
        case 'ua':
            return LangIcons.Ua
        case _:
            return ''


def get_manga_kind(kind: str) -> MangaKinds:
    kinds_matches = {'manga': MangaKinds.manga, 'manhwa': MangaKinds.manhwa, 'manhua': MangaKinds.manhua,
                     'one_shot': MangaKinds.one_shot, 'doujin': MangaKinds.doujin, 'ranobe': MangaKinds.ranobe}
    assert kind in kinds_matches, f"Not fond matches for {kind}"
    return kinds_matches[kind]


def get_locale(locale: QLocale.Language) -> str:
    match locale:
        case QLocale.Language.Russian:
            return Translations.Ru
        case QLocale.Language.Ukrainian:
            return Translations.Uk
        case _:
            return Translations.En


def get_data(data: dict, path: list, default_val=None):
    if not isinstance(data, dict):
        raise ValueError("Data is not dict")
    if default_val is None:
        default_val = {}
    for p in path:
        try:
            data = data[p]
        except KeyError:
            return default_val
    return data


def get_ui_style(style: str):
    dark = Styles.Dark
    light = Styles.Light
    themes = {"Dark": dark, "Light": light}
    return themes[style]
