import csv

with open('./weather-data.csv') as file:
    data = csv.reader(file)
    tenperature = []
    for row in data:
        if row[1] != 'temp':
            temp_data = int(row[1])
            tenperature.append(temp_data)
    print(tenperature)