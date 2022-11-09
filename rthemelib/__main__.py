import sys

import rthemed
import rthemelib
from gi.repository import Gio

rtheme_settings = Gio.Settings.new("io.risi.rtheme")


def get_subvariant():
    gnome_interface = Gio.Settings.new("org.gnome.desktop.interface")
    gnome_a11y = Gio.Settings.new("org.gnome.desktop.a11y.interface")
    if gnome_a11y.get_boolean("high-contrast"):
        high_contrast = "-hc"
    else:
        high_contrast = ""
    if gnome_interface.get_string("color-scheme") == "prefer-dark":
        return "dark" + high_contrast
    else:
        return "light" + high_contrast


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(rthemelib.constants.HELP_PROMPT)
        exit(1)


    def check_arguments(arg):
        if not len(sys.argv) - 1 == arg:
            print(rthemelib.constants.HELP_PROMPT)
            exit(1)


    match sys.argv[1]:
        case "list-themes":
            themes = rthemelib.get_theme_list()
            if len(themes) != 0:
                print(" ".join(themes))
            else:
                raise Exception(
                    "No themes found. Please install a theme in the following directories: "
                    + " ".join(rthemelib.THEME_DIRS_)
                )
        case "list-variants":
            theme = rthemelib.theme_classes.Theme()
            theme.parse_yaml(rthemelib.get_file_from_name(
                rtheme_settings.get_string("theme-name")
            ))

            variants = []
            for variant in theme.variants:
                variants.append(variant.name)
            print(' '.join(variants))
        case "get-theme-path":
            print(rthemelib.get_current_theme_path())
        case "apply":
            rthemelib.apply_theme(
                rthemelib.get_current_theme(),
                rtheme_settings.get_string("variant-name"),
                get_subvariant()
            )
            print(
                f"{rtheme_settings.get_string('theme-name')}-"
                f"{rtheme_settings.get_string('variant-name')}"
                " applied"
            )
        case default:
            print(rthemelib.constants.HELP_PROMPT)