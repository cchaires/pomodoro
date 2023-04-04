from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND = "#454545"
C2 = "#FF6000"
C3 = "#FFA559"
C4 = "#FFE6C7"
FONT_NAME = "Fira Code"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SEC = 60
REPS = 1
check = ""
timer = ""
timer_is_running = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS, timer, check, timer_is_running
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    REPS = 1
    check = ""
    check_text.config(text=check)
    timer_is_running = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS, timer_is_running, check

    if not timer_is_running:
        timer_is_running = True
        if REPS % 2 == 0:
            count_down(SHORT_BREAK_MIN * SEC)
            timer_label.config(text="Short break", fg=C2)
        elif REPS == 8:
            count_down(LONG_BREAK_MIN * SEC)
            timer_label.config(text="Long break", fg=C3)
            timer_is_running = False
        else:
            count_down(WORK_MIN * SEC)
            timer_label.config(text="Work", fg=C4)
            check += "✔"
            check_text.config(text=check)
        REPS += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global check, REPS, timer, timer_is_running
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_is_running = False
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BACKGROUND)

canvas = Canvas(width=200, height=224, bg=BACKGROUND, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill=C4, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", background=C2, highlightthickness=0, fg=C4, font=(FONT_NAME, 12, "bold"),
                      command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", background=C2, highlightthickness=0, fg=C4, font=(FONT_NAME, 12, "bold"),
                      command=reset_timer)
reset_button.grid(column=2, row=2)

timer_label = Label(text="Timer", background=BACKGROUND, highlightthickness=0, fg=C4, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

check_text = Label(background=BACKGROUND, fg=C4, font=(FONT_NAME, 20, "bold"))
check_text.grid(column=1, row=3)

window.mainloop()
