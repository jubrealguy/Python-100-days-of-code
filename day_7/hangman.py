import random

word_list = ['irksome', 'iterate', 'chronology']
chosen_word = random.choice(word_list)

if chosen_word == 'irksome' or chosen_word == 'iterate':
    word_holder = ['-', '-', '-', '-', '-', '-', '-']
    print(word_holder)
else:
    word_holder = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    print(word_holder)

print(f"""
    + - - - +
    |       |
    0       |
   /|\\      |
   / \\      |
            |

================
""")

hang_sym = ['0', '|', '/', '\\', '/', '\\']
letter = input("Guess a letter? ").lower()

for alpha in chosen_word:
    if letter == alpha:
        a = chosen_word.find(letter)
        print(a)
        print("Right")
    else:
        print("wrong")