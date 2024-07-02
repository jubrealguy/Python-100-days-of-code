from turtle import Turtle, Screen
import time

# Formatting the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('A Snake Game')
screen.tracer(0)

# Buildind a Snake of three blocks
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
snake = []
for pos in starting_pos:
    snake_block = Turtle('square')
    snake_block.color('white')
    snake_block.penup()
    snake_block.goto(pos)
    snake.append(snake_block)

# Moving the snake, making a snake block replace the position of the one in it's front
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for block_index in range(2, 0, -1):
        x_cor = snake[block_index - 1].xcor()
        y_cor = snake[block_index - 1].ycor()
        snake[block_index].goto(x_cor, y_cor)
    snake[0].forward(20)
    snake[0].left(90)

screen.exitonclick ()