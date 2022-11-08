# A list of colors named colors that can be used in a theme.
THEME_PROPERTIES = [
    "accent_bg_color",
    "accent_fg_color",
    "accent_color",
    "destructive_bg_color",
    "destructive_fg_color",
    "destructive_color",
    "dialog_bg_color",
    "dialog_fg_color",
    "success_bg_color",
    "success_fg_color",
    "success_color",
    "warning_bg_color",
    "warning_fg_color",
    "warning_color",
    "error_bg_color",
    "error_fg_color",
    "error_color",
    "window_bg_color",
    "window_fg_color",
    "view_bg_color",
    "view_fg_color",
    "headerbar_bg_color",
    "headerbar_fg_color",
    "headerbar_border_color",
    "headerbar_backdrop_color",
    "headerbar_shade_color",
    "card_bg_color",
    "card_fg_color",
    "card_shade_color",
    "popover_bg_color",
    "popover_fg_color",
    "shade_color",
    "scrollbar_outline_color",
    "plugin_properties"
]

# A dictionary of GNOME Palette colors converted to Hex values.
PALETTE_COLORS = {
    "@blue_1": "#99c1f1",
    "@blue_2": "#62a0ea",
    "@blue_3": "#3584e4",
    "@blue_4": "#1c71d8",
    "@blue_5": "#1a5fb4",
    "@green_1": "#8ff0a4",
    "@green_2": "#57e389",
    "@green_3": "#33d17a",
    "@green_4": "#2ec27e",
    "@green_5": "#26a269",
    "@yellow_1": "#f9f06b",
    "@yellow_2": "#f8e45c",
    "@yellow_3": "#f6d32d",
    "@yellow_4": "#f5c211",
    "@yellow_5": "#e5a50a",
    "@orange_1": "#ffbe6f",
    "@orange_2": "#ffa348",
    "@orange_3": "#ff7800",
    "@orange_4": "#e66100",
    "@orange_5": "#c64600",
    "@red_1": "#f66151",
    "@red_2": "#ed333b",
    "@red_3": "#e01b24",
    "@red_4": "#c01c28",
    "@red_5": "#a51d2d",
    "@purple_1": "#dc8add",
    "@purple_2": "#c061cb",
    "@purple_3": "#9141ac",
    "@purple_4": "#813d9c",
    "@purple_5": "#613583",
    "@brown_1": "#cdab8f",
    "@brown_2": "#b5835a",
    "@brown_3": "#986a44",
    "@brown_4": "#865e3c",
    "@brown_5": "#63452c",
    "@light_1": "#ffffff",
    "@light_2": "#f6f5f4",
    "@light_3": "#deddda",
    "@light_4": "#c0bfbc",
    "@light-5": "#9a9996",
    "@dark_1": "#77767b",
    "@dark_2": "#5e5c64",
    "@dark_3": "3d3846",
    "@dark_4": "241f31",
    "@dark_5": "000000",
}

# Dictionary of colors to use for preview.
# Resulting colors are tupled with the light and dark variants.
DEFAULT_COLORS = {
    "accent_color": ("#1c71d8", "#78aeed"),
    "accent_bg_color": ("#3584e4", "#3584e4"),
    "accent_fg_color": ("#ffffff", "#ffffff"),
    "destructive_color": ("#c01c18", "#ff7b63"),
    "destructive_bg_color": ("#e01b24", "#c01c28"),
    "destructive_fg_color": ("#ffffff", "#ffffff"),
    "success_color": ("#26a269", "#8ff0a4"),
    "success_bg_color": ("#2ec27e", "#26a269"),
    "success_fg_color": ("#ffffff", "#ffffff"),
    "warning_color": ("#ae7b03", "#f8e45c"),
    "warning_bg_color": ("#a5a50a", "#cd9309"),
    "warning_fg_color": ("rgba(0, 0, 0, 0.8)", "rgba(0, 0, 0, 0.8)"),
    "error_color": ("#c01c18", "#ff7b63"),
    "error_bg_color": ("#e01b24", "#c01c28"),
    "error_fg_color": ("#ffffff", "#ffffff"),
    "window_bg_color": ("#fafafa", "#242424"),
    "window_fg_color": ("rgba(0, 0, 0, 0.8)", "rgba(0, 0, 0, 0.8)"),
    "view_bg_color": ("#ffffff", "#1e1e1e"),
    "view_fg_color": ("#000000", "ffffff"),
    "headerbar_bg_color": ("#ebebeb", "#303030"),
    "headerbar_fg_color": ("rgba(0, 0, 0, 0.8)", "#ffffff"),
    "headerbar_border_color": ("rgba(0, 0, 0, 0.8)", "#ffffff"),
    "headerbar_backdrop_color": ("#fafafa", "#242424"),
    "headerbar_share_color": ("rgba(0, 0, 0, 0.07)", "rgba(0, 0, 0, 0.36)"),
    "card_bg_color": ("#ffffff", "rgba(255, 255, 255, 0.08)"),
    "card_fg_color": ("rgba(0, 0, 0, 0.8)", "#ffffff"),
    "card_shade_color": ("rgba(0, 0, 0, 0.07)", "rgba(0, 0, 0, 0.36)"),
    "dialog_bg_color": ("#fafafa", "#282828"),
    "dialog_fg_color": ("rgba(0, 0, 0, 0.8)", "#ffffff"),
    "popover_bg_color": ("#ffffff", "#383838"),
    "popover_fg_color": ("rgba(0, 0, 0, 0.8)", "#ffffff"),
    "shade_color": ("rgba(0, 0, 0, 0.07)", "rgba(0, 0, 0, 0.36)"),
    "scrollbar_outline_color": ("#ffffff", "rgba(0, 0, 0, 0.5)")
}

SUB_VARIANTS = [
    "global",
    "light",
    "dark",
    "global-hc",
    "light-hc",
    "dark-hc"
]

FLAGS = [
    "light",
    "dark",
    "hc"
]


HELP_PROMPT = """rTheme: The easiest solution for theming on Linux.

[rthemed/rthemelib] help:       Show this help prompt.

DAEMON COMMANDS:
    rthemed status:             Show the current status of rthemed.
    rthemed start:              Start rthemed
    rthemed stop:               Stop rthemed
    rthemed view-logs:           View the full log

THEME COMMANDS:
    rthemelib list-themes:      List all themes
    rthemelib list-variants:    List current theme variants
    rthemelib get-theme-path:   Get the path to the current theme

Use gsettings to modify the theme settings:
    gsettings set io.risi.rtheme theme-name "rthemed_theme"
    gsettings set io.risi.rtheme variant-name "rthemed_variant"
"""
