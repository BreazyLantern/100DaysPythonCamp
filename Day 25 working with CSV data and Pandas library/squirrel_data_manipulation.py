import pandas

#challenge get the count of all 3 color variants of squirrels in the cvs data
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251204.csv")

squirrel_color = squirrel_data["Primary Fur Color"].to_list()
colors = ["Gray", "Cinnamon", "Black"]

color_count_list = []
for color in colors:
    color_count_list.append(squirrel_color.count(color))

squirrel_fur_color_dict = {
    "Fur Color": colors,
    "Count" : color_count_list
}

print(squirrel_fur_color_dict)