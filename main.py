from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from sms import sendSMS
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")    
db = client['Test']
collection = db['TestCollection']


class LoginScreen(Screen):
    def login(self, name, password):
        one = collection.find_one({'name':name, 'password':password})
        if(one != None):
            return True
        else:
            return False

class SignUpScreen(Screen):
    def SignUp(self, name, p, cp, email, number):
        if p == cp:
            if collection.find_one({'name':name}) == None:
                collection.insert_one({'name':name, 'password':p, 'number':int(number), 'mail':email})
                return True
        else:
            return False

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
sm.add_widget(SignUpScreen(name='SignUp'))
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
        screen = Builder.load_file("screenNavigation.kv")
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Amber"

        return screen

SOSApp().run()