from turtle import Turtle, Screen
import random as rd
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('imagess.jpg', 6)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

def normalize_color(color):
    return (color[0]/255, color[1]/255, color[2]/255)

color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106)]

snake = Turtle()
screen = Screen()

x_default = -(screen.window_width() // 2) + 50
y_default = -(screen.window_height() // 2) + 50
snake.speed('fastest')
snake.penup()
default_position = (x_default, y_default)
snake.goto(default_position)
snake.pendown()
snake.shape("turtle")
snake.pensize(20)

print(screen.window_height())
print(screen.window_width())

while snake.ycor() < screen.window_height() // 2:
    def move_snake():
        snake.forward(1)
        snake.penup()
        snake.forward(50)
        snake.pendown()

    snake.color(normalize_color(rd.choice(color_list)))
    move_snake()

    if snake.xcor() > (screen.window_width() // 2) - 100:
        snake.setheading(90)
        move_snake()
        snake.setheading(180)

    if snake.xcor() <= -(screen.window_width() // 2) + 50:
        snake.setheading(90)
        move_snake()
        snake.setheading(360)





screen.exitonclick()