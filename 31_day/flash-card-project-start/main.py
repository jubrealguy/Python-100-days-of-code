from tkinter import *
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

title = 'French'
data = pd.read_csv('./data/french_words.csv')
lang_dict = data.to_dict(orient='records')

def next_card():
    current_card = rd.choice(lang_dict)
    canvas.itemconfig(card_title, text = "French")
    canvas.itemconfig(card_word, text = current_card["French"])

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")

canvas.create_image(400, 263 , image=card_front_image)
card_title = canvas.create_text(400, 150, text=title, font=('Arial', 40, 'italic'))

card_word = canvas.create_text(400, 263, text="word", font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()