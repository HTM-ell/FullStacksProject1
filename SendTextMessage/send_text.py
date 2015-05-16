from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC649691909b6ad3044c056008207dcc29"
auth_token  = "34ac6f9f4e3333bd878cd7f783e1293b"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="My name is Elliott Foster!",
    to="+18328005842",    # Replace with your phone number
    from_="+12816773601") # Replace with your Twilio number
print message.sid
