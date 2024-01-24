print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
friends = input("How many people to split the bill? ")
bill_percent = input("What percentage bill will you like to give? 10, 12, or 15? ")

bill_tip = int(bill_percent) * float(bill) / 100
bill_total = bill_tip + float(bill)
bill_per_friend = round((bill_total / int(friends)), 2)
print(f"Each person should pay: ${bill_per_friend}")