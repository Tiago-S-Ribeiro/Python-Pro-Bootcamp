import tkinter
#import pyperclip
from tkinter.constants import END
from tkinter import messagebox
from pwd_generator import generate_password

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def new_pass():
    if len(password.get()) != 0:
        password.delete(0, END)

    generated_pwd = generate_password()
    password.insert(0, generated_pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def fields_not_valid():
    return len(website.get()) == 0 or len(username.get()) == 0 or len(password.get()) == 0

def save():
    if fields_not_valid():
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(message=f"Details for [{website.get()}]:\nE-mail/Username:  {username.get()}\nPassword:  {password.get()}")

        if is_ok:
            #pyperclip.copy(password.get())
            with open(f"./data_text.txt", "a") as file:
                file.write(f"{website.get()} | {username.get()} | {password.get()}\n")
                
                website.delete(0, END)
                username.delete(0, END)
                password.delete(0, END)
                messagebox.showinfo(message="A new entry on your password manager was successfully added.")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

#Canvas
canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

#Labels
website_label = tkinter.Label(text="Website:")
username_label = tkinter.Label(text="Email/Username:")
password_label = tkinter.Label(text="Password:")

#Inputs
website = tkinter.Entry(width=39)
website.focus()
username = tkinter.Entry(width=39)
password = tkinter.Entry(width=21)

#Buttons
generate_btn = tkinter.Button(text="Generate Password", width=14, command=new_pass)
add_btn = tkinter.Button(width=36, text="Add", command=save)

#Grid Layout
canvas.grid        (column=1, row=0)
website_label.grid (column=0, row=1)
username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website.grid       (column=1, row=1, columnspan=2)
username.grid      (column=1, row=2, columnspan=2)
password.grid      (column=1, row=3)
generate_btn.grid  (column=2, row=3)
add_btn.grid       (column=1, row=4, columnspan=2)

window.mainloop()