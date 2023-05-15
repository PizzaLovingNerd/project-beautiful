import os
import yaml

from gi.repository import GLib, Gio

import rthemelib.theme_classes as tc
import rthemelib.plugin_manager as pm
import rthemelib.constants as constants

HOME_ = os.path.expanduser('~')
THEME_DIRS_ = [(x + "/rthemes").replace("//", "/") for x in GLib.get_system_data_dirs()] + \
    [GLib.get_user_data_dir() + "/rthemes", GLib.get_home_dir() + "/.rthemes"]

manager = pm.PluginManager()
rtheme_settings = Gio.Settings.new("io.risi.rtheme")


def check_yaml(theme_file: str) -> tuple[bool, str]:
    """Parses the theme file to make sure that it's valid."""
    try:
        with open(theme_file, "r") as f:
            theme_data = yaml.safe_load(f)
    except (yaml.parser.ParserError, FileNotFoundError) as e:
        return False, repr(e)

    # Check Flags
    if "flags" not in theme_data:
        return False, "No flags found"
    # Removed due to plugins having custom flags
    # for flag in theme_data["flags"]:
    #     if flag not in constants.DEFAULT_FLAGS:
    #         return False, f"Invalid flag: {flag}"
    if "light" not in theme_data["flags"] and "dark" not in theme_data["flags"]:
        return False, "No light or dark flag found"

    flags = theme_data["flags"]
    variants = list(theme_data.keys())
    variants.remove("flags")  # Make sure that "flags" doesn't get detected as a variant

    # Check to make sure that each variant has a subvariant that matches the specified flags.
    for variant in variants:
        subvariants = list(theme_data[variant].keys())
        if "light" not in flags and ("light" in subvariants or "global" not in subvariants):
            return False, f"light flag found in {variant} without light or global subvariant in {variant}"
        if "light" in theme_data["flags"] and "light" not in subvariants:
            return False, f"light subvariant found in {variant} without light flag"
        if "dark" not in theme_data["flags"] and ("dark" in subvariants or "global" not in subvariants):
            return False, f"dark flag found without dark or global subvariant in {variant}"
        if "dark" in theme_data["flags"] and "dark" not in subvariants:
            return False, f"dark subvariant found in {variant} without dark flag"
        if "hc" in theme_data["flags"]:
            if "light" in theme_data["flags"] and "light-hc" in subvariants:
                return False, f"light and high Contrast flags found without light-hc subvariant in {variant}"
            if "dark" in theme_data["flags"] and "dark-hc" in subvariants:
                return False, f"dark and high Contrast flags found without dark-hc subvariant in {variant}"
        if "hc" not in theme_data["flags"] and "light-hc" in subvariants:
            return False, f"light high contrast subvariant found in {variant} without hc flag"
        if "hc" not in theme_data["flags"] and "dark-hc" in subvariants:
            return False, f"dark high contrast subvariant found in {variant} without hc flag"
        if "hc" not in theme_data["flags"] and "global-hc" in subvariants:
            return False, f"global high contrast subvariant found in {variant} without hc flag"

    # Check for main variant
    if "main" not in theme_data:
        return False, "No main variant found"

    # Check Subvariants
    for variant in variants:
        for subvariant in theme_data[variant]:
            if subvariant not in constants.SUB_VARIANTS:
                return False, f"Invalid subvariant: {subvariant}"
            for theme_property in theme_data[variant][subvariant]:
                if theme_property not in constants.THEME_PROPERTIES:
                    return False, f"Invalid property: {theme_property}"

    return True, "Valid Theme"


def apply_theme(theme: tc.Theme, variant_name: str, subvariant_name: str):
    for plugin in manager.loaded_plugins:
        plugin.apply_theme(theme.get_subvariant_from_name(variant_name, subvariant_name))


def get_theme_list() -> list[str]:
    themes = []
    for theme_dir in THEME_DIRS_:
        if os.path.isdir(theme_dir):
            for theme in os.listdir(theme_dir):
                if check_yaml(f"{theme_dir}/{theme}")[0]:
                    themes.append(theme.replace(".rtheme", "").replace(".yaml", "").replace(".yml", ""))
    return themes


def get_file_from_name(name) -> str:
    if os.path.isfile(name):
        return name
    else:
        for theme_dir in THEME_DIRS_:
            if os.path.isdir(theme_dir):
                for theme in os.listdir(theme_dir):
                    if theme == f"{name}.rtheme" or theme == f"{name}.yaml" \
                            or theme == f"{name}.yml" \
                            and check_yaml(f"{theme_dir}/{theme}")[0]:
                        return f"{theme_dir}/{theme}"
    return None


def get_current_theme() -> tc.Theme:
    theme = tc.Theme()
    theme.parse_yaml(get_file_from_name(
        rtheme_settings.get_string("theme-name")
    ))
    return theme


def get_current_theme_path() -> str:
    return get_file_from_name(
        rtheme_settings.get_string("theme-name")
    )


# TEMPORARY, REMOVE IN 2 RELEASES
# This is to deal with us renaming the preinstalled nord theme to solarized
if rtheme_settings.get_string("theme-name") == "nord" and "nord" not in get_theme_list():
    rtheme_settings.set_string("theme-name", "solarized")
