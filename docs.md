# Installing

## Installing via meson
This is the manually way to install rthemelib and rthemed for all Linux distro.
We recommend using your distro's package manager first before using this method, if your distro has a package.

### meson build
```bash
# Prefix is not required, by default it is set to /usr/local
$ meson build --prefix=/usr
```
### meson install

```bash
# Installation, depending on prefix, most likely requires superuser privledges.
# This installs rthemed and rthemelib. You can change the install directory by changing the prefix.
$ sudo meson install -C build --prefix=/usr
```

# Using rtheme

## rthemed

### Start with systemd
```bash
$ systemctl start --user rthemed
```
### Running manually
##### We recommend only doing this if you are on a systemd-free distro, or you are testing.
```bash
$ rthemed start
```

## Adding a theme
In order to add a theme, you need to place the theme into a valid directory. These directories include
* `/usr/share/rthemes` (for system-wide themes)
* `~/.rthemes` and `~/.local/share/rthemes` (for locally installed themes)

### Listing themes
Before we set a theme, we need to check for available themes. You can do this with:
```bash
$ rthemelib list-themes
```
Setting a theme also requires setting a variant.
```bash
$ rthemelib list-variants
```
If you are unsure which variant to use, use the `main` variant as that is a variant all themes must have, and is considered default.


## Setting a theme
### risiTweaks
If you are running risiOS, the risiTweaks tool allows you to set the theme and variant within risiOS.

### Using GSettings
If you aren't on risiOS, we are currently working on a GUI tool for other distros, but in the meantime,
we are currently using GSettings to store rtheme related settings. To set a theme and theme variant use the following commands:
```bash
$ gsettings set io.risi.rtheme theme-name "rthemed_theme"
$ gsettings set io.risi.rtheme variant-name "rthemed_variant"
```
### Applying the theme
If you have rthemed running, it should than automatically change the theme. If not, you can apply the theme by running:
```bash
$ rthemelib apply
```

# Creating a theme
## Anatomy of a theme
A rtheme is made using yaml. This provides a human-readable format for themes that is easy to understand and edit.
Here is an example of a theme:
```yaml
flags:  #  <-  Flags are used to determine how the theme should be applied.
    - light  # <- Flag to allow light theme
    - dark  # <- Flag to allow dark theme
main:   #  <-  The main variant required by all themes.
    light:  #  <- Light subvariant used for the light theme
        accent_color: "#ed4a3f"  # <- accent_color property
        destructive_color: "#d81c1c"
        destructive_bg_color: "#e01b24"
        success_color: "#26a269"
        success_bg_color: "#2ec27e"
        warning_color: "#ae7b03"
        warning_bg_color: "#e5a50a"
        error_color: "#c01c28"
        error_bg_color: "#e01b24"
        window_bg_color: "#f6f5f4"
        window_fg_color: "rgba(0, 0, 0, 0.8)"
        view_bg_color: "#ffffff"
        view_fg_color: "rgba(0, 0, 0, 0.8)"
        headerbar_bg_color: "#d9d9d9"
        headerbar_fg_color: "rgba(0, 0, 0, 0.8)"
        headerbar_border_color: "rgba(0, 0, 0, 0.8)"
        headerbar_backdrop_color: "#f6f5f4"
        headerbar_shade_color: "rgba(0, 0, 0, 0.07)"
        card_bg_color: "#ffffff"
        card_fg_color: "rgba(0, 0, 0, 0.8)"
        card_shade_color: "rgba(0, 0, 0, 0.07)"
        popover_bg_color: "#ffffff"
        popover_fg_color: "rgba(0, 0, 0, 0.8)"
        shade_color: "rgba(0, 0, 0, 0.07)"
        scrollbar_outline_color: "#ffffff"
    dark:  # <- Dark subvariant used for the dark theme
        accent_color: "#cb3f40"
        destructive_color: "#ff7b63"
        destructive_bg_color: "#c01c28"
        success_color: "#8ff0a4"
        success_bg_color: "#26a269"
        warning_color: "#f0c05a"
        warning_bg_color: "#f8e45c"
        error_color: "#ff7b63"
        error_bg_color: "#c01c28"
        window_bg_color: "#353535"
        window_fg_color: "#ffffff"
        view_bg_color: "#2d2d2d"
        view_fg_color: "#ffffff"
        headerbar_bg_color: "#292929"
        headerbar_fg_color: "#ffffff"
        headerbar_border_color: "#ffffff"
        headerbar_backdrop_color: "#242424"
        headerbar_shade_color: "rgba(0, 0, 0, 0.36)"
        card_bg_color: "rgba(255, 255, 255, 0.08)"
        card_fg_color: "#ffffff"
        card_shade_color: "rgba(0, 0, 0, 0.36)"
        popover_bg_color: "#1e1e1e"
        popover_fg_color: "#ffffff"
        shade_color: "rgba(0, 0, 0, 0.36)"
        scrollbar_outline_color: "rgba(0, 0, 0, 0.5)"
    global: # <- Global properties that are used for all subvariants unless overwritten by a subvariant.
        accent_bg_color: "#ff4033"
        accent_fg_color: "#ffffff"
        destructive_fg_color: "#ffffff"
        success_fg_color: "#ffffff"
        warning_fg_color: "rgba(0, 0, 0, 0.8)"
        error_fg_color: "#ffffff"
        plugin_properties:
            gnome_shell:
                panel_color: "#292929"
                custom_css: |
                    #dash .dash-background {
                        background-color: transparent;}
                    #overviewGroup {
                        background-color: #292929; }
blue_accent_color: # <- Custom variant that applies a blue accent color.
    light:
        accent_color: "#1c71d8"
    dark:
        accent_color: "#3584e4"
    global:
        accent_bg_color: "#62a0ea"
```

