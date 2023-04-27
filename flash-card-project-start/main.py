from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
NEW_BACKGROUND_COLOR = "#9FD5B9"
TIMER_SEC = 3
time = None
reps = 0

data = pandas.read_csv("data/french_words.csv")
df = data.to_dict(orient="records")
current_card = {}

def new_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(df)
    origin.config(text="French")
    word.config(text=current_card["French"])
    canvas.itemconfig(card_background, image=flashcard)
    origin.config(text="French", bg="white", fg="black")
    word.config(text=current_card["French"], bg="white", fg="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    origin.config(text="English", bg=NEW_BACKGROUND_COLOR, fg="white")
    word.config(text=current_card["English"], bg=NEW_BACKGROUND_COLOR, fg="white")
    canvas.itemconfig(card_background, image=new_flashcard)


window = Tk()
window.title("Flashy")
window.config(width=1000, height=1000)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=1000, height=1000, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard = PhotoImage(file="images/card_front.png")
new_flashcard = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(500, 300, image=flashcard)
canvas.grid(column=2, row=1, columnspan=2)


right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
right_button = Button(image=right, highlightthickness=0, padx=50, pady=50, command=new_random_word)
wrong_button = Button(image=wrong, highlightthickness=0, padx=50, pady=50, command=new_random_word)
right_button.place(x=700, y=600)
wrong_button.place(x=160, y=600)

origin = Label(text="French", font=("Arial", 40, "italic"), bg="white", fg="black")
origin.place(x=420, y=150)
word = Label(text="", font=("Arial", 60, "bold"), bg="white", fg="black")
word.place(x=400, y=263)


new_random_word()

window.mainloop()
