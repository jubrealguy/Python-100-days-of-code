import random as rd

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "K", "Q", "J"]

computer_choice =[rd.choice(cards)]
for x in range(len(computer_choice)):
    if computer_choice[x] == "K" or computer_choice[x] == "Q" or computer_choice[x] == "J":
        computer_choice[x] = 10
    if computer_choice[x] == "A":
        computer_choice[x] = rd.choice([1, 11])

my_choice = [rd.choice(cards) for i in range(2)]
for x in range(len(my_choice)):
    if my_choice[x] == "K" or my_choice[x] == "Q" or my_choice[x] == "J":
        my_choice[x] = 10
    if my_choice[x] == "A":
        my_choice[x] = int(input("Do you want your A as 1 or 11: "))

print(computer_choice)
print(my_choice)

new_card = input("Type 'y' to get another card and 'n' to pass: ")
if new_card == 'n':
    sum1 = sum(computer_choice)
    sum2 = sum(my_choice)
    print(sum1, sum2)
elif new_card == 'y':
    computer_choice.append(rd.choice(cards))
    my_choice.append(rd.choice(cards))
    
    for x in range(len(computer_choice)):
        if computer_choice[x] == "K" or computer_choice[x] == "Q" or computer_choice[x] == "J":
            computer_choice[x] = 10
        if computer_choice[x] == "A":
            computer_choice[x] = rd.choice([1, 11])
    for x in range(len(my_choice)):
        if my_choice[x] == "K" or my_choice[x] == "Q" or my_choice[x] == "J":
            my_choice[x] = 10
        if my_choice[x] == "A":
            my_choice[x] = int(input("Do you want your A as 1 or 11: "))
    print(computer_choice)
    print(my_choice)
    sum1 = sum(computer_choice)
    sum2 = sum(my_choice)
    print(sum1, sum2)
    
else:
    print("Thank you")