from turtle import Turtle, Screen

ade = Turtle()
screen = Screen()

def move_forward():
    ade.forward(10)

def face_up():
    ade.left(90)
    ade.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()