import rthemelib.plugin_manager as pm
import rthemelib.theme_classes as tc
import os

HOME_ = os.path.expanduser('~')
CSS_FILE_ = f"{HOME_}/.config/gtk-4.0/gtk.css"
CSS_DIR_ = f"{HOME_}/.config/gtk-4.0/"


class Plugin(pm.Plugin):
    def __init__(self, plugin_manager: pm.PluginManager):
        super().__init__(
            "gtk3", "A plugin for GTK3 themes. Requires adw-gtk3",
            "0.1", "PizzaLovingNerd", plugin_manager
        )

    def on_load(self):  # Runs when the plugin is loaded
        pass

    def purge_theme(self):  # Purges the theme.
        if os.path.exists(CSS_FILE_):
            os.remove(CSS_FILE_)

    def apply_theme(self, subvariant: tc.Subvariant):  # Ran when applying a theme.
        self.purge_theme()
        if not os.path.exists(CSS_DIR_):
            os.mkdir(CSS_DIR_)

        lines = [
            "/* AUTOGENERATED BY RTHEME, DO NOT EDIT WITHOUT RUNNING \"rthemed disable\"",
            "OTHERWISE IT MAY BE OVERWRITTEN BY RTHEMED */", ""
        ]
        for items in subvariant.properties.items():
            if items[0] != "custom_css":
                lines.append(f"@define-color {items[0]} {items[1]};")
            else:
                lines.append("")
                lines.append("/* Custom CSS */")
                for item in items[1]["gtk4"].splitlines():
                    lines.append(item)
                lines.append("")
        for line in lines:
            with open(CSS_FILE_, "a") as f:
                f.write(f"{line}\n")
