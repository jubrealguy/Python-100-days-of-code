from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

# Formatting the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('A Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect Colission
    if snake.head.distance(food) < 10:
        print("chopped")
        food.refresh()
        snake.extend_snake()
        scoreboard.add_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_on = False
        scoreboard.game_over()

    for block in snake.snake_blocks[1:]:
        if snake.head.distance(block) < 5:
            game_on = False
            scoreboard.game_over()


screen.exitonclick ()