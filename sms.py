from twilio.rest import Client 
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("SID")
auth_token = os.getenv("TOKEN")
client = Client(account_sid,auth_token) 

def sendSMS(userName, toNumber, msg):
    message = client.messages.create(
                            to=toNumber,
                            from_='+18125059453',       
                            body=userName + msg
                          ) 
