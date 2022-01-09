#import os
import requests
from twilio.rest import Client
from data import CALLER_NUM, ACC_SID, APPID, AUTH_TOKEN, RECEIVER

#To use environment variables:
#export env AUTH_TOKEN=<my_key>   #no spaces
#auth_token = os.environ.get("AUTH_TOKEN")

def send_text(message):
    client = Client(ACC_SID, AUTH_TOKEN)
    message = client.messages.create(body=message, from_=CALLER_NUM, to=RECEIVER)
    print(message.status)

parameters = {
    "lat": 41.152381,
    "lon": -8.618125,
    "exclude": "current,minutely,daily",
    "appid": APPID
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

data = response.json()
codes = []
will_rain = False
weather_slice = data["hourly"][:12]     #Gets the first 12 values

for hour in weather_slice:
    code = hour["weather"][0]["id"]
    codes.append(hour["weather"][0]["id"])
    if int(code) < 700:
        will_rain = True

if will_rain:
    send_text("\n\nIt will rain today, don't forget your umbrella! ☂️")

print(codes)
