from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Generator")

canvas =Canvas(width=200, height=200)
padlock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="W")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="W")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=27)
password_input.grid(row=3, column=1, sticky="W")

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()