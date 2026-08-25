from tkinter import *
import math


# ----------------------------- CONSTANTS --------------------------------------- #
PINK: str = "#e2979c"
RED: str = "#e7305b"
GREEN: str = "#9bdeac"
YELLOW: str = "#f7f5dd"
FONT_NAME: str = "Courier"
WORK_MIN: int = 25
SHORT_BREAK_MIN: int = 5
LONG_BREAK_MIN: int = 20


# ---------------------------- TIMER RESET -------------------------------------- #
def timer_reset():
    """Sets pomodoro timer value to starting point."""
    global loop, countdown, timer_set
    loop = 0
    countdown = 0
    l_mark.config(text="")
    l_title.config(text="Timer", fg=GREEN)
    window.after_cancel(timer_on)
    canvas.itemconfig(timer_text, text=timer_set)


# -------------------------- TIMER MECHANISM ------------------------------------ #
def start_timer():
    """Starts pomodoro clock counting."""
    global countdown, loop
    if loop == 4:
        countdown = LONG_BREAK_MIN
        loop += 1
        l_mark.config(text="\u2714", fg=GREEN)
    elif loop < 4 and (countdown == 20 or countdown == 5 or countdown == 0):
        countdown = WORK_MIN
        l_mark.config(text="\u274c", fg=PINK)
        loop += 1
    elif loop < 4 and countdown == 25:
        countdown = SHORT_BREAK_MIN
        l_mark.config(text="\u2714", fg=RED)
    else:
        timer_reset()
        return
    count_down(countdown * 60)


# ------------------------- COUNTDOWN MECHANISM --------------------------------- #
def count_down(count):
    """Sets pomodoro counting time through stages."""
    global color
    global countdown
    global timer_on
    minutes = math.floor(count / 60)
    seconds = count % 60
    labor: str = ""
    if minutes < 10:
        minutes = f"0{minutes}"
        if minutes == 0:
            minutes = "00"
    if seconds < 10:
        seconds = "0"+str(seconds)
        if seconds == 0:
            seconds = "00"
    if (countdown * 60) == 1500:    
        color = GREEN
        labor = "Work"
    elif (countdown * 60) == 300:        
        color = PINK
        labor = "Break"
    elif (countdown * 60) == 1200:        
        color = RED
        labor = "Break"
        
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    l_title.config(text=labor, fg=color)
    timer_on = window.after(1000, count_down, count - 1)
    if count == 0:
        window.after_cancel(timer_on)
        start_timer()


# ------------------------------ UI SETUP --------------------------------------- #
loop = 0
color = GREEN
countdown = 0
timer_on = ""
timer_set = "00:00"
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="images/tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text=timer_set, fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

l_title = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 40, "bold"), fg=color, justify="center", padx=0, pady=0)
l_title.grid(column=1, row=0)

b_start = Button()
b_start.config(text="Start", highlightthickness=0, relief="groove", command=start_timer)
b_start.grid(column=0, row=2)

l_mark = Label()
l_mark.config(pady=10, text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"), anchor="s")
l_mark.grid(column=1, row=3)

b_reset = Button()
b_reset.config(text="reset", highlightthickness=0, relief="groove", command=timer_reset)
b_reset.grid(column=2, row=2)

window.mainloop()
