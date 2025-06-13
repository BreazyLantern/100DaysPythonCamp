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

    #instructors method of bounce, for me i would have placed this within the ball function, but it makes sense to call the function to bounce here
    #since we also can see the screen width and height values on this file
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect missing with paddle
    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()