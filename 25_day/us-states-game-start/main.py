from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")
screen.bgcolor('black')
img = "blank_states_img.gif"
screen.addshape(img)

turtle = Turtle(img)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?") 
data = pd.read_csv('50_states.csv')
print(data.state.to_list())

screen.exitonclick()