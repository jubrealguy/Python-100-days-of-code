from data import MENU, resources

def input_amount():
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
    if coffee == "latte" or coffee == "cappuccino":
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]

    money = MENU[coffee]["cost"]
    resources["money"] += money

    change = input_amount() - money
    change = round(change, 2)

    if change >= 0:
        print(f"you have {change} in change")
        print(f"Here is your {coffee}. Enjoy!!!")
    elif change < 0:
        print("That is not enough money. Money refunded")
    elif resources["milk"] < 0:
        print("There is no enough milk")
    elif resources["water"] < 0:
        print("There is no enough water")
    elif resources["coffee"] < 0:
        print("There is no enough coffee")

should_continue = True
while should_continue:
    coffee_type = input("What coffee would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")
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
