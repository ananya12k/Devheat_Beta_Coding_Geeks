from twilio.rest import Client 
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("SID")
auth_token = os.getenv("TOKEN")
client = Client(account_sid,auth_token) 

def sendSMS(toNumber, userName):
    message = client.messages.create(
                            to=toNumber,
                            from_='+18125059453',       
                            body=userName + " is in danger."
                          ) 

#sendSMS('+919106204370', "Devansh")