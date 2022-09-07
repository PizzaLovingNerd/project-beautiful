# Only used for development purpose.
import __main__ as main
import theme_classes as tc

theme = tc.Theme()
theme.parse_yaml("/home/cameron/PycharmProjects/project-beautiful/themes/theme_template.yml")
main.apply_theme(theme, "main", "light")
