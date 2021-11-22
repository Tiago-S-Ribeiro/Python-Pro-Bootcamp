from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

#------------ SETUP ---------------
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("DarkBlue")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)
game_is_on = True
score = Score()
#----------------------------------

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
screen.tracer(1)
ball = Ball()

screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)

while game_is_on:
    screen.update()
    ball.move()
    
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    if (ball.xcor() > 320 and ball.distance(right_paddle) < 50) or (ball.xcor() < -320 and ball.distance(left_paddle) < 50):
        ball.paddle_hit()
    if ball.xcor() > 380:
        screen.tracer(0)
        ball.reset_pos()
        score.score_up("left")
    if ball.xcor() < -380:
        screen.tracer(0)
        ball.reset_pos()
        score.score_up("right")
    screen.tracer(1)



screen.exitonclick()