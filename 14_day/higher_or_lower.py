from arts import logo, vs
from game_data import data
import random as rd

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
    print(f"Compare A: {a['name']}, {a['description']}, {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, {b['description']}, {b['country']}")

    option = input("Who has more followers, type A or B: ").upper()
    if option == "A":
        if a['follower_count'] > b['follower_count']:
            score += 1
            print(f"You are right! Current score: {score}")
            a = b
            b = get_random_item(exclude=[a])
        else:
            print("you lose")
            print(f"Your final score is {score}")
            should_continue = False
    elif option == "B":
        if b['follower_count'] > a['follower_count']:
            score += 1
            print(f"You are right! Current score: {score}")
            b = a
            a = get_random_item(exclude=[b])
        else:
            print("you lose")
            print(f"Your final score is {score}")
            should_continue = False
    else:
        print("Invalid input. Please type 'A' or 'B'.")
