from turtle import Screen
from paddle import Paddle
from ball import Ball
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

#create ball
ball = Ball()

#listen for inputs
screen.listen()

#detect keypress to move paddle
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()




screen.exitonclick()