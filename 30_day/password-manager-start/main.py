from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# json.dump() ---- Write
# json.load() ---- Read
# json.update() ---- Update

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops!!!!!', message='You left a box empty')
    else:
        try:
            with open("data.json", "r") as file:
                # Read data
                data = json.load(file)
                
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # Update data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Save updated data
                json.dump(data, file, indent=4)

        finally:
                website_input.delete(0, END)
                password_input.delete(0, END)

def search():
    web_input = website_input.get()
    try:
        with open("data.json", "r") as file:
            websites = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Oops!!!!!', message="No Data File Found")
    else:
        if web_input in websites:
            email = websites[web_input]["email"]
            password = websites[web_input]["password"]
            messagebox.showinfo(title=web_input, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No data found for {web_input}')
    finally:
        website_input.delete(0, END)

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
website_input = Entry(width=40)
website_input.grid(row=1, column=1)
search_button = Button(text="Search", command=search, width=14)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=58)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, 'whizkidjubrealguy@gmail.com')

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=40)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password, width=14)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=50, command=save)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()