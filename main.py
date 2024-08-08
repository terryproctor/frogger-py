import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

frogger = Player()

car_man = CarManager()

screen.listen()
screen.onkeypress(frogger.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    car_man.create_cars()
    for car in car_man.cars:
        car.move()
        if frogger.distance(car) < 18:
            game_is_on = False
            scoreboard.game_over()
        if frogger.ycor() > 280:
            frogger.goto(0, -280)
            scoreboard.level_up()
            car_man.speed_up()
    screen.update()

screen.exitonclick()
