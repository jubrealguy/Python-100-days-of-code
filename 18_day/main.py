from turtle import Turtle, Screen
import random as rd

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown', 'black', 'cyan']
set_angles = [0, 90, 180, 270]


snake = Turtle()
screen = Screen()
snake.shape("turtle")
snake.color("red")
snake.pensize(10)
snake.speed('fastest')
screen.colormode(255)

# # To draw a square
# for i in range(4):
#     snake.forward(200)
#     snake.right(90)

# # To draw a dashed line
# for i in range(15):
#     snake.forward(10)
#     snake.penup()
#     snake.forward(10)
#     snake.pendown()

# # Shapes with different sizes
# num_of_sides = 3
# for _ in range(7):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         snake.forward(100)
#         snake.left(angle)
#     num_of_sides += 1
#     snake.color(rd.choice(colors))

# prev_angle = None
# while True:
#     next_angle = rd.choice(set_angles)
#     while next_angle == prev_angle:
#         next_angle = rd.choice(set_angles)
#     snake.forward(20)
#     snake.setheading(next_angle)
#     prev_angle = next_angle
#     snake.color(rd.choice(colors))

def randomColor():
    r = rd.randint(1, 255)
    g = rd.randint(1, 255)
    b = rd.randint(1, 255)

    color = (r, g, b)
    return color

for _ in range(5000):
    next_angle = rd.choice(set_angles)
    snake.forward(20)
    snake.setheading(next_angle)
    snake.color(randomColor())


screen.exitonclick()