import sys
import rthemelib
from gi.repository import Gio

rtheme_settings = Gio.Settings.new("io.risi.rtheme")

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
            print(" ".join(rthemelib.list_themes()))
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
            print(
                rthemelib.get_file_from_name(
                    rtheme_settings.get_string("theme-name")
                )
            )
        case default:
            print(rthemelib.constants.HELP_PROMPT)