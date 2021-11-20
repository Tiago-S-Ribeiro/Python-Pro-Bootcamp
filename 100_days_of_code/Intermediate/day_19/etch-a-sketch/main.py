from turtle import Turtle, Screen

tt = Turtle()
screen = Screen()

def move_forward():
  tt.forward(10)

def move_backward():
  tt.back(10)

def move_left():
  tt.left(15)
  #tt.setheading(tt.heading() + 15)

def move_right():
  tt.right(15)
  #tt.setheading(tt.heading() - 15)

def clear():
  tt.reset()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()