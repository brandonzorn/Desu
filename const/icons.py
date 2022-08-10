import os
import sys


def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__name__)))
    return os.path.join(base_path, relative_path)


app_icon_path = get_resource_path("images/icon.png")

star_icon_path = get_resource_path("images/star.png")
star_half_icon_path = get_resource_path("images/star_half.png")
star_filled_icon_path = get_resource_path("images/star_filled.png")

gb_icon_path = get_resource_path("images/gb.svg")
ru_icon_path = get_resource_path("images/ru.svg")
jp_icon_path = get_resource_path("images/jp.svg")
