country = input()#Add a country
visits = int(input())#Number of visits
list_of_cities = eval(input())#created list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "list_of_cities": ["Paris", "Dijon","Lille"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "list_of_cities": ["Berlin", "Hamburg", "Stuttgart"]
    }

]

#Do no change the code above
print(country)
print(visits)
print(list_of_cities)

#Write the function that will allow new countries to be added to the travel log
def add_new_country(nation,visits,cities):
    travel_log.append({"country": country, "visits": visits, "list_of_cities": list_of_cities})

#Don't change the code below
add_new_country(country, visits, list_of_cities)
print(f"I've benn to {travel_log[2]['country']} {travel_log[2]['visits']}" + " times")
print(f"My favourite city was {travel_log[2]['list_of_cities'][0]}")
