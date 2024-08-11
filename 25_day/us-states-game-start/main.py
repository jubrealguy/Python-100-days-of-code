from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")
screen.bgcolor('black')
img = "blank_states_img.gif"
screen.addshape(img)

turtle = Turtle(img)
pen = Turtle()
pen.hideturtle()

data = pd.read_csv('50_states.csv')
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?") 
answer_state = answer_state.title()
guessed_states = []

while len(guessed_states) < 50:
    states = data.state.to_list()

    if answer_state == 'Exit':
        data.drop(['x', 'y'], axis=1, inplace=True)
        data.to_csv('states to learn.csv', index=False)
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        answer_row = data[data.state == answer_state]
        pen.penup()
        pen.goto(int(answer_row.x), int(answer_row.y))
        pen.write(answer_state, font=("Poppins", 6, "normal"))
        data = data[data.state != answer_state]
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?") 
        answer_state = answer_state.title()
    else:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?") 
        answer_state = answer_state.title()


screen.exitonclick()