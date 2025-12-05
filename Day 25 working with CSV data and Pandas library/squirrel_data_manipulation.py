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


#Instructors attempt at challenge

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251204.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")