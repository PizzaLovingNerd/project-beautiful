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

if get_option('library').enabled()
  subdir('rthemelib')
endif

if get_option('daemon').enabled()
  subdir('rthemed')
endif

gnome.post_install(
  glib_compile_schemas: true,
  update_desktop_database: true,
)

summary({
  'Prefix': get_option('prefix'),
  'rthemelib': get_option('library'),
  'rthemed': get_option('daemon'),
  'GTK4 Plugin': get_option('plugin_gtk4'),
  'GTK3 Plugin': get_option('plugin_gtk3'),
  'GNOME Shell Plugin': get_option('plugin_gnome')
})