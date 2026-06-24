# with open("weather_data.csv") as weather:
#     temp = weather.readlines()
#     data =[]
#     for t in temp:
#         data.append(t.split())
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     day = []
#     temperature = []
#     condition = []
#     for weather in data:
#         if weather[1].isdigit():
#             temperature.append(int(weather[1]))
        # day.append(weather[0])
        # condition.append(weather[2])

# print(day)
# print(temperature)
# print(condition)

import pandas

data = pandas.read_csv("weather_data.csv")
temp_dict = data["temp"].to_dict()
temp_list = data["temp"].tolist()
print(temp_dict)
print(temp_list)
# print(data["condition"])
# print(data["day"])
# print(data["temp"])

# Get the average (media) from temp - Method 1
print(f"The average temperature is {round(sum(temp_list)/len(temp_list),1)} degrees - Method 1")

#Method 2
print(f'The average temperature is {round(data["temp"].mean(),1)} degrees - Method 2')
print(f"The maximun temperature registered is {data['temp'].max()}")

#Data in row
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

#data = data[data.day == "Monday"]
#mon_temp = data.temp[0] Method 1 - Angela's method

# mon_temp = str(data.temp[data.day == "Monday"]).split() method 2
#
# print(mon_temp)
# mon_temp_fahr = int(mon_temp[1]) * (9/5) + 32
# print(f"Moday's temperature in Fahrenheit: {mon_temp_fahr}F")
#
# data_dict = {"students": ["Amy","James","Angela"],
#              "scores": [76, 56, 65]
#              }
# data_f = pandas.DataFrame(data_dict)
# data_f.to_csv("csv_data.csv")
# print(data_f)

squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_squirrel = squirrel["Primary Fur Color"]
gray = color_squirrel[color_squirrel == "Gray"].count()
red = color_squirrel[color_squirrel == "Cinnamon"].count()
black = color_squirrel[color_squirrel == "Black"].count()
squirrel_data = {"Fur Color": ["Gray", "Red", "Black"], "Count": [gray, red, black]}
squirrel_count = pandas.DataFrame(squirrel_data)
squirrel_count.to_csv("Squirrel_count.csv")
