from turtle import Turtle, Screen
import threading
import random as rd


ade = Turtle()
tosin = Turtle()
ola = Turtle()
dayo = Turtle()
titi = Turtle()

screen = Screen()

turtles = [
    (ade, "ade", "red", -350, -300),
    (tosin, "tosin", "blue", -350, -150),
    (ola, "ola", "green", -350, 0),
    (dayo, "dayo", "yellow", -350, 150),
    (titi, "titi", "purple", -350, 300)
]

for turtle, name, color, x, y in turtles:
    turtle.shape("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)

race_over = threading.Event()
def move_turtle(turtle, name):
    while turtle.xcor() < 330 and not race_over.is_set():
        turtle.forward(rd.randint(1, 5))
        if turtle.xcor() >= 330 and not race_over.is_set():
            race_over.set()
            print(f"{name} with color {turtle.color()[0]} has won the game")
            screen.ontimer(screen.bye, 1000)
            break


def start_race():
    for turtle, name, col, x, y in turtles:
        threading.Thread(target=move_turtle, args=(turtle, name)).start()

screen.onkey(start_race, "space")
screen.listen()




screen.exitonclick()