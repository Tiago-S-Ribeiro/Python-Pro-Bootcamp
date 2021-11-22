from turtle import Turtle
FONT = ("Arial", 16, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_points = 0
        self.right_points = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 275)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.write(f"{self.left_points}    |    {self.right_points}", False, align="center", font=FONT)
    
    def score_up(self, player):
        if player == "right":
            self.right_points += 1
        elif player == "left":
            self.left_points += 1
        self.clear()
        self.update_score()