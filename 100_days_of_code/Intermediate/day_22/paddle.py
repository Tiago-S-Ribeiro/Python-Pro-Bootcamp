from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.goto(x, y)
    
    def up(self):
        self.goto(self.xcor(), self.ycor() + 30)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 30)