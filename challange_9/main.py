import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Road")
screen.tracer(0)
player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.starter,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    carmanager.creator()
    carmanager.move()
    
    # Detecting collisiontwith the cars
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    # Successfull crossing of the player
    if player.ycor() == 300:
        player.go_to_start()
        carmanager.level_up()
        scoreboard.increase_level()



screen.exitonclick()
