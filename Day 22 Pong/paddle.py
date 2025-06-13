from turtle import Turtle

#Constants
XCOORD = 350
STARTING_POSITIONS = (XCOORD, 0)
MOVE_DISTANCE = 20

class Paddle:

    def __init__(self):
        self.paddle = self.create_paddle()


    def create_paddle(self):
        new_paddle = Turtle("square")
        new_paddle.color("white")
        new_paddle.penup()
        new_paddle.turtlesize(stretch_wid=5, stretch_len= 1)
        #instructor used what is below, but it achieves the same effect as above
        #new_paddle.shapesize(stretch_wid=5, stretch_len= 1)
        new_paddle.goto(STARTING_POSITIONS)
        return new_paddle

    def up(self):
        self.paddle.goto(XCOORD, self.paddle.ycor() + MOVE_DISTANCE)

    def down(self):
        self.paddle.goto(XCOORD, self.paddle.ycor() - MOVE_DISTANCE)

