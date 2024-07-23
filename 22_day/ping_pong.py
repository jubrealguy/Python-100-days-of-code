from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()

screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect when ball hit upper and lower boundary
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect when ball hits paddle
    if (ball.distance(paddle_right) < 50 and ball.xcor() > 330) or (ball.distance(paddle_left) < 50 and ball.xcor() < -330):
        ball.x_bounce()

    # Dectect when right paddle misses the ball
    if ball.xcor() > 340:
        ball.reset()
        score.l_add()

    # Dectect when left paddle misses the ball
    if ball.xcor() < -340:
        ball.reset()
        score.r_add()
    




screen.exitonclick()