import os
import shutil

from typing import Tuple

HOME_ = os.path.expanduser('~')
CSS_FILE_ = f"{HOME_}/.config/gtk-4.0/gtk.css"
CSS_FILE_3_ = f"{HOME_}/.config/gtk-3.0/gtk.css"

class Varient:
    def __init__(self):
        self.light_theme = {}
        self.dark_theme = {}
        self.light_custom_css = ""
        self.dark_custom_css = ""

    def property(self, light_prop: Tuple(str, str), dark_prop: Tuple(str, str)):
        self.light_theme[light_prop[0]] = light_prop[1]
        self.dark_theme[dark_prop[0]] = dark_prop[1]

class Theme:
    def __init__(self):
