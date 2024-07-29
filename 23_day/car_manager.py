from turtle import Turtle
import random as rd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = rd.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(rd.choice(COLORS))
            random_y = rd.randint(-250, 250)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)