#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import date, datetime, timedelta
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

cities = FlightSearch()
flights = DataManager()
sheet_data = flights.show_data('prices')
flying_return = ""
flying_depart = ""
end_system = False
city_depart = ""
depart = ""
print("Welcome to Zorca Flight Finder\nwhere flying over there is possible")
while not end_system:
    option = input("Please Choose one of these options:\n1.- Insert customers."
                    "\n2.- Search for Flights.\n3.- Exit.\nYour Option: ")
    if option.isdigit(): option = int(option)
    if option == 3:
        end_system = True
        print("Program Ended")
    elif option ==2:
        city_depart = input("Where do you want to take your flight?: ").title()
        try:
            depart = cities.get_city_code(city_depart)
        except:
            print("Not a valid input")
        else:
            try:
                dep = datetime.strptime(input("Specify your depart date (e.g. 1999-01-01): "),"%Y-%m-%d")
                time_to_return = int(input("How much time will you spend in there? (1 - 6 months): ")) * 30
                if time_to_return < 30 or time_to_return > 180:
                    raise ValidDate
                else:
                    ret = dep + timedelta(days=time_to_return)
                    flying_depart = datetime.strftime(dep,"%Y-%m-%d")
                    flying_return=datetime.strftime(ret,"%Y-%m-%d")

            except ValueError:
                print("Error: Insert a valid Date")
            except Exception as ValidDate:
                print("Error: Your selection is out of range")
            else:
                data = FlightData()
                offer_texting = NotificationManager()
                for dest in sheet_data:
                    cheap_tickets = data.order_data(d_city=depart, d_date=flying_depart,
                                                r_date=flying_return,spreadsheet=dest)

                    if not cheap_tickets == None:
                        for row in sheet_data:
                            city = cheap_tickets[0]['city']
                            ticket_price = float(cheap_tickets[0]['price'])
                            local_price = float("".join(row['low prices']).replace(".","").replace(",","."))
                            if city == row['city'] and ticket_price < local_price:
                                offer_texting.flying_offer_sms(offer=ticket_price,
                                                               place_depar=city_depart,
                                                               iata_dep=depart,
                                                               place_dest= row['city'],
                                                               iata_ret= row['iata_code'],
                                                               time_depar= flying_depart,
                                                               time_dest= flying_return,
                                                               )
                                email = flights.show_data('users')
                                for i in email:
                                    offer_texting.flying_offer_msg(offer=ticket_price,
                                                                   place_depar=city_depart,
                                                                   iata_dep=depart,
                                                                   place_dest= row['city'],
                                                                   iata_ret= row['iata_code'],
                                                                   time_depar= flying_depart,
                                                                   time_dest= flying_return,
                                                                   route=cheap_tickets[1],
                                                                   email_dest=i['Email']
                                                                   )

    elif option==1:
        fn = input("What's your first name?: ").title()
        if fn != "":
            ln = input("What's your last name?: ").title()
            if ln != "":
                mail = input("Introduce your E-mail address: ")
                if mail != "" and "@" in mail:
                    if mail == input("Type your email again: "):
                        flights.add_new_user(user_fn=fn,user_ln=ln,user_em=mail)
                    else:
                        print("ATTENTION: E-mail addresses mismatch")
                else:
                    print("ATTENTION: A valid E-mail is missing!!!")
            else:
                print("ATTENTION: A last name is required.")
        else:
            print("ATTENTION: A first name is required.")
    else:
        print("ATTENTION: Insert a valid option.")
    if input("Continue? Y/N: ").upper()[0] == "Y":
        end_system = False
    else:
        end_system = True
# cities_code = []

# print(cities_code)
# flights.update_iata_code(sheet_data, cities_code)
# pprint(sheet_data)