import rthemelib
import sys
from gi.repository import Gio

rtheme_settings = Gio.Settings.new("io.risi.rtheme")

def help_prompt():
    print("""rThemeD: The daemon for modifying rtheme settings and on the fly theme modification.

rthemed help:               Show this help prompt.

DAEMON COMMANDS:
    rthemed status:         Show the current status of rthemed.
    rthemed enable:         Enable rthemed
    rthemed disable:        Disable rthemed
    rthemed reload:         Reload rthemed
    rthemed start:          Start rthemed
    rthemed stop:           Stop rthemed
    rthemed view-log:       View the full log

THEME COMMANDS:
    rthemed list-themes:    List all themes
    rthemed list-variants:  List current theme variants
    rthemed get-theme:      Get the current theme
    rthemed get-variant:    Get the current variant
    rthemed get-theme-path: Get the path to the current theme
    rthemed refresh:        Refresh the theme list

Use gsettings to modify the theme settings:
    gsettings set io.risi.rtheme theme-name "rthemed_theme"
    gsettings set io.risi.rtheme variant-name "rthemed_variant"
""")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help_prompt()
        exit(1)


    def check_arguments(arg):
        if not len(sys.argv) - 1 == arg:
            help_prompt()
            exit(1)


    match sys.argv[1]:
        case "status":
            check_arguments(1)
        case "enable":
            check_arguments(1)
        case "disable":
            check_arguments(1)
        case "reload":
            check_arguments(1)
        case "start":
            check_arguments(1)
        case "stop":
            check_arguments(1)
        case "view-log":
            check_arguments(1)

        case "list-themes":
            check_arguments(1)
        case "list-variants":
            check_arguments(1)
        case "get-theme":
            check_arguments(1)
        case "get-variant":
            check_arguments(1)
        case "get-theme-path":
            check_arguments(1)
        case "refresh":
            check_arguments(1)

        case default:
            help_prompt()