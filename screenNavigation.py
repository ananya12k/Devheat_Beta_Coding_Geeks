screen_helper = """

ScreenManager:
    MenuScreen:
    ProfileScreen:


<MenuScreen>:
    name: 'Menu'
    MDLabel:
        text: "SOS"
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.95}
        theme_text_color: 'Custom'
        text_color: (0, 1, 1, 0.9)
        font_style: 'H3'
    MDRectangleFlatButton:
        text: "Call"
        pos_hint: {'center_x':0.5, 'center_y':0.85}
        font_style: 'H6'
        on_press: root.manager.current = 'Profile'
    MDRectangleFlatButton:
        text: "Profile"
        pos_hint: {'center_x':0.5, 'center_y':0.75}
        font_style: 'H6'
    MDRectangleFlatButton:
        text: "Map"
        pos_hint: {'center_x':0.5, 'center_y':0.65}
        font_style: 'H6'
            

<ProfileScreen>:
    name: 'Profile'
    MDRectangleFlatButton:
        text: "<-"
        valign: 'top'
        pos_hint: {'x':0, 'center_y':0.95}
        font_style: 'H6'
        on_press: root.manager.current = 'Menu'

"""