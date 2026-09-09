import datetime
import time

import requests
from datetime import *
#nutrionix API data
WORKOUT_API_ID = ''
WORKOUT_API_KEY = ''
NUTRITIONIX_EP = "https://trackapi.nutritionix.com"
NATURAL_NUTRIENTS = "/v2/natural/nutrients" #POST
INSTANT_ENDPOINT = "/v2/search/instant" #GET
SEARCH_ITEM = "/v2/search/item" #GET
EXERCISES = "/v2/natural/exercise" #POST
#nuritionix data fields
#name: exercise's name
#duration_min: time used to perform the exercise
#nf_calories: calories burned after doing the exercise
header_params = {'x-app-id':WORKOUT_API_ID,
                'x-app-key':WORKOUT_API_KEY}
nutri_params = {'query':input("Tell me which exercises you did: ")}

nutri_guide = requests.post(url=f"{NUTRITIONIX_EP}{EXERCISES}",
                           json=nutri_params,
                           headers=header_params)
nutri_guide.raise_for_status()
workout_data = nutri_guide.json()
# print(workout_data)


SHEETY_DOMAIN = 'https://api.sheety.co'
SHEETS_APIKEY_USERNAME = ''
PROJECT_NAME = ''
SHEET_NAME = ''
endpoint = f"{SHEETY_DOMAIN}/{SHEETS_APIKEY_USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
head ={'content-type':'application/json',
       'authorization':'Bearer {replace text inside here with your token}'}
for i in workout_data['exercises']:
    FORMAT_DATE = "%d/%m/%Y"
    workout_date = datetime.now().strftime(FORMAT_DATE)
    FORMAT_TIME = '%H:%M:%S'#To adapt time to local format, use '%X'. It means what excel sheet does with time
    workout_time = datetime.now().strftime(FORMAT_TIME)
    row = '1'
    # endpoint += f"/{row}"
    print(endpoint)
    workout_data = {
                    SHEET_NAME[0:len(SHEET_NAME)-1]:{
                                'date':workout_date,
                                'time':workout_time,
                                'exercise':f"{i['name']}".title(),
                                'duration':i['duration_min'],
                                'calories':i['nf_calories']
                        }
    }
    excel_sheet = requests.post(url=endpoint, json=workout_data, headers=head)
    #To update rows is the same but using "PUT" instead "POST"

endpoint += f"/{input('Which record ho you wanna see?: ')}"
excel_sheet = requests.get(url=endpoint, headers=head)
#It's the same to delete without using "GET" but "DELETE" instead
print(excel_sheet.json())
