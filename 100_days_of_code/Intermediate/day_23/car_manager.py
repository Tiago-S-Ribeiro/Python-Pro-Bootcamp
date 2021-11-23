from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        probability = random.randint(0, 5)
        if probability == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.car_list.append(new_car)
    
    def move_cars(self):
        for car in self.car_list:
            car.backward(self.speed)
    
    def level_up(self):
        self.speed += MOVE_INCREMENT