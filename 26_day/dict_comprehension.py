# import random as rd
import pandas as pd

# names = ["Ola", "Bayo", "Titi", "Dayo", "Tosin", "Tolu"]

# student_scores = {name: rd.randint(1, 100) for name in names}
# print(student_scores)

# student_passed = {key: value + 5 for (key, value) in student_scores.items() if value > 39}
# print(student_passed)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# word_length = {word: len(word) for word in sentence.split()}
# print(word_length)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

# Looping through a dataframe
students_data = {
    "student": ["Ola", "Tosin", "Bayo"],
    "Score": [28, 71, 33]
}

student_dataframe = pd.DataFrame(students_data)
# print(student_dataframe)

# accessing columns
for (key, values) in student_dataframe.items():
    print(values)

#accessing rows
# for (index, row) in student_dataframe.iterrows():
#     print(row)