import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random as rd

screen = Screen()
screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
level = Scoreboard()

screen.listen() 
screen.onkey(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detecting when the turtle hit the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()
            print("game over")

    # Detecting when the Turtle get to the other side
    if player.ycor() > 280:
        level.level_up()
        player.goto_start()
        car_manager.speed_up()


screen.exitonclick()