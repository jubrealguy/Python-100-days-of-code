from turtle import Turtle

class Frame(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.pensize(5)
        self.speed(0)
        self.penup()
        self.goto(-300, 300)
        self.pendown()
        self.hideturtle()

    def draw(self, width, height):
        for _ in range(2):
            self.forward(width)
            self.right(90)
            self.forward(height)
            self.right(90)