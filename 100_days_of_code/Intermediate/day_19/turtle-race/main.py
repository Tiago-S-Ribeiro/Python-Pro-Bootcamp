from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "blue", "orange", "purple"]
y_pos = -50
race_is_on = False
ninja_turtles = []

bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race? Enter a color (red, blue, orange, purple:")

for i in range(4):
  turtle = Turtle(shape="turtle")
  turtle.penup()
  turtle.color(colors[i])
  turtle.goto(x=-225, y=y_pos)
  y_pos += 33
  ninja_turtles.append(turtle)


if bet:
  race_is_on = True

while race_is_on:
    for turtle in ninja_turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= 225:
            race_is_on = False
            if turtle.pencolor() == bet:
                print(f"\n\nYou won your bet, the {turtle.pencolor()} won the race!")
            else:
                print(f"\n\nYou lost your bet, the {turtle.pencolor()} turtle was the winner!")

screen.exitonclick()