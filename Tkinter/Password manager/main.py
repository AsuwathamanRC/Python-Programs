import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

WHITE = "#fff"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^', '-', '_', '=', '`', '~', '[', ']', '{', '}', '\\', '|', ':', ';', "'", '"', ',', '<', '.', '>', '/', '?']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)
    password = "".join(password_list)

    passwordEntry.delete(0,END)
    passwordEntry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePswd():
    email = emailEntry.get()
    password = passwordEntry.get()
    website = websiteEntry.get()

    if len(email)==0 or len(password)==0 or len(website)==0:
        messagebox.showwarning(title="Oops",message="Please don't leave any fields empty!")
    else:
        isOk = messagebox.askokcancel(title=website.title(),message=f"These are the details entered.\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        # Save data in txt file
        # if isOk:
        #     with open(r"Tkinter\Password manager\data.txt", "a") as f:
        #         f.write(f"{website} | {email} | {password}\n")
        #         passwordEntry.delete(0,END)
        #         websiteEntry.delete(0,END)

        # Save data in json file
        if isOk:
            newData = {website.lower():{
                "email": email,
                "password": password
            }}
            try:
                with open(r"Tkinter\Password manager\data.json","r") as f:
                    data = json.load(f)
                    data.update(newData)
            except FileNotFoundError:
                # Creates a new file
                with open(r"Tkinter\Password manager\data.json", 'w') as f:
                    json.dump(newData,f,indent=4)
                    pass
            else:
                with open(r"Tkinter\Password manager\data.json","w") as f:
                    json.dump(data,f,indent=4)
            finally:
                passwordEntry.delete(0,END)
                websiteEntry.delete(0,END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def searchPassword():
    website = websiteEntry.get().lower()
    try:
        with open(r"Tkinter\Password manager\data.json","r") as f:
            data = json.load(f)
            email = data[website]["email"]
            password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No data file found.")
    except KeyError:
        messagebox.showwarning(title="Warning",message=f"No password found for {website.title()}")
    else:
        messagebox.showinfo(title=website.title(),message=f"Email: {email}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,background=WHITE)

canvas = Canvas(width=200,height=200, highlightthickness=0, bg=WHITE)
img = PhotoImage(file=r"Tkinter\Password manager\logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0,column=1)

# Labels
website = Label(text="Website:", bg=WHITE)
website.grid(row=1,column=0)
email = Label(text="Email/Username:", bg=WHITE)
email.grid(row=2,column=0)
pswd = Label(text="Password:", bg=WHITE)
pswd.grid(row=3,column=0)

# Entries
websiteEntry = Entry(width=32)
websiteEntry.grid(row=1,column=1)
websiteEntry.focus()
emailEntry = Entry(width=50)
emailEntry.grid(row=2,column=1,columnspan=2)
emailEntry.insert(0,"defaultmail@test.com")
passwordEntry = Entry(width=32)
passwordEntry.grid(row=3,column=1)

# Buttons
searchBtn = Button(text="Search",command=searchPassword,width=12)
searchBtn.grid(row=1,column=2)
generatePswdBtn = Button(text="Generate Password",command=generatePassword)
generatePswdBtn.grid(row=3,column=2)
addBtn = Button(text="Add",command=savePswd,width=43)
addBtn.grid(row=4,column=1,columnspan=2)

window.mainloop()