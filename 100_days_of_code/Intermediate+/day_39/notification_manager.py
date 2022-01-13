from twilio.rest import Client
from data import TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, TWILIO_CALLER, TWILIO_RECEIVER

class NotificationManager:

    def send_text(self, message: str):
        client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(body=message, from_=TWILIO_CALLER, to=TWILIO_RECEIVER)
    
        print(message.status)
