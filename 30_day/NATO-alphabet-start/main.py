import pandas as pd

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# # {"A": "Alfa", "B": "Bravo"}

nato = pd.read_csv('nato_phonetic_alphabet.csv')
# print(nato)

new = {row.letter: row.code for (index, row) in nato.iterrows()}
print(new)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Create your word: ").upper()
    # phonetic_code = [value for (key, value) in new.items() if key in list(word)]

    try:
        phonetic_code_ = [new[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_code_)

generate_phonetic()

