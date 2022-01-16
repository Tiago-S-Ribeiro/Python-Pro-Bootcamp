class FlightData:
    
    def __init__(
        self, 
        price, 
        airport_from,
        city_from, 
        airport_to, 
        city_to, 
        departure_day, 
        departure_hour,
        arrival_day,
        arrival_hour,
        comeback_day,
        comeback_hour,
        comeback_arrival_day,
        comeback_arrival_hour,
        seats_available,
        stop_overs=0,
        via_city=""
    ):
        self.price = price
        self.airport_from = airport_from
        self.city_from = city_from
        self.airport_to = airport_to
        self.city_to = city_to
        self.departure_day = departure_day
        self.departure_hour = departure_hour
        self.arrival_day = arrival_day
        self.arrival_hour = arrival_hour
        self.comeback_day = comeback_day
        self.comeback_hour = comeback_hour
        self.comeback_arrival_day = comeback_arrival_day
        self.comeback_arrival_hour = comeback_arrival_hour
        self.seats_available = seats_available
        self.stop_overs = stop_overs
        self.via_city= via_city