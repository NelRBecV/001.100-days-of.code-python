from twilio.rest import Client
from dotenv import load_dotenv
import requests
import os

load_dotenv()
MY_LAT = float(os.getenv("HOME_LAT"))
MY_LONG = float(os.getenv("HOME_LONG"))
parameters = {'lat': MY_LAT,
              'lon': MY_LONG,
              'cnt': 4,
              'appid': os.getenv("APP_ID")}


def set_message_deliver_server():
    account_sid = os.getenv('ACCOUNT_SID')
    auth_token = os.getenv('AUTH_TOKEN')
    return Client(account_sid, auth_token)


def get_local_weather():
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    # Very important note: you must add 'http://' or 'https://' in case endpoint doesn't have it
    weather.raise_for_status()
    # get the http code from 'requests' API
    print(weather.status_code)
    return weather.json()['list']


def weather_forecast_notification():
    rain = False
    client = set_message_deliver_server()
    while not rain:
        for i in get_local_weather():
            if i['weather'][0]['id'] < 700:
                rain = True
                break
        if rain:
            message = client.messages.create(
                from_=os.getenv("PHONE_SENDER"),
                body='Today is gonna rain. So, Bring an ☂',
                to='+584147533905'
            )
            print(message.sid)
            print(message.status)


if __name__ == '__main__':
    weather_forecast_notification()
