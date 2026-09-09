import json
import requests
import os

# print(os.environ)

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.DOMAIN = 'https://api.sheety.co'
        self.API_KEY_USERNAME = os.environ['SHEETY_USER_KEY']
        self.API_KEY_SHEETDB = ""
        self.PROJECT_NAME = ""
        self.SHEET_NAME = ""
        self.endpoint_sheety = f"{self.DOMAIN}{self.API_KEY_USERNAME}f/{self.PROJECT_NAME}/{self.SHEET_NAME}"
        self.endpoint_sheetdb = "https://sheetdb.io/api/v1/"
        self.user_sheetdb = ''
        self.head = {
                     'content-type':'application/json',
                     'authorization':os.environ['SHEETY_API_BEARER']
                     }
        self.SHEETDB_HEADER = {
                                "accept":"application/json",
                                "content-type":"application/json",
                                "authorization": self.API_KEY_SHEETDB
                                }


    def show_data(self, sheetdata):
        """Shows the spreadsheet contained data"""
        sheetdb_endpoint = f'{self.endpoint_sheetdb}/{self.user_sheetdb}'
        sheetdb_head = {'authorization':self.API_KEY_SHEETDB}
        sheetdb_body = {'sheet':sheetdata}
        # sheet_data = requests.get(url=self.endpoint, headers=self.head) #Sheety API
        sheet_data = requests.get(url=sheetdb_endpoint, params=sheetdb_body, headers=sheetdb_head) #SheetDB API
        return sheet_data.json()

    def update_iata_code(self, data_set, new_value):
        """Retrives the IATA code to be changed into the spread sheet"""
        save_data = ""

        for reg in range(0,len(data_set)):
            row = data_set[reg]['city']
            endpoint = f"{self.endpoint_sheetdb}/{self.user_sheetdb}/city/{row}"
            body = {"data":{
                       "iata_code":new_value[reg]
                    }
            }
            # save_data = requests.put(url=endpoint, json=body, headers=self.head)
            save_data = requests.put(url=endpoint, json=body, headers=self.SHEETDB_HEADER)

        print(save_data.json())

    def add_new_user(self, user_fn, user_ln, user_em):
        endpoint = f"{self.endpoint_sheetdb}/{self.user_sheetdb}"
        user_data= {'data':{'First Name': user_fn,
                   'Last Name': user_ln,
                   'Email':user_em},
                    'sheet':'users'
                    }
        record = requests.post(url=endpoint, json=user_data, headers=self.SHEETDB_HEADER)
        if record.json()['created'] == 1:
            print("Success!!! Your data has been added.")


