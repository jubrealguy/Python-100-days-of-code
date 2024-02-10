import random as rd

print("""
 _                                           
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
      """)

hangman = ["""
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
    =========
    """, """
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
    =========
    """, """
        +---+
        |   |
        O   |
       /|\  |
            |
            |
    =========
    """, """
        +---+
        |   |
        O   |
       /|   |
            |
            |
    =========
    """, """
        +---+
        |   |
        O   |
       /    |
            |
            |
    =========
    """, """
        +---+
        |   |
        O   |
            |
            |
            |
    =========
    """, """
        +---+
        |   |
            |
            |
            |
            |
    =========
    """, """
        +---+
            |
            |
            |
            |
            |
    =========
    """]

rope = ['|', 'O', '/', '|', '\\', '/', '|', '\\']
correct_words = ["olaleye", "adebayo", "titilayo", "oladayo", "oluwatosin"]
chosen_word = list(rd.choice(correct_words))

word = []
for i in range(len(chosen_word)):
    word.append('_')
print(''.join(word))

game_ends = False
lives = 7
while not game_ends:
    guess = input("Guess a letter: ").lower()
    for pos in range(len(chosen_word)):
        if guess == chosen_word[pos]:
            print(f"Your guess {guess} is correct")
            word[pos] = guess
    

    if guess not in chosen_word:
        lives -= 1
        print(f"Your guess {guess} is not in the word")
        if lives == 0:
            print("You have lost")
            game_ends = True

    print(''.join(word))
    print(hangman[lives])

    if '_' not in word:
        game_ends = True
        print("You have won")

# if letter == guess:
#             letter_index = chosen_word.index(letter)
#             word[letter_index] = guess
#             chosen_word[letter_index] = '-'