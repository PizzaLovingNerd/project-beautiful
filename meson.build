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

systemd = dependency('systemd', version: '>= 242', required: true)
if systemd.found()
  systemduserunitdir = get_option('systemduserunitdir')
  if systemduserunitdir == ''
    systemduserunitdir = systemd.get_variable(
      pkgconfig: 'systemduserunitdir',
      pkgconfig_define: ['prefix', get_option('prefix')]
    )
  endif
endif

subdir('data')
subdir('themes')
subdir('rthemelib')
subdir('rthemed')

gnome.post_install(
     glib_compile_schemas: true,
  update_desktop_database: true,
)

summary({
  'Prefix': get_option('prefix')
})