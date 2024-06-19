from turtle import Turtle, Screen
import random as rd

ade = Turtle()
tosin = Turtle()
ola = Turtle()
dayo = Turtle()
titi = Turtle()

screen = Screen()

ade.shape("turtle")
ade.color("red")
ade.penup()
ade.goto(-250, -250)

tosin.shape("turtle")
tosin.color("blue")
tosin.penup()
tosin.goto(-250, -125)

ola.shape("turtle")
ola.color("green")
ola.penup()
ola.goto(-250, 0)

dayo.shape("turtle")
dayo.color("yellow")
dayo.penup()
dayo.goto(-250, 125)

titi.shape("turtle")
titi.color("purple")
titi.penup()
titi.goto(-250, 250)


while ade.xcor() < 250:
    ade.forward(rd.randint(1, 4))

while tosin.xcor() < 250:
    tosin.forward(rd.randint(1, 4))

while ola.xcor() < 250:
    ola.forward(rd.randint(1, 4))

while dayo.xcor() < 250:
    dayo.forward(rd.randint(1, 4))

while titi.xcor() < 250:
    titi.forward(rd.randint(1, 4))




# tosin.shape("turtle")
# ola.shape("turtle")
# dayo.shape("turtle")
# titi.shape("turtle")


# tosin.color("blue")
# ola.color("green")
# dayo.color("yellow")
# titi.color("purple")



screen.exitonclick()