import os.path
from tkinter import *
import random
import pandas as p

CSV_PATH = r"Tkinter\Flash card app\data\words_to_learn.csv"
if not os.path.exists(CSV_PATH):
    CSV_PATH = r"Tkinter\Flash card app\data\french_words.csv"

data = p.read_csv(CSV_PATH)
toLearn = data.to_dict(orient="records")
BACKGROUND_COLOR = "#B1DDC6"
currentCard = {}

def nextWord():
    global currentCard, flipTimer
    window.after_cancel(flipTimer)
    currentCard = random.choice(toLearn)
    canvas.itemconfig(title,text="French",fill="Black")
    canvas.itemconfig(word,text=currentCard["French"],fill="black")
    canvas.itemconfig(bgImage,image=front_img)
    flipTimer = window.after(3000,func=flipCard)

def flipCard():
    canvas.itemconfig(title,text="English",fill="White")
    canvas.itemconfig(word,text=currentCard["English"],fill="white")
    canvas.itemconfig(bgImage,image=back_img)

def isKnown():
    toLearn.remove(currentCard)
    data = p.DataFrame(toLearn)
    data.to_csv(r"Tkinter\Flash card app\data\words_to_learn.csv",index=False)
    nextWord()
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

flipTimer = window.after(3000,func=flipCard)

canvas = Canvas(width=800,height=526, highlightthickness=0,background=BACKGROUND_COLOR)
front_img = PhotoImage(file=r"Tkinter\Flash card app\images\card_front.png")
back_img = PhotoImage(file=r"Tkinter\Flash card app\images\card_back.png")
bgImage = canvas.create_image(400, 263, image=front_img)

title = canvas.create_text(400,150,text="",font=('Ariel 40 italic'))
word = canvas.create_text(400,263,text="",font=('Ariel', 60, 'bold'))
canvas.grid(row=0,column=0,columnspan=2)

imgWrong = PhotoImage(file=r"Tkinter\Flash card app\images\wrong.png")
unknownButton = Button(image=imgWrong,borderwidth=0,highlightthickness=0,command=nextWord)
unknownButton.grid(row=1,column=0)

imgCorrect = PhotoImage(file=r"Tkinter\Flash card app\images\right.png")
knownButton = Button(image=imgCorrect,borderwidth=0,highlightthickness=0,command=isKnown)
knownButton.grid(row=1,column=1)

nextWord()
window.mainloop()