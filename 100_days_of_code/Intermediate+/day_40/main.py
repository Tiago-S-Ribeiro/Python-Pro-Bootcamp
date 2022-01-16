# DataManager -> responsible for talking to the Google Sheets API.
# FlightSearch -> responsible for talking to the Flight Search API.
# FlightData -> responsible for structuring the flight data
# NotificationManager -> responsible for sending notifications with the deal flight details

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
    
    if flight_info is None:
        continue

    if data_row["lowestPrice"] >= flight_info.price:
        msg = f"\n({flight_info.city_from.split('-')[0].strip()}) -> ({flight_info.city_to.split('-')[0].strip()})"
        print(msg)
        if flight_info.stop_overs > 0:
            msg = f"Flight from {flight_info.city_from.split('-')[0].strip()} to {flight_info.city_to.split('-')[0].strip()} has 1 stop over, via {flight_info.via_city}."
            print(msg)
        nm.send_text(format_notification(flight_info))
        nm.send_emails(format_notification(flight_info))
