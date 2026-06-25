import pandas

squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_squirrel = squirrel["Primary Fur Color"]

gray = color_squirrel[color_squirrel == "Gray"].count()
red = color_squirrel[color_squirrel == "Cinnamon"].count()
black = color_squirrel[color_squirrel == "Black"].count()

squirrel_data = {"Fur Color": ["Gray", "Red", "Black"], "Count": [gray, red, black]}
squirrel_count = pandas.DataFrame(squirrel_data).set_index("Fur Color")
squirrel_count.to_csv("Squirrel_count.csv")
