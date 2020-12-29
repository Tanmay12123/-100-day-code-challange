# with open("C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_11/weather_data.csv") as data:
#     data_file = data.readlines()
#     print(data_file)

# import csv

# with open("C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_11/weather_data.csv") as data:
#     data_file = csv.reader(data)
#     temperatures = []
#     for row in data_file:   
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures) 

# import pandas

# data = pandas.read_csv("C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_11/weather_data.csv")
# print(data["temp"])
# file = data["temp"].to_list()
# total = 0
# for num in file:
#     total +=num
# average = round(total/len(file))
# print(f"The average is {average}")

# print(data["temp"].max())

# print(data.condition)

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_farhen = (monday_temp * 1.8) + 32
# print(f"The temperature is {monday_farhen} F")

# data = pandas.read_csv("C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_11/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# squir_col = data["Primary Fur Color"]
# grey = []
# cinnamon = []
# black = []
# for color in squir_col:
#     if color == "Gray":
#         grey.append(color)
#     elif color == "Cinnamon":
#         cinnamon.append(color)
#     elif color == "Black":
#         black.append(color)

# with open("C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_11/new_data.csv",mode = "r+") as file:
#     file.write(f"grey = {len(grey)}\ncinnamon = {len(cinnamon)}\nblack = {len(black)}")
