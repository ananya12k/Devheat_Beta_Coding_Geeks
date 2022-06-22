from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager
from kivymd.uix import dialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

import random
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

from sms import sendSMS

client = pymongo.MongoClient(os.getenv("serverLink"))    
db = client['SOS']
collection = db['SOSUserCollection']

user = {}

class LoginScreen(Screen):

    def login(self, name, password):
        try:
            if collection.find_one({"name":name}) != None:
                if collection.find_one({"name":name, "password":password}) != None:
                    user = collection.find_one({"name":name, "password":password})
                    return True
                else:
                    SOSApp().PopUp("Password", "Wrong Password !!", 'Login')
                    return False
            else:
                SOSApp().PopUp("Username", "User dosn't exist.", 'Login')
                return False
        except:
            SOSApp().PopUp("Server Error", "Try after some time", 'Login')
            return False

class SignUpScreen(Screen):
    def SignUp(self, name, p, cp, email, number):
        try:
            if p == cp:
                if collection.find_one({"name":name}) == None:
                    if collection.find_one({"number":int(number)}) == None:
                        collection.insert_one({"name":name, "password":p, "number":int(number), "mail":email, "friends":[]})
                        user = collection.find_one({"name":name, "password":p})
                        return True
                    else:
                        SOSApp().PopUp("Mobile number",  "Can't register the same number twice.", 'SignUp')
                else:
                    SOSApp().PopUp("User name", "User name alredy exist", 'SignUp')
            else:
                SOSApp().PopUp("Confirm Password", "Password & Confirm Password must be same", 'SignUp')
        except:
            SOSApp().PopUp("Server issus", "Try after some time", 'SignUp')

class OTPScreen(Screen):
    otp=0
    def sendOTP(self, number):
        if collection.find_one({"number":int(number)}) != None:
            self.otp = random.randrange(1000, 9999)
            sendSMS("Your OTP is ", "+91" + number, str(self.otp) + ".")
        else:
            SOSApp().PopUp("Mobile number",  "User not found.", 'OTP')
    def verifyOTP(self, OTP, number):
        if str(self.otp) == OTP:
            user = collection.find_one({"number":int(number)})
            return True
        else:
            SOSApp().PopUp("OTP",  "Invalid OTP.", 'OTP')

class FPassScreen(Screen):
    def setPass(self, p, cp):
        if p == cp:
            collection.update_one(user, {"$set":{"password":p}})
            SOSApp().PopUp("Welcome back", "Password changed !", 'Main')
        else:
            SOSApp().PopUp("Confirm Password", "Password & Confirm Password must be same.", 'FPass')

class MainScreen(Screen):
    def sendAlert(self):
        friends = collection.find_one(user)['friends']
        for friend in friends:
            num = friend['number']
            name = collection.find_one(user)['name']
            sendSMS(name, "+91"+str(num), " is in danger.")

class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class FriendsScreen(Screen):
    pass
class MapScreen(Screen):
    pass


class Friends:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class SOSApp(MDApp):
    dialog = None

    def build(self):
        screen = Builder.load_file("screenNavigation.kv")
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Amber"
        return screen

    def PopUp(self, tilt, msg, src):
        if not self.dialog:
            self.dialog = MDDialog(
                title=tilt,
                md_bg_color=[1, 1, 0, 0.5],
                radius=[20, 20, 0, 0],
                text=msg
            )
        self.dialog.open()
        return src

SOSApp().run()