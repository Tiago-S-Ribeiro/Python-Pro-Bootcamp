import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
FONT_CANVAS = ("Courier", 32, "normal")
FONT_LABEL = ("Courier", 46, "bold")
FONT_MARK = ("Courier", 28, "normal")
BG = "#FAEDC6"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#519259"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ------------------------------ TIMER RESET --------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="TIMER", fg=GREEN)
    marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    TIME_TO_WORK = WORK_MIN * 60
    TAKE_A_SHORT_BREAK = SHORT_BREAK_MIN * 60
    TAKE_A_LONG_BRAKE = LONG_BREAK_MIN * 60

    if reps == 8:
        label.config(text="Long Break", fg=RED)
        countdown(TAKE_A_LONG_BRAKE)
    elif reps % 2 == 0:
        label.config(text="Short Break", fg=PINK)
        countdown(TAKE_A_SHORT_BREAK)
    else:
        label.config(text="Work", fg=GREEN)
        countdown(TIME_TO_WORK)
    
# --------------------------- COUNTDOWN MECHANISM ---------------------------- # 
def countdown(time):
    global reps
    global timer
    minutes = math.floor(time / 60)
    seconds = time % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    output_time = f"{minutes}:{seconds}"

    canvas.itemconfig(timer_text, text=output_time)
    if time > 0:
        timer = window.after(1000, countdown, time - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks.config(text=marks.cget("text")+CHECKMARK)
        if reps > 8:
            reset_timer()

# -------------------------------- UI SETUP ---------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.minsize(width=500, height=500)
window.config(padx=60, pady=80, bg=BG)

canvas = tkinter.Canvas(width=300, height=300, bg=BG, highlightthickness=0)
tomato = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato)
timer_text = canvas.create_text(150, 170, text="00:00", font=FONT_CANVAS)

label =     tkinter.Label(text="TIMER", font=FONT_LABEL, bg=BG, fg=GREEN)
start_btn = tkinter.Button(text="Start", highlightbackground=BG, fg=RED, command=start_timer)
reset_btn = tkinter.Button(text="Reset", highlightbackground=BG, fg=RED, command=reset_timer)
marks =     tkinter.Label(font=FONT_MARK, bg=BG, fg=GREEN)

canvas.grid   (column=1, row=1)
label.grid    (column=1, row=0)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)
marks.grid    (column=1, row=3)

window.mainloop()