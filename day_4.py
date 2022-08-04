import random as rd

# ***** CHOOSING HEAD OR TAIL AT RANDOM *****

# side = rd.randint(0, 1)

# if side == 0:
#     print("Head")
# else:
#     print("Tail")


# ***** CHOOSING SOMEONE TO FOOT A BILL OUT OF A LIST OF FRIENDS *****

# names_str = input("Provide everyone's name separated by a comma, let me find the payer\n")
# names = names_str.split(", ")
# last_name = len(names) - 1
# r = rd.randint(0, last_name)
# payer = names[r]

# print(f"No much worry guyz, {payer} is footing the bill")


# ***** PUTTING AN X SPOT IN A NESTED ARRAY *****

# row1 = ['😒', '😞', '😔']
# row2 = ['😟', '😕', '🙁']
# row3 = ['☹️', '😀', '😃']
# map = [row1, row2, row3]

# print(f"{row1}\n{row2}\n{row3}")
# print("Your first digit is the row number while your second digit is the column number")
# num = int(input("Enter a two-digit number to mark X in a spot in the board: "))

# x = (num // 10) - 1
# y = (num % 10) - 1

# map[x][y] = "X"
# print(f"{row1}\n{row2}\n{row3}")

# ****** ROCK, PAPER, SCISSORS GAME *****

options = ['Rock', 'Paper', 'Scissors']

print("Welcome to the Rock, Paper, Scissors Game")
print("""
0 for Rock
1 for Paper
2 for Scissors
""")

player = int(input("Enter one of 0, 1, 2: "))
cpu = rd.randint(0, 2)
player_op = options[player]
cpu_op = options[cpu]

print(f"You chose {player_op}")
print(f"Computer choses {cpu_op}")

if player == cpu:
    print("It's a draw")
elif player == 0 and cpu == 1:
    print("Computer wins")
elif player == 1 and cpu == 0:
    print("You win")
elif player == 0 and cpu == 2:
    print("You win")
elif player == 2 and cpu == 0:
    print("Computer win")
elif player == 1 and cpu == 2:
    print("Computer wins")
elif player == 2 and cpu == 1:
    print("You win")
elif player > 2 or player < 0:
    print("You typed a wrong number")
else:
    print("Please enter an integer as ashown above")