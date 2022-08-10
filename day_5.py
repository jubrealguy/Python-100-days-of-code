# *******  GETTING THE AVERAGE HEIGHT OF A GROUP OF BOYS  *******

# heights_str = input("Enter heights of every boy in the hall separated by a space:\n")
# heights = heights_str.split()

# sum_heights = 0
# num_heights = 0

# for person_height in heights:
#     sum_heights += float(person_height)

# #for num in range(0, len(height)):

# for person in heights:
#     num_heights += 1
    
# mean = sum_heights/num_heights
# print(round(mean))


# *******  GETTING THE MAXIMUM SCORE IN A LIST OF SCORES  *******

# scores_str = input("Enter the scores of the students separated by a space:\n")
# scores = scores_str.split()

# for n in range(0, len(scores)):
#     scores[n] = int(scores[n])

# max_score = 0

# for each_score in scores:
#     if each_score > max_score:
#         max_score = each_score
# print(f'The highest score in the list of scores is {max_score}')


# *******  ADDITION OF EVEN NUMBERS FROM 1 - 100  *******

# total_number = 0

# # for number in range(2, 100, 2):
# #     total_number += number
# # print(total_number)

# for number in range(2, 100):
#     if number % 2 == 0:
#         total_number += number
# print(total_number)


# *******  FIZZBUZZ CHALLENGE  *******

# for number in range(1, 100):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# ******** PASSWORD GENERATOR *********
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z']

figures = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '+']

letters_nos = int(input("Enter number of letters you want in your password\n"))
figures_nos = int(input("Enter number of figures you want in your password\n"))
symbols_nos = int(input("Enter number of symbols you want in your password\n"))

password_string = ""

for i in range (0, letters_nos):
    letter = random.choice(letters)
    password_string += letter

for i in range (0, figures_nos):
    figure = random.choice(figures)
    password_string += figure

for i in range (0, symbols_nos):
    symbol = random.choice(symbols)
    password_string += symbol       # Our final password for the easy stage but we need it shuffled and not arranged systematically

password_list = list(password_string) # Converting the password string to a list
random.shuffle(password_list)  # Reshuffling the password list

password = ""
for item in password_list:
    password += item

print(password)
