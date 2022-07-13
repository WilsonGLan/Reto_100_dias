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

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    labelTitle.config(text="Timer")
    labelCheck.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        labelTitle.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(long_break_sec)
        labelTitle.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        labelTitle.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_seg = count % 60

    if count_seg < 10 and count_seg >= 0:
        count_seg = "0"+str(count_seg)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seg}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        labelCheck.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW, highlightthickness=0)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row= 1)

buttonStart = Button(text="Start", highlightthickness=0, command=start_timer)
buttonStart.grid(column=0, row=3)

buttonReset = Button(text="Reset", highlightthickness=0, command=reset_timer)
buttonReset.grid(column=2, row=3)

labelTitle = Label(text="TIMER", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg= YELLOW)
labelTitle.grid(column=1, row= 0)

labelCheck = Label(text="✔", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg= YELLOW)
labelCheck.grid(column=1, row= 4)



window.mainloop()