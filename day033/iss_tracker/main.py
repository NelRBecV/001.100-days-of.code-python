import time
import requests
from datetime import datetime
import smtplib
import os

# To locally run this script, you must uncomment this lines bellow and add your own environment variables
# from dotenv import load_dotenv
#
# load_dotenv()

MY_LAT = float(os.getenv("HOME_LAT"))
MY_LONG = float(os.getenv("HOME_LONG"))


def get_iss_location() -> tuple:
    """Returns a float numbers pair indicating International Space Station (ISS) current position."""
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude


def get_local_daylight(parameters: dict) -> tuple:
    """Returns sunrise/sunset exact time from your given coordinates."""
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 3
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 3
    return sunrise, sunset


def iss_locator():
    """Delivers an email when ISS is overhead the given position."""
    iss_latitude, iss_longitude = get_iss_location()
    # Your position is within +5 and -5 degrees of the ISS position
    if (MY_LAT + 5) > iss_latitude > (MY_LAT - 5) and (MY_LONG - 5) < iss_longitude < (MY_LONG + 5):
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }
        sunrise, sunset = get_local_daylight(parameters)
        my_hour = datetime.now().hour
        if sunrise > my_hour or sunset < my_hour:
            user = os.getenv("USER_MAIL")
            pw = os.getenv("PSWD_MAIL")
            serv = os.getenv("SERV_MAIL")
            port = int(os.getenv("PORT_MAIL"))
            dest = "raulbvillamizar@gmail.com"
            message = f"Subject: Hey, look up!!!\n\n The ISS is right now over your head."
            with smtplib.SMTP(serv, port) as email_conn:
                email_conn.starttls()
                email_conn.login(user, pw)
                email_conn.sendmail(from_addr=user, to_addrs=dest, msg=message)
        else:
            print("It's daylight. You won't be able to see anything.")
    time.sleep(10)


if __name__ == "__main__":
    iss_locator()

# If the ISS is close to my current position,
# and it's currently dark
# Then email me telling to look up
# BONUS: run the code every 60 seconds
