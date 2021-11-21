from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_body = self.create_snake()
    
    def create_snake(self):
        snake_body = []
        for i in range(3):
            body_part = Turtle(shape="square")
            body_part.color("beige")
            body_part.penup()
            body_part.goto(x=i*-20, y=0)
            snake_body.append(body_part)
        return snake_body
    
    def move(self):
        for i in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i-1].position())
        self.snake_body[0].forward(20)
    
    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)
    
    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)