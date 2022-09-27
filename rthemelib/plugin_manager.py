import importlib
import os

import rthemelib.theme_classes as tc

# PLUGIN_DIR = "/usr/share/rtheme/plugins"
PLUGIN_DIR = "/home/cameron/PycharmProjects/project-beautiful/rthemelib/plugins"


class PluginManager:
    def __init__(self):
        self.plugins = []
        self.load_plugins()

    def load_plugins(self):
        for plugin in os.listdir(PLUGIN_DIR):
            if plugin.endswith(".py"):
                plugin_module = importlib.import_module(f"rthemelib.plugins.{plugin[:-3]}")
                plugin = plugin_module.Plugin(self)
                plugin.on_load()
                self.plugins.append(plugin)

    def get_plugins(self):
        return self.plugins


class Plugin:
    def __init__(self, name: str, description: str, version: str, author: str, plugin_manager: PluginManager):
        self.name = name
        self.description = description
        self.version = version
        self.author = author
        self.plugin_manager = plugin_manager

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


def get_plugins():
    plugin_manager = PluginManager()
    return plugin_manager.get_plugins()
