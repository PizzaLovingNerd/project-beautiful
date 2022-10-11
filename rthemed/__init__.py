import rthemelib
import rthemelib.theme_classes as tc
from gi.repository import Gio
from gi.repository import GLib

gnome_interface = Gio.Settings.new("org.gnome.desktop.interface")
gnome_a11y = Gio.Settings.new("org.gnome.desktop.a11y.interface")
gnome_notifications = Gio.Settings.new("org.gnome.desktop.notifications")
rtheme_settings = Gio.Settings.new("io.risi.rtheme")


class Logger:
    def __init__(self):
        self.logs = []

    def log(self, text):
        self.logs.append(text)
        print(text)

    def get_logs(self):
        return self.logs

    def clear_logs(self):
        self.logs = []

    def get_last_log(self):
        return self.logs[-1]


def get_subvariant():
    if gnome_a11y.get_boolean("high-contrast"):
        high_contrast = "-hc"
    else:
        high_contrast = ""
    if gnome_interface.get_string("color-scheme") == "prefer-dark":
        return "dark" + high_contrast
    else:
        return "light" + high_contrast


def apply_theme():
    rthemelib.apply_theme(
        rthemelib.get_current_theme(),
        rtheme_settings.get_string("variant-name"),
        get_subvariant()
    )

