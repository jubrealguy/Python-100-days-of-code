import random as rd
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "K", "Q", "J"]

def winner():
    sum1 = sum(computer_choice)
    sum2 = sum(my_choice)
    if sum1 > sum2 or sum2 > 21:
        print(f"Computer has {sum1}\nYou have {sum2}\nComputer wins")
    elif sum1 == sum2:
        print("It's a draw")
    else:
        print(f"Computer has {sum1}\nYou have {sum2}\nYow win!!!")

def replace_with_10(card_arr):
    for x in range(len(card_arr)):
        if card_arr[x] == "K" or card_arr[x] == "Q" or card_arr[x] == "J":
            card_arr[x] = 10

def choice():
    replace_with_10(my_choice)
    for x in range(len(my_choice)):
        if my_choice[x] == "A":
            my_choice[x] = int(input("You picked an 'A' Do you want to replace it with 1 or 11: "))

def computer():
    computer_choice.append(rd.choice(cards))
    replace_with_10(computer_choice)
    print(f"Computer cards: {computer_choice}")
    print(f"My cards: {my_choice}")
    for x in range(len(computer_choice)):
        if computer_choice[x] == "A":
            computer_choice[x] = rd.choice([1, 11])

computer_choice =[rd.choice(cards)]
replace_with_10(computer_choice)
for x in range(len(computer_choice)):
    if computer_choice[x] == "A":
        computer_choice[x] = rd.choice([1, 11])

my_choice = [rd.choice(cards) for i in range(2)]
choice()

print(computer_choice)
print(my_choice)

new_card = input("Type 'y' to get another card and 'n' to pass: ")

if new_card == 'n':
    computer()
    winner()
elif new_card == 'y':
    my_choice.append(rd.choice(cards))
    choice()
    computer()
    winner()
    
else:
    print("Thank you")