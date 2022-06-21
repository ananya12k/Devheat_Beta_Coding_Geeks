import email
import pyrebase
import time
from rsa import sign

firebaseConfig={'apiKey': "AIzaSyB_fx_D6dj_MqOTSAWJooCkCzCH1w_cmA8",
  'authDomain': "sos-authentication.firebaseapp.com",
  'projectId': "sos-authentication",
  'storageBucket': "sos-authentication.appspot.com",
  'messagingSenderId': "486081670072",
  'appId': "1:486081670072:web:aa6f737d98499827dd7d4d",
  'measurementId': "G-Q5XHM6RNYY",
  'databaseURL':""}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def login():
  print("Log in .....")
  try:
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    login = auth.sign_in_with_email_and_password(email,password)
    print('Successfully created logged in!')
  except:
    print("Invalid password!")

def signup():
  print("Signing in .....")
  email=input("Enter your email: ")
  password=input("Enter your password: ")
  try:
      user=auth.create_user_with_email_and_password(email, password)
      auth.send_email_verification(user['idToken'])
      print('''Successfully created account!!!
Kindly check your email for a verification email ''')
      ask=input("Do you want to login?[y/n]")
      if ask=='y':
            login()
  except:
    print("Email already exists!!\nTry using another email ID")

ans=input("Are you a new user?[y/n]")
if ans=='y':
  signup()
elif ans=='n':
  login()