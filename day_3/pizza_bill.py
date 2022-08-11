print("Welcome to Python Pizza Shop, check our guide below")
print("""
S for Small Pizza
M for Medium Pizza
L for Large Pizza
Y for Yes
N for No
""")
size = input("What size of pizza do you want? S, M, L:  ")
pep = input("Do you want some pepperoni? Y or N:  ")
che = input("Do you want some cheese? Y or N:  ")
amount = 0

if size == "S" or size == "M" or size =="L":
    if size == "S":
        amount += 15
    elif size == "M":
        amount += 20
    elif size == "L":
        amount += 25

    if pep == "Y":
        amount += 2
    else:
     amount += 0

    if che == "Y":
        amount += 1
    else:
        amount += 0

    print(f"Your bill is ${amount}")
else:
    print("Please refer to our guide and choose the correct size")