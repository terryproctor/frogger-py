import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

frogger = Player()

# new_car = Car()
car_man = CarManager()


screen.listen()
screen.onkeypress(frogger.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    car_man.create_cars()
    for car in car_man.cars:
        car.move()
        if frogger.distance(car) < 20:
            game_is_on = False
            scoreboard = Scoreboard()
            #scoreboard.game_over()
    screen.update()

screen.exitonclick()
