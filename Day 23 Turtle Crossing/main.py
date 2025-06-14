import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#make player
player = Player()

#listen for keys
screen.listen()
screen.onkey(player.movement, "Up")

#make cars
cars = []
for _ in range(25):
    cars.append(CarManager())

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.car_movement()

