from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self,quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=25, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR,font = ("Arial", 15, "italic"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,width = 280,
                                                     text="Some Question Quest",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        my_image_right = PhotoImage(
            file="C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_20/images/true.png")
        self.button_right = Button(image=my_image_right, highlightthickness=0)
        self.button_right.grid(row=2, column=0)

        my_image_wrong = PhotoImage(
            file="C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_20/images/false.png")
        self.button_left = Button(
            image=my_image_wrong, highlightthickness=0)
        self.button_left.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()
        
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text = q_text)
        


# QuizInterface(quiz)
