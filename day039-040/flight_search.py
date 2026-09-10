import requests
import os
from openpyxl import *

class FlightSearch:
    #     #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.IATA_DATA = load_workbook("iata_airport_codes.xlsx")
        self.IATA_SHEET_LIST = self.IATA_DATA['Hoja1']
        self.HTTP_AMADEUS = 'https://test.api.amadeus.com/'
        self.ENDPOINT_AUTH_AMADEUS = 'v1/security/oauth2/token'
        self.ENDPOINT_FLIGHT_AMADEUS = 'v1/shopping/flight-destinations'
        self.ENDPOINT_CITY_AMADEUS = 'v1/reference-data/locations/cities'
        self.ENDPOINT_OFFER_AMADEUS = 'v2/shopping/flight-offers'
        self.API_KEY_AM = os.environ['AMADEUS_API_KEY']
        self.API_SECRET_AM = os.environ['AMADEUS_SECRET_API']
        self.header_auth = {'content-type':'application/x-www-form-urlencoded'}
        self.body_auth={"grant_type": "client_credentials",
                        "client_id": self.API_KEY_AM,
                        "client_secret": self.API_SECRET_AM
                  }

    def get_token(self):
        """Gives a key access to Amadeus API's"""
        endpoint = self.HTTP_AMADEUS + self.ENDPOINT_AUTH_AMADEUS
        self.TOKEN_AMADEUS = requests.post(url=endpoint, data=self.body_auth, headers=self.header_auth)
        return self.TOKEN_AMADEUS.json()['access_token']

    def get_city_code(self, city_name:str):
        header = {"authorization": f"Bearer {self.get_token()}"}
        """Returns the IATA code of the given city name"""
        endpoint = self.HTTP_AMADEUS + self.ENDPOINT_CITY_AMADEUS
        query_body = {"keyword":city_name,
                      "max":1}
        city_code = requests.get(url=endpoint, params=query_body, headers=header)
        return city_code.json()['data'][0]['iataCode']

    def get_city_name(self, iata: str):
        """Returns the exact name of a city by its IATA code"""
        for i in range(2, self.IATA_SHEET_LIST.max_row + 1):
            if iata == self.IATA_SHEET_LIST[f'C{i}'].value:
                full_name = self.IATA_SHEET_LIST[f'A{i}'].value.split(",")[0].split("-")[0].split("/")[0]
                return full_name

    def get_flight_offers(self, ori:str,
                          dest:str, dep_date:str,
                          ret_date:str, people_on_flight=1,
                          no_scale='false', max_res = 1):
        """Returns a list of prices from the user's departure/arrival selected location"""
        header = {"authorization": f"Bearer {self.get_token()}"}
        endpoint = f"{self.HTTP_AMADEUS}{self.ENDPOINT_OFFER_AMADEUS}"
        fo_body = {'originLocationCode': ori,
                 'destinationLocationCode': dest,
                 'departureDate':dep_date,
                 'returnDate':ret_date,
                 'adults':people_on_flight,
                 'nonStop':no_scale,
                 'max':max_res}
        flight_offers = requests.get(url=endpoint, params=fo_body, headers=header)
        return flight_offers.json()
