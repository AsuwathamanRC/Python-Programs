import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    global reps
    reps = 0
    window.after_cancel(timer)
    title.config(text="Timer")
    checkMark.config(text="")
    canvas.itemconfig(timerText,text="25:00")
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%8==0:
        title.config(text="Break",fg=RED)
        countDown(long_break_sec)
    elif reps%2==0:
        title.config(text="Break",fg=PINK)
        countDown(short_break_sec)
    else:
        title.config(text="Work",fg=GREEN)
        countDown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# ✔
def countDown(count):
    count_minutes = math.floor(count/60)
    count_seconds = count%60

    if count_seconds<10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timerText,text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000,countDown, count-1)
    else:
        startTimer()
        mark = ""
        workSessions = math.floor(reps/2)
        for _ in range(workSessions):
            mark += "✔"
        checkMark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
img = PhotoImage(file=r"Tkinter\Pomodoro project\tomato.png")
canvas.create_image(100, 112, image=img)
timerText = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)

title = Label(text="Timer",font=(FONT_NAME,25,"bold"),fg=GREEN,bg=YELLOW)
title.grid(column=1,row=0)

startButton = Button(text="Start",command=startTimer)
startButton.grid(row=2,column=0)

resetButton = Button(text="Reset",command=resetTimer)
resetButton.grid(row=2,column=2)

checkMark = Label(font=(FONT_NAME,15,"bold"),fg=GREEN,bg=YELLOW)
checkMark.grid(row=3,column=1)

window.mainloop()