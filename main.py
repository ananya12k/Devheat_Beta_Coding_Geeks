from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton

# from sms import sendSMS
from screenNavigation import screen_helper

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='Menu'))
sm.add_widget(ProfileScreen(name='Profile'))


class Friends:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class SOSApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"

        return screen

SOSApp().run()