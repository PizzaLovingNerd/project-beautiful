import glob
import importlib
import os
import site

from pathlib import Path

import rthemelib.theme_classes
import rthemelib.theme_classes as tc

import gi
gi.require_version("Gio", "2.0")
from gi.repository import Gio

SITE_DIRS = site.getsitepackages()


class PluginManager:
    def __init__(self):
        self.loaded_plugins = []
        settings = Gio.Settings.new("io.risi.rtheme")
        self.enabled_plugins = settings.get_strv("enabled-plugins")
        self.load_plugins()

    def get_loaded_plugins(self):
        return self.loaded_plugins

    def load_plugins(self):
        for plugin_class in get_available_plugins():
            if plugin_class.name in self.enabled_plugins:
                plugin = plugin_class(self)
                plugin.on_load()
                self.loaded_plugins.append(plugin)


class Plugin:
    name = None
    description = None
    version = None
    author = None
    plugin_properties = []
    flags = []

    def __init__(self, plugin_manager: PluginManager):
        self.plugin_manager = plugin_manager

        if not self.name:
            raise ValueError("Plugin name must be set.")
        if not self.version:
            raise ValueError("Plugin version must be set.")
        if not self.author:
            raise ValueError("Plugin author must be set.")

    def on_load(self):
        """Runs when the plugin is loaded."""
        pass

    def pre_apply(self):
        """Ran before applying a theme. This is useful for plugins that need to
        edit the theme before it is applied."""
        pass

    def purge_theme(self):
        """Removes any theming files generated by the plugin.
        We recommend using this function when removing the plugin and
        when applying a theme to prevent any errors when reapplying the theme."""
        pass

    def apply_theme(self, subvariant: tc.Subvariant):  # Ran when applying a theme.
        pass

    def subvariant_has_plugin_property(self, sv: rthemelib.theme_classes.Subvariant, prop: str):
        if self.name in sv.plugin_properties:
            if prop in sv.plugin_properties[self.name]:
                return sv.plugin_properties[self.name][prop]
        return None


def get_plugins():
    plugin_manager = PluginManager()
    return plugin_manager.get_plugins()


def get_available_plugins():
    plugins = []
    plugin_dirs = [x for x in SITE_DIRS if (Path(x) / "rthemelib" / "plugins").is_dir()]
    for directory in plugin_dirs:
        plugin_path = Path(directory) / "rthemelib" / "plugins"
        for possible_plugin in plugin_path.glob("*.py"):
            plugin_name = (os.path.basename(possible_plugin).split('/')[-1].split('.')[0])
            try:
                plugin_module = importlib.import_module(f"rthemelib.plugins.{plugin_name}")
                plugins.append(plugin_module.Plugin)
            except ImportError as e:
                print(e)
                pass
        for possible_plugin in plugin_path.iterdir():
            if (possible_plugin / "__main__.py").is_file():
                plugin_name = (os.path.basename(possible_plugin).split('/')[-1].split('.')[0])
                try:
                    plugin_module = importlib.import_module(
                        f"rthemelib.plugins.{plugin_name}.__main__"
                    )
                    plugins.append(plugin_module.Plugin)
                except ImportError as e:
                    print(e)
                    pass
    return plugins