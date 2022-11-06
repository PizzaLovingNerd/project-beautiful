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
# This installs rthemed and rthemelib
$ sudo meson install -C build
```

# Using rtheme
### Using rtheme

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

## Setting a theme
### Adding a theme
In order to add a theme, you need to place the theme into a valid directory. These directories include
- `/usr/share/rthemes` (for system-wide themes)
- `~/.rthemes` and `~/.local/share/rthemes` (for locally installed themes)

### Listing themes
Before we set a theme, we need to check for available themes. You can do this with
```bash
$ rthemelib list-themes
```

### Using GSettings
We are currently using GSettings to store rtheme related settings. To set a theme and theme variant
