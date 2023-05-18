automatic = {
    "43": {
        "dark_base_color": ("window_bg_color_dark", "desaturate($dark_4, 100%)"),
        "light_base_color": ("window_bg_color_light", "$light_1"),
        "bg_color_light": ("window_bg_color_light", "$light_2"),
        "bg_color_dark": (None, "lighten($base_color, 5%)"),
        "fg_color_light": ("window_fg_color_light", "transparentize(black, .2)"),
        "fg_color_dark": ("window_fg_color_dark", "white"),
        "selected_fg_color": ("accent_fg_color_dark", "$light_1"),
        "selected_bg_color": ("accent_bg_color_dark", "$blue_3"),
        "selected_borders_color_light": (None, "darken($selected_bg_color, 15%)"),
        "selected_borders_color_dark": (None, "darken($selected_bg_color, 30%)"),
        "borders_color_light": (None, "transparentize($fg_color, .5)"),
        "borders_color_dark": (None, "transparentize($fg_color, .9)"),
        "borders_edge_light": (None, "rgba(255,255,255,0.8)"),
        "borders_edge_dark": (None, "lighten($bg_color, 5%)"),
        "link_color_light": (None, "darken($selected_bg_color, 10%)"),
        "link_color_dark": (None, "lighten($selected_bg_color, 20%)"),
        "link_visited_color_light": (None, "darken($selected_bg_color, 20%)"),
        "link_visited_color_dark": (None, "lighten($selected_bg_color, 10%)"),
        "warning_color_light": ("warning_bg_color_light", "$yellow_5"),
        "warning_color_dark": ("warning_bg_color_dark", "#cd9309"),
        "error_color_light": ("error_bg_color_light", "$red_3"),
        "error_color_dark": ("error_bg_color_dark", "$red_4"),
        "success_color_light": ("success_bg_color_light", "$green_4"),
        "success_color_dark": ("success_bg_color_dark", "$green_5"),
        "destructive_color": (None, "$error_color"),
        "osd_fg_color": ("window_fg_color_dark", "$light_1"),
        "osd_bg_color": ("window_bg_color_dark", "$_dark_base_color"),
        "osd_insensitive_bg_color": (None, "transparentize(mix($osd_fg_color, opacify($osd_bg_color, 1), 10%), 0.5)"),
        "osd_insensitive_fg_color_light": (None, "mix($osd_fg_color, $osd_bg_color, 80%)"),
        "osd_insensitive_fg_color_dark": (None, "mix($osd_fg_color, $osd_bg_color, 70%)"),
        "osd_borders_color": (None, "transparentize(black, 0.3)"),
        "osd_outer_borders_color": (None, "transparentize($osd_fg_color, 0.9)"),
        "shadow_color_light": (None, "rgba(0,0,0,0.1)"),
        "shadow_color_dark": (None, "rgba(0,0,0,0.2)"),
        "bubble_bubble_color_light": (None, "darken($bg_color, 7%)"),
        "bubble_bubble_color_dark": (None, "lighten($bg_color, 5%)"),
        "system_bg_color": (None, "$base_color"),
        "insensitive_fg_color": (None, "mix($fg_color, $bg_color, 50%)"),
        "insensitive_bg_color": (None, "mix($fg_color, $base_color, 60%)"),
        "insensitive_borders_color": (None, "mix($borders_color, $base_color, 60%)"),
        "backdrop_base_color_light": (None, "darken($bg_color,1%)"),
        "backdrop_base_color_dark": (None, "lighten($bg_color,1%)"),
        "backdrop_bg_color": (None, "$bg_color"),
        "backdrop_fg_color": (None, "mix($fg_color, $backdrop_bg_color, 80%)"),
        "backdrop_insensitive_fg_color_light": (None, "darken($backdrop_bg_color,15%)"),
        "backdrop_insensitive_fg_color_dark": (None, "lighten($backdrop_bg_color,15%)"),
        "backdrop_borders_color": (None, "mix($borders_color, $bg_color, 90%)"),
        "backdrop_dark_fill": (None, "mix($backdrop_borders_color,$backdrop_bg_color, 35%)"),
        "checked_bg_color_light": (None, "darken($bg_color, 7%)"),
        "checked_bg_color_dark": (None, "lighten($bg_color, 7%)"),
        "checked_fg_color_light": (None, "darken($fg_color, 7%)"),
        "checked_fg_color_dark": (None, "lighten($fg_color, 7%)"),
        "hover_bg_color_light": (None, "darken($bg_color, 3%)"),
        "hover_bg_color_dark": (None, "lighten($bg_color, 10%)"),
        "hover_fg_color_light": (None, "darken($fg_color, 5%)"),
        "hover_fg_color_dark": (None, "lighten($fg_color, 10%)"),
        "active_bg_color_light": (None, "darken($bg_color, 5%)"),
        "active_bg_color_dark": (None, "lighten($bg_color, 12%)"),
        "active_fg_color_light": (None, "darken($fg_color, 5%)"),
        "active_fg_color_dark": (None, "lighten($fg_color, 12%)")
    },
    "44": {
        "dark_base_color": ("window_bg_color_dark", "darken(desaturate(#241f31, 100%), 2%)"),
        "light_base_color": ("window_bg_color_light", "#fff"),
        "bg_color_light": ("window_bg_color_light", "#f6f5f4"),
        "bg_color_dark": (None, "lighten($base_color, 5%)"),
        "fg_color_light": ("window_fg_color_light", "transparentize(black, .2)"),
        "fg_color_dark": ("window_fg_color_dark", "white"),
        "selected_fg_color": ("accent_fg_color_dark", "#fff"),
        "selected_bg_color": ("accent_bg_color_dark", "#3584e4"),
        "selected_borders_color_light": (None, "darken($selected_bg_color, 15%)"),
        "selected_borders_color_dark": (None, "darken($selected_bg_color, 30%)"),
        "borders_color_light": (None, "transparentize($fg_color, .5)"),
        "borders_color_dark": (None, "transparentize($fg_color, .9)"),
        "borders_edge_light": (None, "rgba(255,255,255,0.8)"),
        "borders_edge_dark": (None, "lighten($bg_color, 5%)"),
        "link_color_light": (None, "darken($selected_bg_color, 10%)"),
        "link_color_dark": (None, "lighten($selected_bg_color, 20%)"),
        "link_visited_color_light": (None, "darken($selected_bg_color, 20%)"),
        "link_visited_color_dark": (None, "lighten($selected_bg_color, 10%)"),
        "warning_color_light": ("warning_bg_color_light", "$yellow_5"),
        "warning_color_dark": ("warning_bg_color_dark", "#cd9309"),
        "error_color_light": ("error_bg_color_light", "$red_3"),
        "error_color_dark": ("error_bg_color_dark", "$red_4"),
        "success_color_light": ("success_bg_color_light", "$green_4"),
        "success_color_dark": ("success_bg_color_dark", "$green_5"),
        "destructive_color": (None, "$error_color"),
        "osd_fg_color": ("window_fg_color_dark", "white"),
        "osd_bg_color": ("window_bg_color_dark", "$_dark_base_color"),
        "osd_insensitive_bg_color": (None, "transparentize(mix($osd_fg_color, opacify($osd_bg_color, 1), 10%), 0.5)"),
        "osd_insensitive_fg_color_light": (None, "mix($osd_fg_color, $osd_bg_color, 80%)"),
        "osd_insensitive_fg_color_dark": (None, "mix($osd_fg_color, $osd_bg_color, 70%)"),
        "osd_borders_color": (None, "transparentize(black, 0.3)"),
        "osd_outer_borders_color": (None, "transparentize($osd_fg_color, 0.98)"),
        "shadow_color_light": (None, "rgba(0,0,0,0.1)"),
        "shadow_color_dark": (None, "rgba(0,0,0,0.2)"),
        "card_bg_color_light": (None, "darken($bg_color, 5%)"),
        "card_bg_color_dark": (None, "lighten($bg_color, 2%)"),
        "card_outer_borders_color": (None, "transparentize($fg_color, 0.98)"),
        "bubble_bubble_color_light": (None, "darken($bg_color, 12%)"),
        "bubble_bubble_color_dark": (None, "lighten($bg_color, 10%)"),
        "system_bg_color": (None, "$base_color"),
        "insensitive_fg_color": (None, "mix($fg_color, $bg_color, 50%)"),
        "insensitive_bg_color": (None, "mix($fg_color, $base_color, 60%)"),
        "insensitive_borders_color": (None, "mix($borders_color, $base_color, 60%)"),
        "backdrop_base_color_light": (None, "darken($bg_color,1%)"),
        "backdrop_base_color_dark": (None, "lighten($bg_color,1%)"),
        "backdrop_bg_color": (None, "$bg_color"),
        "backdrop_fg_color": (None, "mix($fg_color, $backdrop_bg_color, 80%)"),
        "backdrop_insensitive_fg_color_light": (None, "darken($backdrop_bg_color,15%)"),
        "backdrop_insensitive_fg_color_dark": (None, "lighten($backdrop_bg_color,15%)"),
        "backdrop_borders_color": (None, "mix($borders_color, $bg_color, 90%)"),
        "backdrop_dark_fill": (None, "mix($backdrop_borders_color,$backdrop_bg_color, 35%)"),
        "checked_bg_color_light": (None, "darken($bg_color, 7%)"),
        "checked_bg_color_dark": (None, "lighten($bg_color, 7%)"),
        "checked_fg_color_light": (None, "darken($fg_color, 7%)"),
        "checked_fg_color_dark": (None, "lighten($fg_color, 7%)"),
        "hover_bg_color_light": (None, "darken($bg_color, 3%)"),
        "hover_bg_color_dark": (None, "lighten($bg_color, 10%)"),
        "hover_fg_color_light": (None, "darken($fg_color, 5%)"),
        "hover_fg_color_dark": (None, "lighten($fg_color, 10%)"),
        "active_bg_color_light": (None, "darken($bg_color, 5%)"),
        "active_bg_color_dark": (None, "lighten($bg_color, 12%)"),
        "active_fg_color_light": (None, "darken($fg_color, 5%)"),
        "active_fg_color_dark": (None, "lighten($fg_color, 12%)")
    }
}

custom_properties = {
    "panel_color": """#panel {
    background-color: **panel_color**;}
#panel.unlock-screen, #panel.login-screen, #panel:overview {
    background-color: transparent;}
""",
    "dash_color": """#dash .dash-background {
    background-color: **dash_color**;}
""",
    "overview_color": """#overviewGroup {
    background-color: **overview_color**;
}"""
}
