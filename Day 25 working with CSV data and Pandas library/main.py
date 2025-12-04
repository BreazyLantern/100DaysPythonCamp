"""import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
    """
import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["temp"])


data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))

#find average temp
print(data["temp"].mean())

#find max
print(data["temp"].max())


#get column
print(data["condition"])
print(data.condition)

#get row
print(data[data.day == "Monday"])

#challenge get max temp of the week
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.condition)

#get fahrenheit of monday.
F = monday.temp[0] *9/5 +32
print(F)
#(0°C × 9/5) + 32 = 32

#create data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Terry"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")