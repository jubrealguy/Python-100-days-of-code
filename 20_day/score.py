from turtle import Turtle
FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.num} ", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.num += 1
        self.clear()
        self.update_score()
