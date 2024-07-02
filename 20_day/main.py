from turtle import Screen
from snake import Snake
import time

# Formatting the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('A Snake Game')
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# Moving the snake, making a snake block replace the position of the one in it's front
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

screen.exitonclick ()