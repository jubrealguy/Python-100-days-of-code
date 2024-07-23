from turtle import Turtle
FONT = ("Arial", 50, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score} ", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score} ", align=ALIGNMENT, font=FONT)

    def l_add(self):
        self.l_score += 1
        self.update_score()
    
    def r_add(self):
        self.r_score += 1
        self.update_score()


    # def update_score(self):
    #     self.write(f"Score: {self.num} ", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!!!", align=ALIGNMENT, font= FONT)
    
    # def add_score(self):
    #     self.num += 1
    #     self.clear()
    #     self.update_score()
