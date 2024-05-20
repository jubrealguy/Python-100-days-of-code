import random as rd

print("""

   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                                                                                                                 
""")

print("Welcome to Number Guessing Game")
print("I'm thinking of a number between 1 -100")

random_num = rd.randint(1, 100)

def guess_game(num_trials):
    more_attempts = True
    while more_attempts:
        print(f"You have {num_trials} attempts remaining to guess the number")
        guessed_num = int(input("Make a guess: "))
        if num_trials > 1:
            if guessed_num == random_num:
                print("You got it, the answer is {}".format(random_num))
                more_attempts = False
            elif guessed_num > random_num:
                print(f"Too high\nGuess again")
            else:
                print(f"Too low\nGuess again")
        else:
            print(f"You have run out of guesses, you lose")
            more_attempts = False
        num_trials-=1

level_flag = True
while level_flag:
    level = input("Choose a difficulty, type 'easy' or 'hard: ").lower()
    if level == 'easy':
        guess_game(10)
        level_flag = False
    elif level == 'hard':
        guess_game(5)
        level_flag = False
    else:
        print("Wrong input, type 'easy' or 'hard: ")