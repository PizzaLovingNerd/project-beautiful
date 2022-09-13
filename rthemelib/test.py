# Only used for development purpose.
import rthemelib
import theme_classes as tc

theme = tc.Theme()
theme.parse_yaml("/home/cameron/PycharmProjects/project-beautiful/themes/theme_template.yml")
rthemelib.apply_theme(theme, "main", "light")
print(rthemelib.get_theme_list())
