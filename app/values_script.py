import os
from twilio.rest import Client

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
assistant_sid = os.environ.get('ASSISTANT_SID')
client = Client(account_sid, auth_token)

