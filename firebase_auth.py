import email
from itertools import count
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
  n=0
  try:
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    login = auth.sign_in_with_email_and_password(email,password)
    print('Successfully created logged in!')
  except:
    n=n+1
    print("Invalid password!")
  if n==1:
    input("Forgot password?[y/n] ")
    if 'y':
      auth.send_password_reset_email(email)
      print("Password reset email has been sent to you kindly check it")
      print("If you have not received email try again after 30 seconds")
  t=30
  countdown(int(t))
      
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    count=input("Not receieved mail?[y/n] ")
    if ans=='y':
      print("Resend link")
      auth.send_password_reset_email(email)
    print("Mail has been sent again\nLogin with new password")
    login()   

def signup():
  print("Signing in .....")
  email=input("Enter your email: ")
  password=input("Enter your password: ")
  try:
      user=auth.create_user_with_email_and_password(email, password)
      auth.send_email_verification(user['idToken'])
      print('''Successfully created account!!!
Kindly check your email for a verification email ''')
      ask=input("Do you want to login?[y/n] ")
      if ask=='y':
            login()
  except:
    print("Email already exists!!\nTry using another email ID")

ans=input("Are you a new user?[y/n] ")
if ans=='y':
  signup()
elif ans=='n':
  login()