import random as rd

row1 = ['😒', '😞', '😔']
row2 = ['😟', '😕', '🙁']
row3 = ['☹️', '😀', '😃']
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
print("Your first digit is the row number while your second digit is the column number")
num = int(input("Enter a two-digit number to mark X in a spot in the board: "))

x = (num // 10) - 1
y = (num % 10) - 1

map[x][y] = "X"
print(f"{row1}\n{row2}\n{row3}")