## Building

```bash
# Prefix is not required, by default it is set to /usr/local
$ meson build --prefix=/usr
```

## Installing

```bash
# Installation, depending on prefix, most likely requires superuser privledges
$ sudo meson install -C build
```

## Running

```bash
# Run the daemon
$ rthemed start
# Show help menu
$ rthemed help
```
