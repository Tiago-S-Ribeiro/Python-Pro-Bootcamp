import requests
import os

SHEETY_API_URL = os.getenv('SHEETY_API_URL')

class GoogleSheetFiller:

    def __init__(self):
        pass

    def transfer_data_to_sheet(self, all_listings):
        for item in all_listings:
            listing = {
                "sheet1": {
                    "type": item["house"],
                    "region": item['region'],
                    "price": item['price'],
                    "typology": item['type'],
                    "realtor": item['realtor'],
                    "link": item['link']
                }
            }
            response_listings = requests.post(url=SHEETY_API_URL, json=listing)
            print(response_listings.text)
