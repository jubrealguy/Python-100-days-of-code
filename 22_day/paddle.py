from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, y_pos)

    def move_up(self):
        x_pos = self.xcor()
        y_pos = self.ycor() + MOVE_DISTANCE
        self.goto(x_pos, y_pos)

    def move_down(self):
        x_pos = self.xcor()
        y_pos = self.ycor() - MOVE_DISTANCE
        self.goto(x_pos, y_pos)