from twilio.rest import Client
import requests
import smtplib
from data import TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, TWILIO_CALLER, TWILIO_RECEIVER, CSV_USER_ID, SENDER_EMAIL, SENDER_PWD

ENDPOINT = f"https://api.sheety.co/{CSV_USER_ID}/flightDeals/users"

class NotificationManager:

    def send_text(self, message: str):
        client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(body=message, from_=TWILIO_CALLER, to=TWILIO_RECEIVER)
    
        print(message.status)
    
    def send_emails(self, message):
        response = requests.get(url=ENDPOINT)
        response.raise_for_status()
        users_data = response.json()["users"]
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=SENDER_EMAIL, password=SENDER_PWD)
                
                for user in users_data:
                    connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=user['email'], msg=f"Subject:New Flight Alert!\n\n{message}")
        except smtplib.SMTPAuthenticationError:
            print("Error Found. Confirm SMTP settings and/or authentication information.")
        else:
            connection.close()
            print("\nMessage sent!\n")
        