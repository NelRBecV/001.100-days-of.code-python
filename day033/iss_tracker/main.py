import requests
from datetime import datetime
import smtplib
from tkinter import *
import os
from dotenv import load_dotenv()

load_dotenv()

MY_LAT = 7.8160153271683965
MY_LONG = -72.26874225465156

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
t = Tk()
t.withdraw()
def iss_locator(data):
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longuitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 and -5 degrees of the ISS position
    if (MY_LAT + 5) > iss_latitude > (MY_LAT-5) and (MY_LONG - 5)< iss_latitude < (MY_LONG + 5):

            parameters = {
                    "lat": MY_LAT,
                    "lng": MY_LONG,
                    "formatted":0,
            }
            response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
            response.raise_for_status()
            data = response.json()
            sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
            sunset = int(data["result"]["sunset"].split("T")[1].split(":")[0])

            time_now = datetime.now()
            my_hour = time_now.hour
            if my_hour < sunrise and my_hour > sunset:
                user = os.getenv("USER_MAIL")
                pw = os.getenv("PSWD_MAIL")
                serv = "smtp.gmail.com"
                dest = "raulbvillamizar@gmail.com"
                message = f"Subject: Hey, look up!!!\n\n The ISS is right now over your head"
                with smtplib.SMTP(serv, 587) as email_conn:
                    email_conn.starttls()
                    email_conn.login(user, pw)
                    email_conn.sendmail(from_addr=user, to_addrs=dest, msg=message)
            else:
                print("It's daylight. You won't be able to see anything")
    else:
        print("Nothing in the horizont, Captain")
    t.after(60000, iss_locator, data)

if  __name__ == "__main__":
    iss_locator(data)

t.mainloop()

#If the ISS is close to my current position
#and it's currently dark
#Then send me an email to tell me to look up
#BONUS: run the code every 60 seconds
