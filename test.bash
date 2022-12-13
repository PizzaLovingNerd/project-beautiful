#rm -rf build && meson build && sudo meson install -C build && rthemed start
rm -rf build && meson build --prefix=/usr && sudo meson install -C build && python3 -m rthemelib apply
