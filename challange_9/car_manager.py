from typing import Generator
import random
from turtle import Turtle,Screen

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def creator(self):
        random_num = random.randint(1,6)
        if random_num == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250,250)
            new_car.goto(300,new_y)
            self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed += 5
        for car in self.all_cars:
            car.backward(self.car_speed)