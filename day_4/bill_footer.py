import random as rd

names_str = input("Provide everyone's name separated by a comma, let me find the payer\n")
names = names_str.split(", ")
last_name = len(names) - 1
r = rd.randint(0, last_name)
payer = names[r]

print(f"No much worry guyz, {payer} is footing the bill")