rthemes are made up of 4 things. Flags at the top, then variants and subvariants under each variant. And properties that
each subvariant can have. Please refer to the example above for a better understanding of how to implement these things.

### Flags
Flags are used to specific what themes are applied. The current flags are:
* `light`
* `dark`
* `light-hc`
* `dark-hc`

At the moment, the light and dark flags are used to determine what modes a theme supports.
The light-hc and dark-hc flags are used to determine if a theme supports high contrast mode,
although high contrast support is still in development, so this is mainly for future use.

### Variants
Variants are used to allow variants of a theme.
For example, you can make different variants of a theme for different accent colors,
or to more closely match a distribution's branding.

All themes must have a `main` variant, which is used as the default variant. Outside the main variant,
you can make as many or as little variants as you want.

Each variant than contains different subvariants for different modes.

### Subvariants
Subvariants are used to specify what colors are used for each mode.
The current subvariants are:
* `global`
* `light`
* `dark`
* `global-hc`
* `light-hc`
* `dark-hc`
* 
The global subvariant is used to specify colors that are set in both the light and dark subvariants.
Then the light and dark subvariants are applied on top of the global subvariant.

The "*-hc" variants are used to specify colors that are used in high contrast mode. As mentioned earlier,
high contrast mode is still in development, so this is mainly for future-proofing your theme.

### Properties:
Each subvariant has a subset of properties that determine theme colors. The default properties are:
* `accent_color`
* `destructive_color`
* `destructive_bg_color`
* `success_color`
* `success_bg_color`
* `warning_color`
* `warning_bg_color`
* `error_color`
* `error_bg_color`
* `window_bg_color`
* `window_fg_color`
* `view_bg_color`
* `view_fg_color`
* `headerbar_bg_color`
* `headerbar_fg_color`
* `headerbar_border_color`
* `headerbar_backdrop_color`
* `headerbar_shade_color`
* `card_bg_color`
* `card_fg_color`
* `card_shade_color`
* `popover_bg_color`
* `popover_fg_color`
* `shade_color`
* `scrollbar_outline_color`
* `accent_bg_color`
* `accent_fg_color`
* `destructive_fg_color`
* `success_fg_color`
* `warning_fg_color`
* `error_fg_color`

These default properties are based on Libadwaita's named color palette. You can find more information here:
https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/named-colors.html

Each property can hold either a hex color (`#ffffff`), a rgba color (`rgba(255, 255, 255, 0.5)`).
Some plugins can also have their own properties specified with the `plugin_properties` property.

### Plugin Properties:
Plugin properties are used to specify properties that are specific to a plugin.
When setting plugin properties, you must specify the plugin name under `plugin_properties`
and then the properties you want to set.

For example, if you wanted to set the panel color for the gnome-shell plugin, you would do:
```yaml
plugin_properties:
    gnome_shell:
        panel_color: "#292929"
```

# Default Plugins:
## gtk3 and gtk4:
These plugins are used to set the colors for GTK3 and GTK4 applications.
These plugins automatically generate a theme from the default properties, and only have 1 custom plugin property:
* `custom_css`
This custom_css property is used to add additional CSS to the theme.

## gnome_shell:
This is the plugin used to set the colors for the gnome-shell.
At the moment this is only supported on risiOS 37 (and later), but we are working on adding support for other
Linux distributions through a GNOME extension.

This attempts to generate a theme based on the dark subvariant, but will fallback to the light variant if
there is no dark subvariant. It also uses the light subvariant if you run gnome-classic.

This plugin's only 2 custom plugin properties are:
* `panel_color`
* `custom_css`

However, you can also override the properties set by the default properties using the following custom properties.
* `dark_base_color`
* `light_base_color`
* `bg_color_light`
* `bg_color_dark`
* `fg_color_light`
* `fg_color_dark`
* `selected_fg_color`
* `selected_bg_color`
* `selected_borders_color_light`
* `selected_borders_color_dark`
* `borders_color_light`
* `borders_color_dark`
* `borders_edge_light`
* `borders_edge_dark`
* `link_color_light`
* `link_color_dark`
* `link_visited_color_light`
* `link_visited_color_dark`
* `warning_color_light`
* `warning_color_dark`
* `error_color_light`
* `error_color_dark`
* `success_color_light`
* `success_color_dark`
* `destructive_color`
* `osd_fg_color`
* `osd_bg_color`
* `osd_insensitive_bg_color`
* `osd_insensitive_fg_color_light`
* `osd_insensitive_fg_color_dark`
* `osd_borders_color`
* `osd_outer_borders_color`
* `shadow_color_light`
* `shadow_color_dark`
* `card_bg_color_light`
* `card_bg_color_dark`
* `card_outer_borders_color`
* `bubble_bubble_color_light`
* `bubble_bubble_color_dark`
* `system_bg_color`
* `insensitive_fg_color`
* `insensitive_bg_color`
* `insensitive_borders_color`
* `backdrop_base_color_light`
* `backdrop_base_color_dark`
* `backdrop_bg_color`
* `backdrop_fg_color`
* `backdrop_insensitive_fg_color_light`
* `backdrop_insensitive_fg_color_dark`
* `backdrop_borders_color`
* `backdrop_dark_fill`
* `checked_bg_color_light`
* `checked_bg_color_dark`
* `checked_fg_color_light`
* `checked_fg_color_dark`
* `hover_bg_color_light`
* `hover_bg_color_dark`
* `hover_fg_color_light`
* `hover_fg_color_dark`
* `active_bg_color_light`
* `active_bg_color_dark`
* `active_fg_color_light`
* `active_fg_color_dark`

You can also disable shell theming by adding the `no_gnome_shell` flag to the theme at the top.
