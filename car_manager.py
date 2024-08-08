from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.turtlesize(1 , 2)
        self.penup()
        self.left(180)
        self.color(random.choice(COLORS))
        self.y_start = random.randint(-240, 260)
        self.x_start = 300
        self.goto((self.x_start, self.y_start))

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
        if self.xcor() < -320:
            self.goto(self.x_start, random.randint(-240, 260))

    def speed_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT / 1000

class CarManager:
    def __init__(self):
        self.cars = []

    def create_cars(self):
        random_chance = random.randint(1, 8)
        if random_chance == 1:
            new_car = Car()
            self.cars.append(new_car)

    def speed_up(self):
        for car in self.cars:
            car.speed_up()

        
            

