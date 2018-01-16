# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC5ce1f3a7a20af5546b71a31fe9b8f928"
auth_token = "95144415af96d1c9f7522eeda44967e5"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+56964590925", from_="+56988949343",
                                     body="Hello there!")
