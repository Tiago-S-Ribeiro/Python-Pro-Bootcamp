import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
RIGHT_IMG = "./images/right.png"
WRONG_IMG = "./images/wrong.png"
CARD_FRONT = "./images/card_front.png"
CARD_BACK = "./images/card_back.png"
FONT = ("Roboto", 40, "italic")
FONT_II = ("Roboto", 60, "bold")
BLACK = "#000000"
WHITE="#FFFFFF"
chosen_combo = {}

# ------------------------------------------------------------------ #
def right_answer():
  data_dict.remove(chosen_combo)
  pandas.DataFrame(data_dict).to_csv("./data/words_to_learn.csv", index=False)
  random_word()
  
def random_word():
  global chosen_combo, flip_timer
  
  window.after_cancel(flip_timer)
  chosen_combo = random.choice(data_dict)
  
  canvas.itemconfig(language, text="French", fill=BLACK)
  canvas.itemconfig(translation, text=chosen_combo["French"], fill=BLACK)
  canvas.itemconfig(card_bg, image=card_front_img)
  
  flip_timer = window.after(3000, func=flip_card)

def flip_card():
  global chosen_combo
  
  canvas.itemconfig(language, text="English", fill=WHITE)
  canvas.itemconfig(translation, text=chosen_combo["English"], fill=WHITE)
  canvas.itemconfig(card_bg, image=card_back_img)

# ---------------------------- CSV DATA ------------------------------- #
try:
  data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
  data = pandas.read_csv("./data/french_words.csv")
finally:  
  data_dict = data.to_dict(orient="records")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flash Cards")
window.minsize(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#Images
card_front_img = tkinter.PhotoImage(file=CARD_FRONT)
card_back_img = tkinter.PhotoImage(file=CARD_BACK)
right = tkinter.PhotoImage(file=RIGHT_IMG)
wrong = tkinter.PhotoImage(file=WRONG_IMG)

#Canvas
canvas = tkinter.Canvas(width=800, height=526)
card_bg = canvas.create_image(400, 263, image=card_front_img)
language = canvas.create_text(400, 150, text="French", font=FONT, fill=BLACK)
translation = canvas.create_text(400, 263, text="", font=FONT_II, fill=BLACK)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

#Buttons
right_btn = tkinter.Button(image=right, highlightthickness=0, command=right_answer)
wrong_btn = tkinter.Button(image=wrong, highlightthickness=0, command=random_word)

#Grid
canvas.grid(row=0, column=0, columnspan=2)
wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)

random_word()
window.mainloop()