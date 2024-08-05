PLACEHOLDER = "[name]"

with open('./Input/Names/invited_names.txt') as names:
    name_list = names.readlines()

with open('./Input/Letters/starting_letter.txt') as letter:
    content = letter.read()
    for name in name_list:  
        stripped_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode = 'w') as file:
            file.write(new_letter)
            

































# PLACEHOLDER = "[name]"


# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()

# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)

