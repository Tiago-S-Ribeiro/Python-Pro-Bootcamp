import requests
import datetime as dt
import smtplib
import time
from data import HOST_SERVER, EML, PWD, DST

MY_LAT = 38.723308
MY_LNG = -9.140687
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

def iss_is_visible(lat, lon):
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_lat = float(data_iss["iss_position"]["latitude"])
    iss_lng = float(data_iss["iss_position"]["longitude"])
    
    return (lat + 5 >= iss_lat <= lat - 5) and (lon + 5 >= iss_lng <= lon - 5)

def is_nightime():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()

    now_hour = dt.datetime.now().hour
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    return now_hour >= sunset_hour or now_hour <= sunrise_hour

def send_email(message):
    try:
        with smtplib.SMTP(HOST_SERVER) as connection:
            connection.starttls()
            connection.login(user=EML, password=PWD)
            connection.sendmail(from_addr=EML, to_addrs=DST, msg=f"Subject:ISS is within range\n\n{message}")
    except smtplib.SMTPAuthenticationError:
        print("Error Found. Confirm SMTP settings and/or authentication information.")
    else:
        print("\nMessage sent!\n")

#------------------------------------------------------------------------------------------

while True:
    time.sleep(30)
    if iss_is_visible(MY_LAT, MY_LNG) and is_nightime():
        send_email("\nLook Up! ☝🏼\n")
    else:
        print("\nISS is still not near enough.\n")