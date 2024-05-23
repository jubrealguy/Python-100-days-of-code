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

resources["money"] = 0

coffee_type = input("What coffee would you like? (espresso/latte/cappuccino): ").lower()
if coffee_type == "report":
    print(resources)
elif coffee_type == "espresso":
    print("please insert coins")
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.1
    nickels = int(input("How many nickels: ")) * 0.05
    pennies = int(input("How many penies: ")) * 0.01
    amount = quarters + dimes + nickels + pennies
    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    print(amount)