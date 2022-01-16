from cProfile import label
from tkinter import *
from turtle import width

def buttonClicked():
    mile = float(mileInput.get())
    kmOutput.config(state=NORMAL)
    kmOutput.delete(0,END)
    kmOutput.insert(0,round(mile*1.609,2))
    kmOutput.config(state=DISABLED)


window = Tk()
window.title("Mile to Kilometre Converter")
window.minsize(width=500,height=500)
window.config(pady=20,padx=20)

label = Label(text="Enter mile: ")
label.grid(column=1,row=1)

mileInput = Entry(width=30)
mileInput.grid(column=2,row=1)

label2 = Label(text="Value in Km: ")
label2.grid(column=1,row=2)

kmOutput = Entry(width=30)
kmOutput.config(state=DISABLED)
kmOutput.grid(column=2,row=2)

button = Button(text="Convert",command=buttonClicked)
button.grid(column=2,row=3)



window.mainloop()