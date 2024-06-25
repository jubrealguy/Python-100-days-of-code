# from turtle import Turtle, Screen
# import threading
# import random as rd


# Turtle().shape('turtle')
# # Naming of Turtles
# ade = Turtle()
# tosin = Turtle()
# ola = Turtle()
# dayo = Turtle()
# titi = Turtle()

# screen = Screen()

# # Setting up width and height of screen
# screen.setup(width=800, height=680)

# user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: ")
# print(user_choice)

# # Turtles, their names, colors and positions in a tuple
# turtles = [
#     [ade, "ade", "red", -350, -300],
#     [tosin, "tosin", "blue", -350, -150],
#     [ola, "ola", "green", -350, 0],
#     [dayo, "dayo", "yellow", -350, 150],
#     [titi, "titi", "purple", -350, 300]
# ]

# # Assigning color and positions to the turtles
# for turtle, name, color, x, y in turtles:
#     turtle.color(color)
#     turtle.penup()
#     turtle.goto(x, y)

# # Moving the turtles from starting to finishing and determining the first position
# race_over = threading.Event()
# def move_turtle(turtle, name):
#     while turtle.xcor() < 330 and not race_over.is_set():
#         turtle.forward(rd.randint(1, 5))
#         if turtle.xcor() >= 330 and not race_over.is_set():
#             race_over.set()
#             print(f"{name} with color {turtle.color()[0]} has won the game")
#             screen.ontimer(screen.bye, 1000)
#             break

# # A function that turtles starts at the same time and move at the same time
# def start_race():
#     for turtle, name, col, x, y in turtles:
#         threading.Thread(target=move_turtle, args=(turtle, name)).start()

# # Using the space key to trigger the function
# screen.onkey(start_race, "space")
# screen.listen()




# screen.exitonclick()


# <<<<< --------------------------------------------------------- >>>>>>

from turtle import Turtle, Screen
import random as rd

screen = Screen()
screen.setup(width=800, height=680)
user_choice = screen.textinput(title="Make your bet", prompt="Which Turtle will win? Choose a color: ")
race_on = False

colors = ["red", "blue", "green", "purple", "yellow", "grey"]
y_position = [-125, -75, -25, 25, 75, 125]
all_turtles = []

while user_choice not in colors:
    user_choice = screen.textinput(title="Make your bet", prompt="Wrong color!!! Which Turtle will win? Choose a color: ")

for i in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-350, y=y_position[i])
    all_turtles.append(new_turtle)

if user_choice:
    race_on = True

while race_on:
    for turtle in all_turtles:
        dist = rd.randint(0, 10)
        turtle.forward(dist)
        if turtle.xcor() > 350:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You win, {turtle.pencolor()} won the race")
            else:
                print(f"You lose, {turtle.pencolor()} won the race")
            






screen.exitonclick()