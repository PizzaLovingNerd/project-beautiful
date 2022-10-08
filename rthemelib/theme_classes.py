import copy
import yaml


class Subvariant:
    """A class to represent a theme subvariant."""

    def __init__(self, name: str, properties: dict):
        self.name = name
        self.properties = properties
        self.parent_variant = None

class Variant:
    """A class to represent a theme variant."""
    def __init__(self, name: str):
        self.name = name
        self.theme = None
        self.subvariants = []

    def create_subvariants(self, subvariants_dict: dict):
        """Creates subvariants from a dictionary. Some subvariants may be created based on another subvariant."""
        self.subvariants = []
        subvariants = subvariants_dict.keys()
        if "global" in subvariants:
            self.add_subvariant(Subvariant("global", subvariants_dict["global"].copy()))
            if "light" in subvariants:
                light = Subvariant("light", subvariants_dict["global"].copy())
                light.properties.update(subvariants_dict["light"].copy())
                self.add_subvariant(light)
            if "dark" in subvariants:
                dark = Subvariant("dark", subvariants_dict["global"].copy())
                dark.properties.update(subvariants_dict["dark"].copy())
                self.add_subvariant(dark)
        else:
            if "light" in subvariants:
                light = Subvariant("light", subvariants_dict["light"].copy())
                self.add_subvariant(light)
            if "dark" in subvariants:
                dark = Subvariant("dark", subvariants_dict["dark"].copy())
                self.add_subvariant(dark)
        if "light-hc" in subvariants:
            light_hc = Subvariant("light-hc", subvariants_dict["light"].copy())
            light_hc.properties.update(subvariants_dict["light-hc"])
            self.add_subvariant(light_hc)
        if "dark-hc" in subvariants:
            dark_hc = Subvariant("dark-hc", subvariants_dict["dark"].copy())
            dark_hc.properties.update(subvariants_dict["dark-hc"])
            self.add_subvariant(dark_hc)

    def add_subvariant(self, subvariant: Subvariant):
        subvariant.parent_variant = self
        self.subvariants.append(subvariant)

    def get_subvariant_from_name(self, subvariant_name: str) -> Subvariant or None:
        for subvariant in self.subvariants:
            if subvariant.name == subvariant_name:
                return subvariant
        return None


class Theme:
    """A class to represent a theme."""
    def __init__(self):
        self.variants = []  # List of variants of the theme.
        self.invalid = False  # Whether the theme is invalid. Used for displaying if there is an error.
        self.error = ""  # Error message if the theme is invalid.
        self.theme_file = ""  # Path to the theme file.
        self.theme_flags = []  # List of flags of the theme.
        self.theme_data = {}  # Data loaded from the theme

    def parse_yaml(self, file_path: str):
        """Parses the theme file."""
        # Load the theme files
        with open(file_path, "r") as f:
            self.theme_data = yaml.safe_load(f)

        self.theme_file = file_path

        self.theme_flags = self.theme_data["flags"]
        variants = list(self.theme_data.keys())

        if "flags" in variants:  # Make sure that "flags" doesn't get detected as a variant
            variants.remove("flags")

        # Applying main variant on top of other variants
        # I despise this code, but it works. If you have a better way to do this, please create a pull request.
        for variant in variants:
            if variant == "main":
                continue
            for main_subvariant in self.theme_data["main"].keys():
                for subvariant in self.theme_data[variant].keys():
                    if main_subvariant == subvariant:
                        applied_data = self.theme_data["main"][subvariant].copy()
                        applied_data.update(self.theme_data[variant][subvariant])
                        self.theme_data[variant][subvariant] = applied_data

        for v in variants: # Generate variants
            variant = Variant(v)
            variant.theme = self
            variant.create_subvariants(self.theme_data[v])
            self.variants.append(variant)

    def get_variant_from_name(self, variant: str) -> Variant or None:
        """Returns the variant with the specified name."""
        for v in self.variants:
            if v.name == variant:
                return v
        return None

    def get_subvariant_from_name(self, variant: str, subvariant: str) -> Subvariant or None:
        """Convenience function to get a subvariant from a variant."""
        variant = self.get_variant_from_name(variant)
        if variant is not None:
            return variant.get_subvariant_from_name(subvariant)
        return None
