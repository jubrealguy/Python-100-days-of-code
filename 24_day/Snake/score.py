from turtle import Turtle
FONT = ("Arial", 18, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 0
        with open('my_file.txt') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 310)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.num}    ||    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.num > self.high_score:
            self.high_score = self.num
            with open('my_file.txt', 'w') as file:
                    file.write(str(self.high_score))
        self.num = 0
        self.update_score()
    
    def add_score(self):
        self.num += 1
        self.update_score()
