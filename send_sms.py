# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC5b3dfb6450dc6c859c8a55db5e5a680b"
auth_token = "43387aea03f99110c909f27b8c6ee1bb"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+56964590925", from_="+56988949343",
                                     body="Hello there!")
