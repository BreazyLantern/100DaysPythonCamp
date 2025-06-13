from turtle import Screen
from paddle import Paddle
import time

#constants
HEIGHT = 600
WIDTH = 800
BACKGROUND_COLOR = "black"

#initialize screen of game
screen = Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
screen.title("Pong")

#create paddle to control
r_paddle = Paddle(350)

#listen for inputs
screen.listen()


game_is_on = True
while game_is_on:
    screen.update()
    # Delay by seconds
    time.sleep(0.1)

    #detect keypress to move paddle
    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")

screen.exitonclick()