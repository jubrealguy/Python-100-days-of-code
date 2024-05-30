from data import MENU, resources

def process_coins():
    """ A function that process coins and returns the total amount paid"""
    print("please insert coins")
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.1
    nickels = int(input("How many nickels: ")) * 0.05
    pennies = int(input("How many penies: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total    

money = 0
resources["money"] = money

def output(coffee):
    """ Function to check if transaction was successful and subsequently make the coffee """
    if coffee == "latte" or coffee == "cappuccino":
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]

    money = MENU[coffee]["cost"]
    resources["money"] += money

    change = process_coins() - money
    change = round(change, 2)

    def check_ingredients(item):
        """ Function to check if ingredients are enough """
        if resources[item] <= 0:
            resources[item] = 0
            print(f"There is no enough {item}")

    if change >= 0 and resources["milk"] > 0 and resources["water"] > 0 and resources["coffee"] > 0:
        print(f"you have ${change} in change")
        print(f"Here is your {coffee} ☕️ Enjoy!!!")
    elif change < 0:
        print("That is not enough money. Money refunded")
    else:
        check_ingredients("milk")
        check_ingredients("water")
        check_ingredients("coffee")

should_continue = True
while should_continue:
    coffee_type = input("What coffee would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == "off":
        should_continue = False
    elif coffee_type in ["espresso", "latte", "cappuccino"]:
        output(coffee_type)
    elif coffee_type == "report":
        for key, value in resources.items():
            if key == 'money':
                print(f"{key}: ${value}")
            else:
                print(f"{key}: {value}")
    else:
        print("Not available, please ")

    # print report
    # check if resources are sufficcient
    # process coins
    # check if transaction is successful
    # Make coffee
