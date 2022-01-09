import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
RIGHT_IMG = "./images/true.png"
WRONG_IMG = "./images/false.png"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #Score Label
        self.score_label = tkinter.Label(text="Score: 0", fg="white", bg= THEME_COLOR)
        
        #Canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=FONT, fill=THEME_COLOR)

        #Buttons
        right_image = tkinter.PhotoImage(file = RIGHT_IMG)
        wrong_image = tkinter.PhotoImage(file = WRONG_IMG)
        self.right_btn = tkinter.Button(image=right_image, highlightthickness=0, command=self.choose_true)
        self.wrong_btn = tkinter.Button(image=wrong_image, highlightthickness=0, command=self.choose_false)
        
        #Grid Layout
        self.wrong_btn.grid(row=2, column=1)
        self.right_btn.grid(row=2, column=0)
        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #Invokes the first question
        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text=f"You've finished the quiz with a score of {self.quiz.score}/10.")
    
    def choose_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def choose_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self, answer_is_correct):
        if answer_is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
    