import contextlib
import json
import os
from functools import wraps
from typing import Callable

import requests
from PySide6.QtCore import QRunnable, Slot, QThreadPool, QLocale
from PySide6.QtWidgets import QApplication

from const.app import APP_NAME
from const.icons import ru_icon_path, gb_icon_path, jp_icon_path, ua_icon_path
from const.lists import MangaKinds
from const.translations import uk_trans_path, en_trans_path, ru_trans_path
from const.urls import DEFAULT_HEADERS


def get_html(url: str, headers: dict = DEFAULT_HEADERS, params=None):
    try:
        assert "test" not in QApplication.arguments(), "Test mode"
        return requests.get(url, headers=headers, params=params)
    except Exception as e:
        print(f"{e=}", f"{url=}", f"{params=}", f"{headers=}", sep="\n")


def get_language_icon(language: str):
    match language:
        case 'ru':
            return ru_icon_path
        case 'en':
            return gb_icon_path
        case 'jp':
            return jp_icon_path
        case 'ua':
            return ua_icon_path
        case _:
            return ''


def get_status(status: str) -> str:
    match status:
        case 'ongoing':
            return translate("Other", status.capitalize())
        case 'completed' | 'released':
            return translate("Other", 'completed'.capitalize())
        case _:
            if status:
                return status.capitalize()


def get_manga_kind(kind: str) -> None:
    kinds_matches = {'manga': MangaKinds.manga, 'manhwa': MangaKinds.manhwa, 'manhua': MangaKinds.manhua,
                     'one_shot': MangaKinds.one_shot, 'doujin': MangaKinds.doujin, 'ranobe': MangaKinds.ranobe}
    assert kind in kinds_matches, f"Not fond matches for {kind}"
    return kinds_matches[kind]


def get_locale_path(locale: QLocale.Language) -> str:
    match locale:
        case QLocale.Language.Russian:
            return ru_trans_path
        case QLocale.Language.Ukrainian:
            return uk_trans_path
        case _:
            return en_trans_path


def translate(context, string):
    return QApplication.translate(context, string, None)


def get_data(a: dict, path: list, default_val=None):
    if default_val is None:
        default_val = {}
    data = a
    for p in path:
        try:
            data = data.get(p)
        except Exception as e:
            data = default_val
            print("Get data error\t", e)
    return data


def singleton(cls):
    instance = [None]

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper


def with_lock_thread(locker):
    def decorator(func: Callable):

        @wraps(func)
        def wrapper(*args, **kwargs):
            with locker:
                return func(*args, **kwargs)
        return wrapper
    return decorator


class Worker(QRunnable):
    def __init__(self, func: Callable, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        self.func(*self.args, **self.kwargs)

    def start(self):
        QThreadPool.globalInstance().start(self)


@contextlib.contextmanager
def lock_ui(ui_to_lock: list):
    [i.setEnabled(False) for i in ui_to_lock]
    yield
    [i.setEnabled(True) for i in ui_to_lock]


class TokenManager:
    path = f'{APP_NAME}/tokens'

    @staticmethod
    def save_token(token, catalog_name='Shikimori'):
        path = f'{TokenManager.path}/{catalog_name}'
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        with open(f'{path}/token.json', 'w') as f:
            f.write(json.dumps(token))

    @staticmethod
    def load_token(catalog_name):
        path = f'{TokenManager.path}/{catalog_name}'
        if os.path.exists(f'{path}/token.json'):
            with open(f'{path}/token.json') as f:
                data = json.load(f)
                if data:
                    return data
        return {}
