from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel

from sms import sendSMS
from screenNavigation import screen_helper

class LoginScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class FriendsScreen(Screen):
    pass
class MapScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name='Login'))
sm.add_widget(MainScreen(name='Main'))
sm.add_widget(MenuScreen(name='Menu'))
sm.add_widget(ProfileScreen(name='Profile'))
sm.add_widget(FriendsScreen(name='Friends'))
sm.add_widget(MapScreen(name='Map'))


class Friends:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class SOSApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Amber"

        return screen

SOSApp().run()