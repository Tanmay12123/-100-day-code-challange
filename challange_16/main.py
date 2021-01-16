from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
#............................................................csv reading..........................................................#
try:
    data = pandas.read_csv(
        "C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/words_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv(
        "C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_16/data/french_words.csv")
    to_learn = original.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=my_card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=my_card_back)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


#.........................................................................UI..........................................................#
window = Tk()
# window.config(bg = BACKGROUND_COLOR)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)

my_image_right = PhotoImage(
    file="C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_16/images/right.png")
known_button = Button(image=my_image_right,
                      highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)


my_image_wrong = PhotoImage(
    file="C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_16/images/wrong.png")
unknown_button = Button(image=my_image_wrong,
                        highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)


my_card_front = PhotoImage(
    file="C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_16/images/card_front.png")
my_card_back = PhotoImage(
    file="C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_16/images/card_back.png")
card_background = canvas.create_image(400, 263, image=my_card_front)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(
    400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="Word", font=("Ariel", 60, "bold"))

next_card()
window.mainloop()
