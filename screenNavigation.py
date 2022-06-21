screen_helper="""
ScreenManager:
    LoginScreen:
    MainScreen:
    MenuScreen:
    ProfileScreen:
    FriendsScreen:
    MapScreen:

<LoginScreen>:
    name: 'Login'
    MDCard:
        size_hint: 0.8, 0.7
        mode: 'fill'
        fill_color: 0.3, 0.3, 0.3, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        padding: 25
        spacing: 25
    MDLabel:
        text: "Login to SOS"
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.8}
        theme_text_color: 'Custom'
        text_color: (0.3, 0.3, 0.1, 0.8)
        font_style: 'H4'
    MDTextField:
        id : userName
        hint_text: "Username"
        required: 'True'
        mode: 'fill'
        fill_color: 0, 0, 0, 0.3
        size_hint: 0.7, None
        height: "30dp"
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x':0.5,'center_y':0.5}
    MDTextField:
        id : userPass
        hint_text: "Password"
        required: 'True'
        mode: 'fill'
        fill_color: 0, 0, 0, 0.3
        max_text_length: 6
        size_hint: 0.7, None
        height: "30dp"
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x':0.5,'center_y':0.3}
    MDRoundFlatButton:
        text: "Login"
        font_style:'H6'
        pos_hint:{'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'Main'




<MainScreen>:
    name: "Main"
    MDFillRoundFlatButton:
        text: "SOS"
        font_style:'H2'
        pos_hint:{'center_x':0.5,'center_y':0.5}
    MDRoundFlatButton:
        text: "Menu"
        font_style:'H6'
        pos_hint:{'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'Menu'

<MenuScreen>:
    name: 'Menu'
    MDLabel:
        text: "SOS"
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.95}
        theme_text_color: 'Custom'
        text_color: (0.3, 0.3, 0.1, 0.9)
        font_style: 'H3'
    MDRectangleFlatButton:
        text: "Profile"
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        font_style: 'H6'
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'Profile'
    MDRectangleFlatButton:
        text: "Friends"
        pos_hint: {'center_x':0.5, 'center_y':0.45}
        font_style: 'H6'
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'Friends'
    MDRectangleFlatButton:
        text: "Map"
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        font_style: 'H6'
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'Map'
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.5, 'center_y':0.15}
        font_style: 'H6'
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = 'Main'
            

<ProfileScreen>:
    name: 'Profile'
    MDRectangleFlatButton:
        text: "<-"
        valign: 'top'
        pos_hint: {'x':0, 'center_y':0.95}
        font_style: 'H6'
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = 'Menu'
<FriendsScreen>:
    name: 'Friends'
    MDRectangleFlatButton:
        text: "<-"
        valign: 'top'
        pos_hint: {'x':0, 'center_y':0.95}
        font_style: 'H6'
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = 'Menu'
<MapScreen>:
    name: 'Map'
    MDRectangleFlatButton:
        text: "<-"
        valign: 'top'
        pos_hint: {'x':0, 'center_y':0.95}
        font_style: 'H6'
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = 'Menu'
"""