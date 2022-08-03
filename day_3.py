print("Welcome to Ozomba Island")
print("You have been chosen to find the missing prince")
print("The King is counting on you and may the gods be with you")
direction = input("You are at a T-junction, where would you go? Type 'left' or 'right': ")

if direction == "left":
    decision = input("You are at a river, type 'swim' to swim and 'wait' to wait for a boat: ")
    if decision == "wait":
        color = input("You arrived at the Island, three doors beckon, red, blue and yellow. Type the color you choose: ")
        if color == "blue":
            print("Congratulatios, you found the boy!!!!")
        elif color == "red":
            print("You are in a room full of fire, game over!!!")
        elif color == "yellow":
            print("You are in a lion's den, game over!!!")
        else:
            print("wrong choice, game over!!!")
    else:
        print("You drowned, game over!!!")
else:
    print("you ot caught up in thorns, game over!!!")


# ******** BMI and their categories *********** 

# print("Welcome, know your BMI and the category you fall in")
# weight = float(input("What is your weight in kg: "))
# height = float(input("What is your height in m: "))

# bmi = weight / height ** 2
# bmi_round = round(bmi, 1)

# if bmi_round < 18.5:
#     print(f"Your BMI is {bmi_round} amd you are Underweight.")
# elif bmi_round >= 18.5 and bmi_round < 25:
#     print("Your BMI is {} and you have a Normal weight".format(bmi_round))
# elif bmi_round >= 25 and bmi_round < 30:
#     print("Your BMI is " + bmi_round + " you are Overweight")
# elif bmi_round >= 30 and bmi_round < 35:
#     print(f"Your BMI is {bmi_round} and you are Obese")
# else:
#     print(f"Your BMI is {bmi_round} and you are Clinically obese")

# print("Welcome to the leap year checker")
# year = int(input("Enter a year: "))


# ******* Leap year checker ********

# if ((year % 4 == 0 and (year % 100 != 0)) or year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# ****** Pizza Shop *******

# print("Welcome to Python Pizza Shop, check our guide below")
# print("""
# S for Small Pizza
# M for Medium Pizza
# L for Large Pizza
# Y for Yes
# N for No
# """)
# size = input("What size of pizza do you want? S, M, L:  ")
# pep = input("Do you want some pepperoni? Y or N:  ")
# che = input("Do you want some cheese? Y or N:  ")
# amount = 0

# if size == "S" or size == "M" or size =="L":
#     if size == "S":
#         amount += 15
#     elif size == "M":
#         amount += 20
#     elif size == "L":
#         amount += 25

#     if pep == "Y":
#         amount += 2
#     else:
#      amount += 0

#     if che == "Y":
#         amount += 1
#     else:
#         amount += 0

#     print(f"Your bill is ${amount}")
# else:
#     print("Please refer to our guide and choose the correct size")


#  ******* Love Calculator ********

# print("This is your favourite Love Calculator")
# mine = input("What is your Name: ")
# yours = input("What is their name: ")
# name = (mine + yours).lower()

# true = ['t', 'r', 'u', 'e']
# firstDigit = 0
# for i in true:
#     firstDigit += name.count(i)

# love = ['l', 'o', 'v', 'e']
# secondDigit = 0
# for i in love:
#     secondDigit += name.count(i)

# score = int(str(firstDigit) + str(secondDigit))

# if score < 10 or score > 90:
#     print(f"Your score is {score}, you guys go together like coke and menthos")
# elif score >= 40 and score <= 50:
#     print(f"Your score is {score}, you guyz go together")
# else:
#     print(f"Your score is {score}")
