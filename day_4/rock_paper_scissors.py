import random as rd

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