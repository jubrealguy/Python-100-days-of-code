from turtle import Turtle, Screen

ade = Turtle()
screen = Screen()

def move_forward():
    ade.forward(10)
def move_backward():
    ade.backward(10)
def clockwise():
    ade.right(10)
def counter_clockwise():
    ade.left(10)
def clear():
    ade.clear()
    ade.penup()
    ade.home()
    ade.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(clockwise, "d")
screen.onkey(counter_clockwise, "a")
screen.onkey(clear, "c")

screen.exitonclick()