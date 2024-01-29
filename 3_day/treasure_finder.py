print("Welcome to Ozomba Island")
print("You have been chosen to find the missing prince")
print("The King is counting on you and may the gods be with you")
direction = input("You are at a T-junction, where would you go? Type 'left' or 'right': ")

if direction == "left":
    decision = input("You are at a river, type 'swim' to swim and 'wait' to wait for a boat: ")
    if decision == "wait":
        color = input("You arrived at the Island, three doors beckon, red, blue and yellow. Type the color you choose: ")
        if color == "blue":
            print("Congratulatios, you found the boy!!!!")
        elif color == "red":
            print("You are in a room full of fire, game over!!!")
        elif color == "yellow":
            print("You are in a lion's den, game over!!!")
        else:
            print("wrong choice, game over!!!")
    else:
        print("You drowned, game over!!!")
else:
    print("you ot caught up in thorns, game over!!!")