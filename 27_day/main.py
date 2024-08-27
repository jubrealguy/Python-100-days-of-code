from tkinter import *

def button_clicked():
    print("I was clicked")
    my_label["text"] = input.get()

window = Tk()
window.title('Program')
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
my_label = Label(text="My Label", font=("Arial", 24, "bold"))
my_label["text"] = "Changed Label"
# my_label.pack(side="left")
my_label.config(text="config label")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx= 100, pady=20)

# Button
button = Button(text="Click me", command=button_clicked)
# button.pack(side="left")
# button.place(x=0, y=0)
button.grid(column=1, row=1)

button_new = Button(text="New Button", command=button_clicked)
button_new.grid(column=2, row=0)

# Entry
input = Entry(width=30)
# input.pack(side='left')
input.grid(column=3, row=2)







window.mainloop()