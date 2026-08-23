import pandas

data = pandas.read_csv("weather_data.csv")
temp_dict = data["temp"].to_dict()
temp_list = data["temp"].tolist()
print(temp_dict)
print(temp_list)

# Get the average (media) from temp - Method 1
print(f"The average temperature is {round(sum(temp_list)/len(temp_list),1)} degrees - Method 1")

# Method 2
print(f'The average temperature is {round(data["temp"].mean(),1)} degrees - Method 2')
print(f"The maximum temperature registered is {data['temp'].max()}")

# Data in row
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

data = data[data.day == "Monday"]
mon_temp = data.temp[0]  # Method 1 - Angela's method

mon_temp_2 = str(data.temp[data.day == "Monday"]).split()  # method 2

print(mon_temp)
print(mon_temp_2)
mon_temp_fahr = int(mon_temp[1]) * (9/5) + 32
print(f"Monday's temperature in Fahrenheit: {mon_temp_fahr}F")

data_dict = {"students": ["Amy", "James", "Angela"],
             "scores": [76, 56, 65]
             }
data_f = pandas.DataFrame(data_dict)
data_f.to_csv("csv_data.csv")
print(data_f)
