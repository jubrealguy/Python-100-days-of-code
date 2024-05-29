import random as rd
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J"]

def winner():
    sum_computer = sum(computer_choice)
    sum_player = sum(my_choice)
    
    if sum_computer > 21 and sum_player > 21:
        print(f"Computer has {sum_computer}\nYou have {sum_player}\nBoth are over 21. It's a draw!")
    elif sum_computer > 21:
        print(f"Computer has {sum_computer}\nYou have {sum_player}\nComputer is over 21. You win!")
    elif sum_player > 21:
        print(f"Computer has {sum_computer}\nYou have {sum_player}\nYou are over 21. Computer wins!")
    elif sum_computer > sum_player:
        print(f"Computer has {sum_computer}\nYou have {sum_player}\nComputer wins!")
    elif sum_player > sum_computer:
        print(f"Computer has {sum_computer}\nYou have {sum_player}\nYou win!")
    else:
        print(f"Computer has {sum_computer}\nYou have {sum_player}\nIt's a draw!")
    print("Thank you")

def replace_with_10(card_arr):
    for x in range(len(card_arr)):
        if card_arr[x] == "K" or card_arr[x] == "Q" or card_arr[x] == "J":
            card_arr[x] = 10

def choice():
    replace_with_10(my_choice)
    for x in range(len(my_choice)):
        if my_choice[x] == "A":
            choose_1_or_11 = True
            while choose_1_or_11:
                my_choice[x] = input("You picked an 'A' Do you want to replace it with 1 or 11: ")
                if my_choice[x] == '1' or my_choice[x] == '11':
                    my_choice[x] = int(my_choice[x])
                    choose_1_or_11 = False
                

def computer():
    computer_choice.append(rd.choice(cards))
    replace_with_10(computer_choice)
    for x in range(len(computer_choice)):
        if computer_choice[x] == "A":
            computer_choice[x] = rd.choice([1, 11])
    print(f"Computer cards: {computer_choice}")
    print(f"My cards: {my_choice}")

computer_choice = [rd.choice(cards)]
replace_with_10(computer_choice)
for x in range(len(computer_choice)):
    if computer_choice[x] == "A":
        computer_choice[x] = rd.choice([1, 11])

my_choice = [rd.choice(cards) for i in range(2)]
choice()

print(f"Computer cards: {computer_choice}")
print(f"My cards: {my_choice}")

continue_play = True
while continue_play:
    new_card = input("Type 'y' to get another card and 'n' to pass: ")
    if new_card == 'n':
        computer()
        winner()
        continue_play = False
    elif new_card == 'y':
        my_choice.append(rd.choice(cards))
        choice()
        computer()
        if sum(computer_choice) < 17:
            computer_choice.append(rd.choice(cards))
            replace_with_10(computer_choice)
            for x in range(len(computer_choice)):
                if computer_choice[x] == "A":
                    computer_choice[x] = rd.choice([1, 11])
            print(f"Computer new cards: {computer_choice}")
        winner()
        continue_play = False
    else:
        continue_play
        