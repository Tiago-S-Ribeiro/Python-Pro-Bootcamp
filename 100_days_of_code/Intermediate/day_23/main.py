import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#---------------SETUP----------------
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
game_is_on = True
#------------------------------------

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=player.move)

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.car_list:
        if player.distance(car.position()) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    if player.crossed_the_road():
        player.reset_pos()
        car_manager.level_up()
        scoreboard.level_up()
        

screen.exitonclick()