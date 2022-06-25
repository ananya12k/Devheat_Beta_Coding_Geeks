from gc import collect
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import pymongo
import os
import random
from dotenv import load_dotenv
from sms import sendSMS

load_dotenv()
client = pymongo.MongoClient(os.getenv("serverLink"))    
db = client['SOS']
collection = db['SOSUserCollection']

user = {}

class LoginScreen(Screen):

    def login(self, name, password):
        global user
        try:
            if collection.find_one({"name":name}) != None:
                if collection.find_one({"name":name, "password":password}) != None:
                    user = collection.find_one({"name":name, "password":password})
                    #print(user)
                    return True
                else:
                    SOSApp().PopUp("Password", "Wrong Password !!", 'Login')
                    return False
            else:
                SOSApp().PopUp("Username", "User doesn't exist.", 'Login')
                return False
        except:
            SOSApp().PopUp("Server Error", "Try after some time", 'Login')
            return False

class SignUpScreen(Screen):
    def SignUp(self, name, p, cp, email, number):
        global user
        try:
            if p == cp:
                if collection.find_one({"name":name}) == None:
                    if collection.find_one({"number":int(number)}) == None:
                        collection.insert_one({"name":name, "password":p, "number":int(number), "mail":email, 'msg':"I am in Danger","friends":[]})
                        user = collection.find_one({"name":name, "password":p})
                        return True
                    else:
                        SOSApp().PopUp("Mobile number",  "Can't register the same number twice.", 'SignUp')
                else:
                    SOSApp().PopUp("User name", "User name already exist", 'SignUp')
            else:
                SOSApp().PopUp("Confirm Password", "Password & Confirm Password must be same", 'SignUp')
        except:
            SOSApp().PopUp("Server issues", "Try after some time", 'SignUp')

class OTPScreen(Screen):
    otp=0
    def sendOTP(self, number):
        global user
        if collection.find_one({"number":int(number)}) != None:
            self.otp = random.randrange(1000, 9999)
            sendSMS("Your OTP is ", "+91" + number, str(self.otp) + ".")
        else:
            SOSApp().PopUp("Mobile number",  "User not found.", 'OTP')
    def verifyOTP(self, OTP, number):
        global user
        if str(self.otp) == OTP:
            user = collection.find_one({"number":int(number)})
            return True
        else:
            SOSApp().PopUp("OTP",  "Invalid OTP.", 'OTP')

class FPassScreen(Screen):
    def setPass(self, p, cp):
        global user
        if p == cp:
            collection.update_one(user, {"$set":{"password":p}})
            SOSApp().PopUp("Welcome back", "Password changed !", 'Main')
        else:
            SOSApp().PopUp("Confirm Password", "Password & Confirm Password must be same.", 'FPass')

class MainScreen(Screen):
    def sendAlert(self):
        global user
        friends = user['friends']
        for friend in friends:
            num = friend['number']
            name = user['name']
            try:
                sendSMS(name + " : ", "+91"+str(num), user['msg'])
            except:
                SOSApp().PopUp(friend['name'] + " is not verified", "", 'Main')        
        SOSApp().PopUp("SOS sent !!", "", 'Main')

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    def update_(self):
        global user
        self.ids.userName.text = user['name']
        self.ids.email.text = user['mail']
        self.ids.number.text = str(user['number'])

    def update(self, name, email, number):
        global user
        collection.update_one(user, {"$set":{"name":name,"number":int(number), "mail":email}})
        user = collection.find_one({'_id':user['_id']})
        return True

class FriendsScreen(Screen):
    pass

class ViewFriends(Screen):
    def buildTable(self):
        global user
        friends = collection.find_one({'name':user['name']})['friends']
        print(friends)
        table = MDDataTable(
            size_hint=(0.9, 0.6),
            use_pagination=True,
            pos_hint={'center_x':0.5, 'center_y':0.5},
            column_data= [("Name", dp(30)), ("Number", dp(30))],
            row_data= [(friend['name'], friend['number']) for friend in friends]
        )
        self.add_widget(table)

class AddFriends(Screen):
    def add_friends(self, name, number):
        global user
        try:
            oldFriends = user['friends']
            newFriends = oldFriends + [{'name': name, 'number': int(number)}]
            collection.update_one(user, {"$set":{'friends':newFriends}})
            user = collection.find_one({'_id':user['_id']})
            SOSApp().PopUp("Added Successfully", "Go Back", 'Delete Friends')
            return True
        except:
            SOSApp().PopUp("Server error.", "", 'AddFriends')
            return False

class DeleteFriends(Screen):
    def delete_friends(self, name, number):
        global user
        i = 0
        try:
            oldFriends = user['friends']
            for friend in oldFriends:
                if friend['name'] == name and friend['number'] == int(number):
                    i+=1
                    oldFriends.remove(friend)
            if i == 1:
                collection.update_one({'name': user['name']}, {"$set":{'friends':oldFriends}})
                SOSApp().PopUp("Deleted Successfully", "Go Back", 'Delete Friends')
                return True
            else:
                SOSApp().PopUp("Friend not found.", "Check the details", 'Delete Friends')
                return False
        except:
            SOSApp().PopUp("Server issues", "Try after some time", 'Friends')
            return False

class MessageScreen(Screen):
    def update_(self):
        global user
        self.ids.msg.text = user['msg']
    def update(self, msg):
        global user
        collection.update_one(user, {"$set":{'msg':msg}})
        user = collection.find_one({'_id':user['_id']})
        return True

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