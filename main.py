import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# average = sum(temp_list)/len(temp_list)
# print(average)
#
# mean = data["temp"].mean()
# print(mean)
#
# maximum = data["temp"].max()
# print(maximum)
#
# # Get data in a columns
# print(data["condition"])
# print(data.condition)

# Get data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
