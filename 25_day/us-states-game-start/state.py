from turtle import Turtle

class State(Turtle):
    def __init__(self, user_choice = screen.textinput(title="Make your bet", prompt="Wrong color!!! Which Turtle will win? Choose a color: ")):
        super().__init__()
        self.name = name
        self.color = white