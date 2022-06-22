from kivymd.app import MDApp

from kivy.core.window import Window
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
class ImageButton(ButtonBehavior, Image):
    pass
class LabelButton(ButtonBehavior, Label):
    pass
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition

Window.size = (375, 750)

import os
from kivy.utils import platform
from profilephotomanager import ProfilePhotoManager

class HomeScreen(Screen):
    pass
class ProfilePhotoScreen(Screen):
    pass
class MainApp(MDApp):


    def on_start(self):
        # https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        # Profile photo manager
        self.profile_photo_grid = self.root.ids.profilephoto_screen.ids.profilephotogrid
        self.profile_photo_manager = ProfilePhotoManager()
        self.profile_photo_manager_screen = self.profile_photo_manager.run()
        self.profile_photo_grid.add_widget(self.profile_photo_manager_screen)

        def change_screen(self, screen_name, direction='forward', mode=""):
            # Get the screen manager from the kv file.
            screen_manager = self.root.ids.screen_manager

            if direction == "None":
                screen_manager.current = screen_name
                return

            screen_manager.current = screen_name

        def change_profile_source(self, path):
            self.root.ids.profile.source = "C:" + path  # For computer
            # self.root.ids.profile.source = path # For mobile phone
            self.root.ids.nav_drawer.toggle_nav_drawer()
            with open("profile_source.txt", "w") as f:
                # f.write(path) # For mobile phone
                f.write("C:" + path)  # For computer

        if os.path.isfile("profile_source.txt"):
            with open("profile_source.txt", "r") as f:
                some_path = f.read()
                if len(some_path) > 0:
                    img_source_path = some_path
                else:
                    img_source_path = "empty.jpg"
        else:
            img_source_path = "empty.jpg"



       if screen_name == "profilephoto_screen":
            print("Screen name is ", screen_name)
            if platform == 'android':
                #from android.permissions import request_permissions, Permission
                #request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
                if os.path.isfile("profile_source.txt"):
                    with open("profile_source.txt", "r") as f:
                        some_path = f.read()
                        if len(some_path) > 0:
                            img_source_path = some_path
                        else:
                            img_source_path = "empty.jpg"
                else:
                    img_source_path = "empty.jpg"

MainApp().run()