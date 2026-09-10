import smtplib

from twilio.rest import Client
from smtplib import SMTP
import os
#print(os.environ) shows all environment variables created in the O.S.

class NotificationManager:
    """Sends flight cheap offers by text message and e-mail."""
    def __init__(self):
        self.txt_message = ""
        #envionment variables created outside program
        self.DELIVER_NUMBER = os.environ['TWILIO_NUMBER_PHONE']
        self.RECEIVER_NUMBER = os.environ['TWILIO_DEST_NUMBER']
        self.CLIENT_ID = os.environ['TWILIO_APP_ID']
        self.API_KEY = os.environ['TWILIO_APP_KEY']
        self.offer = Client(self.CLIENT_ID, self.API_KEY)
        self.EMAIL_SERVER = ''
        self.EMAIL_ACCOUNT = ''
        self.EMAIL_PASSWORD = ''

    def flying_offer_sms(self, offer, place_depar, iata_dep, place_dest, iata_ret, time_depar, time_dest):
        body_text = f"Low price alert! Only \u20AC{offer} " \
                    f"to fly from {place_depar}-{iata_dep} to {place_dest}-{iata_ret}," \
                    f" from {time_depar} to {time_dest}.".encode('utf-8')
        message = self.offer.messages.create(from_=self.DELIVER_NUMBER, to=self.RECEIVER_NUMBER,
                                   body=body_text)
        print(message.status)

    def flying_offer_msg(self, offer:str, place_depar:str, iata_dep:str, place_dest:str, iata_ret:str,
                         time_depar:str, time_dest:str, route:list, email_dest:str):
        body_text = f"Subjet: Flight Offer Today!!!\n\n\nLow price alert! Only \u20AC{offer} " \
                    f"to fly from {place_depar}-{iata_dep} to {place_dest}-{iata_ret}," \
                    f" from {time_depar} to {time_dest}.".encode('utf-8')

        if len(route) > 1:
            body_text += f'\n\nFlight has {len(route)} scales over. Via {", ".join(route).replace(" , ",", ").strip()}.'.encode('utf-8')
        elif len(route) == 1:
            body_text += f'\n\nFlight has {len(route)} scale over. Via {", ".join(route).replace(" , ",", ").strip()}.'.encode('utf-8')
        else:
            body_text += f"\n\nFlight has {route} scales over.".encode('utf-8')

        with smtplib.SMTP(self.EMAIL_SERVER,587) as flight_user:
            flight_user.starttls()
            flight_user.login(user=self.EMAIL_ACCOUNT, password=self.EMAIL_PASSWORD)
            flight_user.sendmail(from_addr=self.EMAIL_ACCOUNT,to_addrs=email_dest,msg=body_text)
