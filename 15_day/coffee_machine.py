MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def input_amount():
    print("please insert coins")
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.1
    nickels = int(input("How many nickels: ")) * 0.05
    pennies = int(input("How many penies: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total

def check_transaction(coffee):
    if coffee == "latte" or coffee == "cappuccino":
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    print(resources)

money = 0
def output(coffee):
    money = MENU[coffee]["cost"]
    change = input_amount() - money
    if change >= 0:
        print(f"you have {change} in change")
        check_transaction(coffee)
        print(f"Money: {money}")
    else:
        print("you do not have enough money")
        print(f"Money: {money}")

coffee_type = input("What coffee would you like? (espresso/latte/cappuccino): ").lower()
if coffee_type == "report":
    print(resources)
    print(money)
elif coffee_type == "espresso":
    output("espresso")
elif coffee_type == "latte":
    output("latte")
elif coffee_type == "cappuccino":
    output("cappuccino")

    # print report
    # check if resources are sufficcient
    # process coins
    # check if transaction is successful
    # Make coffee
