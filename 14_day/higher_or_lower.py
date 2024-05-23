from arts import logo, vs
from game_data import data
import random as rd
from os import system #for windows
clear = lambda: system('cls')

print(logo)

def get_random_item(exclude=[]):
    """Get a random item from data excluding the ones in exclude list."""
    choices = [item for item in data if item not in exclude]
    return rd.choice(choices)

a = get_random_item()
b = get_random_item(exclude=[a])

score = 0
should_continue = True
while should_continue:
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, {b['description']}, {b['country']}")

    option = input("Who has more followers, type A or B: ").upper()
    clear()
    print(logo)
    if option in ["A", "B"]:
        if (option == "A" and a['follower_count'] > b['follower_count']) or (option == "B" and b['follower_count'] > a['follower_count']):
            score += 1
            print(f"You are right! Current score: {score}")
            a = b
            b = get_random_item(exclude=[a])
        else:
            print(f"You are wrong. Final score is {score}")
            should_continue = False
    else:
        print("Invalid input. Please type 'A' or 'B'.")