print("Welcome to Python Pizza Shop, check our guide below")
print("""
S for Small Pizza
M for Medium Pizza
L for Large Pizza
Y for Yes
N for No
""")
size = input("What size of pizza do you want? S, M, L:  ").upper()
pep = input("Do you want some pepperoni? Y or N:  ").upper()
che = input("Do you want some cheese? Y or N:  ").upper()
amount = 0

def checkPep(amt):
    global amount 
    if pep == "Y":
        amount += amt

if size == "S" or size == "M" or size =="L":
    if size == "S":
        amount += 15
        checkPep(2)
    elif size == "M":
        amount += 20
        checkPep(3)
    elif size == "L":
        amount += 25
        checkPep(3)

    if che == "Y":
        amount += 1
    else:
        amount += 0

    print(f"Your bill is ${amount}")
else:
    print("Please refer to our guide and choose the correct size")