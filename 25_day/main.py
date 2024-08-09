import pandas as pd

data = pd.read_csv('squirrel_data.csv')
gray = data[data['Primary Fur Color'] == 'Gray']
cinnamon = data[data['Primary Fur Color'] == 'Cinnamon']
black = data[data['Primary Fur Color'] == 'Black']

fur_dict = {
    "fur color": ["gray", "cinnamon", "black"],
    "count": [gray.shape[0], cinnamon.shape[0], black.shape[0]]
}

new_data = pd.DataFrame(fur_dict)
new_data.to_csv('squirrel fur.csv')


























# # import csv

# # with open('./weather-data.csv') as file:
# #     data = csv.reader(file)
# #     tenperature = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temp_data = int(row[1])
# #             tenperature.append(temp_data)
# #     print(tenperature)

# import pandas as pd

# # data = pd.read_csv("./weather-data.csv")

# # # DataFrame - 2 dimensional
# # data_dict = data.to_dict()
# # print(data_dict)

# # # Series - 1 dimensional
# # # Getting Columns
# # temp_list = data.temp.to_list()
# # print(temp_list)

# # Getting Rows
# # print(data[data['day'] == 'Monday'])
# # max_temp = data['temp'].max()
# # print(data[data['temp'] == max_temp])

# # monday_data = data[data.day == 'Monday']
# # monday_temp = monday_data.temp
# # monday_temp_faren = (monday_temp * 1.8) + 32
# # print(monday_temp_faren) 

# # Creating a dataframe from scratch
# student_dict = {
#     "names": ["Ola", "Bayo", "Titi", "Dayo"],
#     "score": [78, 65, 87, 91]
# }

# data = pd.DataFrame(student_dict)
# print(data)
# data.to_csv('students_data.csv')