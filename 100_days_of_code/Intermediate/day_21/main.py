from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

#------------ SETUP ---------------
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("DarkBlue")
screen.title("Snake Game")
screen.tracer(0)
still_alive = True
snake = Snake()
food = Food()
score = Score()
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

    if snake.snake_body[0].distance(food) < 15:
        food.spawn()
        score.score_up()
        snake.extend_snake_body()
    
    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -300 or snake.snake_body[0].ycor() > 300 or snake.snake_body[0].ycor() < -280:
        still_alive = False
        score.game_over()
    
    for body_part in snake.snake_body:
        if snake.snake_body.index(body_part) == 0:
            pass
        elif snake.snake_body[0].distance(body_part) < 10:
            still_alive = False
            score.game_over()

screen.exitonclick()