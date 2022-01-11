import requests
import datetime as dt
from data import USER, TOKEN, G_ID, PXL_ENDPOINT, NEW_PIXEL_ENDPOINT, GRAPH_ENDPOINT

headers = {
    "X-USER-TOKEN": TOKEN
}

today = dt.datetime.now()

#------------------- Create a new user using POST -------------------
new_graph_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=PXL_ENDPOINT, json=new_graph_params)
print(response.text)


#---------------- Create a new Pixela graph using POST ----------------
graph_config = {
    "id": G_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "momiji"
}
response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)


#-------------------- Create a new pixel using POST --------------------
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? ")
}
response = requests.post(url=NEW_PIXEL_ENDPOINT, json=pixel_params, headers=headers)
print(response.text)


#----------------------- Update a pixel using PUT -----------------------
put = {
    "quantity": "14"
}
date = dt.datetime(year=2022, month=1, day=10)
update_endpoint = f"{NEW_PIXEL_ENDPOINT}/{date.strftime('%Y%m%d')}"
response = requests.put(url=update_endpoint, json=put, headers=headers)
print(response.text)


#---------------------------- Delete a pixel ----------------------------
response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)