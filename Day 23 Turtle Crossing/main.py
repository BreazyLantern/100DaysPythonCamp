import time
from symbol import factor
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#make player
player = Player()

#make cars
car_manager = CarManager()

#make scoreboard
scoreboard = Scoreboard()

#listen for keys
screen.listen()
screen.onkey(player.movement, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect Collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect crossing finish
    if player.is_at_finish_line():
        player.restart_position()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()