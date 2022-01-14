# Method 1
# with open("Working with CSV\weather_data.csv") as f:
#     data = f.readlines()
#     print(data)

# Method 2
# import csv
# with open("Working with CSV\weather_data.csv") as f:
#     output = csv.reader(f)
#     temperatures = []
#     for row in output:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Method 3
# import pandas as p
# data = p.read_csv("Working with CSV\weather_data.csv")
# print(data["temp"])
# print(data.temp)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())

# monday = data[data.day == "Monday"]
# print(monday)
# print(data[data.temp == data.temp.max()])
# print(monday.condition)
# print(monday["temp"]*2)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores": [76,89,56]
# }

# data = p.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

import pandas as p
data = p.read_csv("Working with CSV\Squirrel_Data.csv")
gray_squirrel = len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"]=="Black"])

data_dict = {
    "Fur color": ["Gray","Cinnamon","Black"],
    "Count": [gray_squirrel,cinnamon_squirrel,black_squirrel]
}
df = p.DataFrame(data_dict)
df.to_csv("new_data.csv")
print(df)