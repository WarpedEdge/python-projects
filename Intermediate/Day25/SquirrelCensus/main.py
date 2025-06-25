import pandas

#TODO: #1 Get data from 2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250623.csv
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250623.csv")

#TODO: #2 Get Primary Fur Color column data
primary_color = data["Primary Fur Color"]

#TODO: #3 Parse out colors
gray = primary_color == "Gray"
cinnamon = primary_color == "Cinnamon"
black = primary_color == "Black"

#TODO: #4 sum the amount of each colors
gray_total = sum(gray)
cinnamon_total = sum(cinnamon)
black_total = sum(black)

#TODO: #5 move data to new spreadsheet

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_total, cinnamon_total, black_total]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")

### Angela's way ###

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250623.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict_angela = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict_angela)
df.to_csv("squirrel_count_angela.csv")