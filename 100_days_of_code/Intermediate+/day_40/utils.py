def convert_date(date):
    date_details = date.split("-")
    return f"{date_details[2]}/{date_details[1]}/{date_details[0]}"

def format_notification(flight_data: object) -> str:
    if flight_data.stop_overs == 0:
        return f"New flight available for only {flight_data.price}€!\nFly from {flight_data.city_from}({flight_data.airport_from}) to {flight_data.city_to}({flight_data.airport_to}).\n From {flight_data.departure_day} to {flight_data.comeback_day}."
    else:
        return f"New flight available for only {flight_data.price}€!\nFly from {flight_data.city_from}({flight_data.airport_from}) to {flight_data.city_to}({flight_data.airport_to}) via {flight_data.via_city}.\n From {flight_data.departure_day} to {flight_data.comeback_day}."