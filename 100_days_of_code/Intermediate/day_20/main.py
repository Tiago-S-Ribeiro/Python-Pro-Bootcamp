from turtle import Turtle, Screen
import time
from snake import Snake

#------------ SETUP ---------------
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("DarkBlue")
screen.title("Snake Game")
screen.tracer(0)
still_alive = True
snake = Snake()
screen.listen()
#----------------------------------

screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)

while still_alive:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()