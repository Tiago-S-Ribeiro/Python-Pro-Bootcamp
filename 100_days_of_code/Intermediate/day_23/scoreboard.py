from turtle import Turtle
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.goto(-265, 280)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.write(f"Level: {self.level}", False, align="center", font=FONT)
    
    def level_up(self):
        self.level += 1
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font=FONT)