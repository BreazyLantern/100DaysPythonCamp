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
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

#listen for inputs
screen.listen()


game_is_on = True
while game_is_on:
    screen.update()

    #detect keypress to move paddle
    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")
    screen.onkey(l_paddle.up, "w")
    screen.onkey(l_paddle.down, "s")


screen.exitonclick()