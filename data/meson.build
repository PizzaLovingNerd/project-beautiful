if get_option('daemon').enabled()
  install_data('io.risi.rthemed.desktop',
    install_dir: join_paths(get_option('datadir'), 'applications')
  )
endif

install_data('io.risi.rtheme.gschema.xml',
  install_dir: join_paths(get_option('datadir'), 'glib-2.0/schemas')
)

compile_schemas = find_program('glib-compile-schemas', required: false)
if compile_schemas.found()
  test('Validate schema file',
       compile_schemas,
       args: ['--strict', '--dry-run', meson.current_source_dir()])
endif