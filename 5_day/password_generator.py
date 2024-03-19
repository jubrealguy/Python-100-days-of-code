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