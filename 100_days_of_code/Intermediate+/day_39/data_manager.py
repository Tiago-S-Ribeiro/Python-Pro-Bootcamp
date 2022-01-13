import requests
from data import CSV_USER_ID

ENDPOINT = f"https://api.sheety.co/{CSV_USER_ID}/flightDeals/prices"

class DataManager:

    def get_google_sheet_curret_data(self):
        response = requests.get(url=ENDPOINT)
        response.raise_for_status()
        return response.json()["prices"]    
    
    def update_iata(self, data_row):
        updated_info = {
            'price': data_row
        }
        response = requests.put(url=f"{ENDPOINT}/{data_row['id']}", json=updated_info)
        response.raise_for_status()