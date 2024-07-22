from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle:
    def __init__(self, x_pos, y_pos):
        self.create_paddle()
        self.paddle.penup()
        self.paddle.goto(x_pos, y_pos)

    def create_paddle(self):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        x_pos = self.paddle.xcor()
        y_pos = self.paddle.ycor() + MOVE_DISTANCE
        self.paddle.goto(x_pos, y_pos)

    def move_down(self):
        x_pos = self.paddle.xcor()
        y_pos = self.paddle.ycor() - MOVE_DISTANCE
        self.paddle.goto(x_pos, y_pos)