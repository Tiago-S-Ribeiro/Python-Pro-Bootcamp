import requests
import datetime as dt

""" r = requests.get(url="http://api.open-notify.org/iss-now.json")
print(r)

r.raise_for_status()
data = r.json()

long =  data["iss_position"]["longitude"]
lat =  data["iss_position"]["latitude"]
iss_position = (long, lat)
print(iss_position) """

#https://httpstatuses.com/

MY_LAT = 38.723308
MY_LNG = -9.140687
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()

response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()
data_iss = response_iss.json()
print(data_iss)

iss_lat = float(data_iss["iss_position"]["latitude"])
iss_lng = float(data_iss["iss_position"]["longitude"])
print((iss_lat, iss_lng))

now = dt.datetime.now()
sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(now.hour)
print(sunrise_hour)
print(sunset_hour)