# DataManager -> responsible for talking to the Google Sheets API.
# FlightSearch -> responsible for talking to the Flight Search API.
# FlightData -> responsible for structuring the flight data
# NotificationManager -> responsible for sending notifications with the deal flight details

from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from utils import format_notification

dm = DataManager()
fs = FlightSearch()
nm = NotificationManager()

sheet_data = dm.get_google_sheet_curret_data()

for data_row in sheet_data:
    if data_row["iataCode"] == "":
        data_row["iataCode"] = fs.get_iata_codes(data_row["city"])
        dm.update_iata(data_row)
    
    flight_info = fs.get_flights_data(data_row["iataCode"])
    if flight_info and (data_row["lowestPrice"] > flight_info.price):
        nm.send_text(format_notification(flight_info))
