import tkinter
import json
from tkinter.constants import END
from tkinter import messagebox
from pwd_generator import generate_password
USER = "email"
PWD = "pwd"

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
        website_entry = website.get()
        new_data = {
            website_entry:{
                "email": username.get(),
                "pwd": password.get()
            }
        }
        try:
            with open(f"./data.json", "r") as file:
                file_data = json.load(file)
        except FileNotFoundError:
            with open(f"./data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            file_data.update(new_data)
            with open(f"./data.json", "w") as file:
                json.dump(file_data, file, indent=4)
        finally:
            website.delete(0, END)
            username.delete(0, END)
            password.delete(0, END)
            messagebox.showinfo(message="A new entry on your password manager was successfully added.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_pwd():
    try:
        with open(f"./data.json", "r") as file:
            file_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="No data file found!")
    else:
        search_input = website.get()
        if search_input in file_data:
            messagebox.showinfo(message = f"Username:  {file_data[search_input][USER]}\nPassword:  {file_data[search_input][PWD]}")
        else:
            messagebox.showinfo(message="No data found.")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

#Canvas
canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
#Labels
website_label = tkinter.Label(text="Website:")
username_label = tkinter.Label(text="Email/Username:")
password_label = tkinter.Label(text="Password:")

#Inputs
website = tkinter.Entry(width=21)
website.focus()
username = tkinter.Entry(width=39)
password = tkinter.Entry(width=21)

#Buttons
generate_btn = tkinter.Button(text="Generate Password", width=14, command=new_pass)
add_btn = tkinter.Button(width=36, text="Add", command=save)
search_btn = tkinter.Button(text="Search", width=14, command=find_pwd)

#Grid Layout
canvas.grid        (column=1, row=0)
website_label.grid (column=0, row=1)
username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website.grid       (column=1, row=1)
username.grid      (column=1, row=2, columnspan=2)
password.grid      (column=1, row=3)
generate_btn.grid  (column=2, row=3)
add_btn.grid       (column=1, row=4, columnspan=2)
search_btn.grid    (column=2, row=1)

window.mainloop()