import smtplib
import datetime
import dotenv
import os
from random import randint

load_dotenv()

with open("data/quotes.txt", "r") as phrases:
    quotes = phrases.readlines()

quote_day = quotes[randint(0, len(quotes)-1)]
todays_date = datetime.datetime.now()
if todays_date.weekday() == 6:
    with smtplib.SMTP("smtp.gmail.com", 587) as gmail_server:
        user = os.getenv("USER_MAIL")
        password = os.getenv("PSWD_MAIL")
        dest = "ciber_espectro@yahoo.com.mx"
        message = f"Subject: Today's Motivational Quote.\n\n {quote_day}"

        gmail_server.starttls()
        gmail_server.login(user=user, password=password)
        gmail_server.sendmail(from_addr=user, to_addrs=dest, msg=message)
        print("E-mail sent successfully")
else:
    print("Today is not Sunday")
