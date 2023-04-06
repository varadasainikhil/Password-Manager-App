from tkinter import *

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open(file="passwords.txt", mode="a") as file:
        file.write(f"{website_text.get()} | {email_text.get()} | {password_text.get()} \n")
    website_text.delete(0, END)
    password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(220, 220)
window.config(padx=20, pady=20)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website", font=(FONT_NAME, 12, "bold"))
website_label.grid(row=1, column=0)

website_text = Entry(width=52)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()

email_label = Label(text="Email/Username", font=(FONT_NAME, 12, "bold"))
email_label.grid(row=2, column=0)

email_text = Entry(width=52)
email_text.grid(row=2, column=1, columnspan=2)
email_text.insert(0, "varadasainikhil@gmail.com")

password_label = Label(text="Password", font=(FONT_NAME, 12, "bold"))
password_label.grid(row=3, column=0)

password_text = Entry(width=34)
password_text.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=14, padx=0, pady=0)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
