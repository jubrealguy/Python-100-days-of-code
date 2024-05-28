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

def check_transaction(item):
    if resources[item] < 0:
        print("There is no enough milk")
    elif resources["water"] < 0:
        print("There is no enough water")
    elif resources["coffee"] < 0:
        print("There is no enough coffee")
    

money = 0
def output(coffee):
    if coffee == "latte" or coffee == "cappuccino":
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]

    money = MENU[coffee]["cost"]

    change = input_amount() - money

    if resources["milk"] < 0:
        print("There is no enough milk")
    elif resources["water"] < 0:
        print("There is no enough water")
    elif resources["coffee"] < 0:
        print("There is no enough coffee")
    else:
        if change >= 0:
            print(f"you have {change} in change")
            print(f"Here is your {coffee}. Enjoy!!!")
        else:
            print("That is not enough money. Money refunded")

should_continue = True
while should_continue:
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
    elif coffee_type == "off":
        should_continue = False
    else:
        print("Not available. Please, choose from (espresso/latte/cappuccino): ")

    # print report
    # check if resources are sufficcient
    # process coins
    # check if transaction is successful
    # Make coffee
