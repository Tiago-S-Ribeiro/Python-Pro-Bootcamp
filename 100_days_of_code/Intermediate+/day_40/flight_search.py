import requests
import datetime
from data import KIWI_API_KEY, KIWI_ENDPOINT
from flight_data import FlightData
from utils import convert_date
from pprint import pprint

headers = { "apikey": KIWI_API_KEY }
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
six_months = tomorrow + datetime.timedelta(days=30*6)

class FlightSearch:

    def get_iata_codes(self, city_name):
        data = {
            "term": city_name,
            "location_types": "city"
        }
        
        response = requests.get(url=f"{KIWI_ENDPOINT}/locations/query", params=data, headers=headers)
        response.raise_for_status()
        response_data = response.json()["locations"]

        return response_data[0]["code"]
    
    def get_flights_data(self, airport_code):
        data = {
            "fly_from": "OPO",
            "fly_to": airport_code,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "flight_type": "round",
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 14,
            "curr": "EUR",
            "max_stopovers": 0,
            "one_for_city": 1,
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}/v2/search", headers=headers, params=data)
        response.raise_for_status()

        try:
            flight_info = response.json()["data"][0]
        except IndexError:
            data["max_stopovers"] = 1
            response = requests.get(url=f"{KIWI_ENDPOINT}/v2/search", headers=headers, params=data)
            response.raise_for_status()
            try:
                flight_info = response.json()["data"][0]
            except IndexError:
                print(f"\nNo flights available from OPO to {airport_code}.")
                return None
            else:
                fd = FlightData(
                    price=flight_info["price"],
                    airport_from=flight_info["flyFrom"],
                    city_from=f"{flight_info['cityFrom']} - {flight_info['countryFrom']['name']}",
                    airport_to=flight_info["flyTo"],
                    city_to=f"{flight_info['cityTo']} - {flight_info['countryTo']['name']}",
                    departure_day=convert_date(flight_info["local_departure"].split("T")[0]),
                    departure_hour=flight_info["local_departure"].split("T")[1].split(".")[0][:5],
                    arrival_day=convert_date(flight_info["local_arrival"].split("T")[0]),
                    arrival_hour=flight_info["local_arrival"].split("T")[1].split(".")[0][:5],
                    comeback_day=convert_date(flight_info["route"][2]["local_departure"].split("T")[0]),
                    comeback_hour=flight_info["route"][2]["local_departure"].split("T")[1].split(".")[0][:5],
                    comeback_arrival_day=convert_date(flight_info["route"][2]["local_arrival"].split("T")[0]),
                    comeback_arrival_hour=flight_info["route"][2]["local_arrival"].split("T")[1].split(".")[0][:5],
                    seats_available=flight_info["availability"]["seats"],
                    stop_overs=1,
                    via_city=flight_info['route'][0]['cityTo']
                )
                return fd
        else:
            fd = FlightData(
                price=flight_info["price"],
                airport_from=flight_info["flyFrom"],
                city_from=f"{flight_info['cityFrom']} - {flight_info['countryFrom']['name']}",
                airport_to=flight_info["flyTo"],
                city_to=f"{flight_info['cityTo']} - {flight_info['countryTo']['name']}",
                departure_day=convert_date(flight_info["local_departure"].split("T")[0]),
                departure_hour=flight_info["local_departure"].split("T")[1].split(".")[0][:5],
                arrival_day=convert_date(flight_info["local_arrival"].split("T")[0]),
                arrival_hour=flight_info["local_arrival"].split("T")[1].split(".")[0][:5],
                comeback_day=convert_date(flight_info["route"][1]["local_departure"].split("T")[0]),
                comeback_hour=flight_info["route"][1]["local_departure"].split("T")[1].split(".")[0][:5],
                comeback_arrival_day=convert_date(flight_info["route"][1]["local_arrival"].split("T")[0]),
                comeback_arrival_hour=flight_info["route"][1]["local_arrival"].split("T")[1].split(".")[0][:5],
                seats_available=flight_info["availability"]["seats"]
            )
            return fd
