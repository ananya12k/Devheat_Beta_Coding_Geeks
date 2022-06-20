from twilio.rest import Client 
 
account_sid = 'AC069488126e2c0e0f9e065ce24d2f094b' 
auth_token = 'f276f0be9438a2962dcc5843687bb7bf' 
client = Client(account_sid, auth_token) 

def sendSMS(toNumber, userName):
    message = client.messages.create(
                            to=toNumber,
                            from_='+18125059453',       
                            body=userName + " is in danger."
                          ) 