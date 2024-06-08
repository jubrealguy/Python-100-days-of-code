from turtle import Turtle, Screen
import random as rd

# List of colors to be used
color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106)]

# Create turtle object and screen
snake = Turtle()
screen = Screen()
screen.colormode(255)  # Set color mode to 255 to use RGB colors directly

# Initial turtle setup
snake.speed('fastest')
#snake.shape("turtle")
snake.pensize(20)


# Function to move the turtle forward by 50 units, lifting the pen for the second half
def move_snake():
    snake.forward(1)
    snake.penup()
    snake.forward(50)
    snake.pendown()

def transparent_move_to_edge(x, y):
    snake.penup()
    snake.goto(x, y)
    snake.pendown()

# Initial position setup
x_default = -(screen.window_width() // 2) + 50
y_default = -(screen.window_height() // 2) + 50

transparent_move_to_edge(x_default, y_default)

# Main loop to move the turtle across the screen in a grid pattern
while snake.ycor() < screen.window_height() // 2:
    snake.color(rd.choice(color_list))  # Choose a random color
    if snake.xcor() < screen.window_width() // 2 - 50:
        move_snake()  # Move forward if within the screen width
    else:
        y_default += 50  # Move up by 50 units if at the right edge
        transparent_move_to_edge(x_default, y_default)


screen.exitonclick()
