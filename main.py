from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Function to generate a password


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Function to save the password into a .txt file
def save_password():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    new_data = {website_text: {
        "email": email_text,
        "password": password_text
    }}

    if len(website_text) == 0 or len(password_text) == 0 or len(email_text) == 0:
        messagebox.showinfo(title="Error", message="Please fill out all the fields.")
    else:
        try:
            with open(file="data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)

        pyperclip.copy(password_text)
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Creating a window
window = Tk()
window.minsize(220, 220)
window.config(padx=20, pady=20)
window.title("Password Manager")

# Creating a canvas for the image
canvas = Canvas(width=200, height=200)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(row=0, column=1)

# Creating a label for the Website
website_label = Label(text="Website", font=(FONT_NAME, 12, "bold"))
website_label.grid(row=1, column=0)

# Creating an entry for the user to enter the website address
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Creating a label for the Email
email_label = Label(text="Email/Username", font=(FONT_NAME, 12, "bold"))
email_label.grid(row=2, column=0)

# Creating an entry for the user to enter the email address
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "johndoe@gmail.com")

# Creating a label for the password
password_label = Label(text="Password", font=(FONT_NAME, 12, "bold"))
password_label.grid(row=3, column=0)

# Creating an entry for the user to enter the password
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Creating a Button to generate Password
generate_password_button = Button(text="Generate Password", width=14, padx=0, pady=0, command=generate_password)
generate_password_button.grid(row=3, column=2)


add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
