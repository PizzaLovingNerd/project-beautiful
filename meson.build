project('rtheme',
          version: '0.1.0',
    meson_version: '>= 0.59.0',
  default_options: [ 'warning_level=2', 'werror=false', ],
)

python = import('python')
gnome = import('gnome')

py = python.find_installation('python3', required: true, modules: [
  'pydbus', 'gi'
])

subdir('data')
subdir('themes')
subdir('rthemelib')
subdir('rthemed')

gnome.post_install(
     glib_compile_schemas: true,
#    gtk_update_icon_cache: true,
  update_desktop_database: true,
)