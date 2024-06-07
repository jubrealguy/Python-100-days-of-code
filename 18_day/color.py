from turtle import Turtle, Screen
import random as rd

# rgb_colors = []
# colors = colorgram.extract('images.jpg', 6)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

def normalize_color(color):
    return (color[0]/255, color[1]/255, color[2]/255)

color_list = [(252, 250, 245), (253, 245, 250), (238, 252, 244), (237, 243, 251), (244, 229, 50), (202, 7, 33)]

snake = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
default_position = (-350, -250)
snake.goto(default_position)
snake.shape("turtle")
snake.pensize(20)
snake.speed('fastest')

while snake.ycor() < screen.window_height():
    snake.color(normalize_color(rd.choice(color_list)))
    snake.forward(1)
    snake.penup()
    snake.forward(50)
    snake.pendown()

    if snake.xcor() >= 350:
        snake.setheading(90)
        snake.forward(1)
        snake.penup()
        snake.forward(50)
        snake.pendown()
        snake.setheading(180)

    if snake.xcor() <= -350:
        snake.setheading(90)
        snake.forward(1)
        snake.penup()
        snake.forward(50)
        snake.pendown()
        snake.setheading(360)





screen.exitonclick()