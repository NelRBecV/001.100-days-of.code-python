import token
from datetime import date, timedelta
from flight_search import FlightSearch
from openpyxl import *
import io

class FlightData:
    """Rearrange the obtained data from Amadeus querying"""
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight = FlightSearch()


    def order_data(self, d_city:str,d_date:str,r_date:str,spreadsheet:dict):
        """Shows the current destination and price flights"""
        ticket_price = ""
        cheap_offers = []
        destination = spreadsheet['iata_code']
        price = ""
        try:
            route = []
            flight_price = self.flight.get_flight_offers(ori=d_city,
                                                       dest=destination,
                                                       dep_date=d_date,
                                                       ret_date=r_date,
                                                       )

            price = flight_price['data'][0]['price']['total']
            ticket_price = f"{spreadsheet['city']}: {price}€"
            scales = len(flight_price['data'][0]['itineraries'][0]['segments'])
            if scales > 1:
                for c in range(1,scales):
                    city_route = []
                    sc = flight_price['data'][0]['itineraries'][0]['segments'][c]['departure']['iataCode']
                    city_name = self.flight.get_city_name(sc)
                    city_route.append(city_name)
            route = city_route
            cheap_offers = {'city':spreadsheet['city'], 'iata':spreadsheet['iata_code'], 'price':price}
            return cheap_offers, route
        except:
            print(f"{spreadsheet['city']}: No offers were found.")
            # ticket_price = f"{city['city']}: No offers were found."
