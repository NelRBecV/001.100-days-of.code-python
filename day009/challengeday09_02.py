# Nested dictionaries

# Example - 1
# travel_log = {"France": ["Paris", "Lille", "Nice", "Bordeaux"],
#               "Germany": ["Berlin","Hamburg","Frankfurt","Dortmund"]
#               }

# Example - 2
# travel_log = {"France": {"cities_visited": ["Paris", "Lille", "Nice", "Bordeaux"]},
#               "Germany": {"places_to_go": ["Berlin", "Hamburg", "Frankfurt", "Dortmund"], "money_spend": 12,
#                           "Stadiums_visited": ["Eintracht Stadium", "Borussia Park"]}
#               }

# print(travel_log["Germany"])

# Example - 3
travel_log = [
        {"country": "France",
         "cities_visited": ["Paris", "Lille", "Nice", "Bordeaux"]},
        {"country": "Germany",
         "places_to_go": ["Berlin", "Hamburg", "Frankfurt", "Dortmund"],
         "money_spend": 12,
         "Stadiums_visited":["Eintracht Stadium", "Borussia Park"]}
        ]

print(travel_log)
