from turtle import Turtle

#Constants
MOVE_DISTANCE = 20

class Paddle:

    def __init__(self, x_cord):

        self.paddle = self.create_paddle(x_cord)


    def create_paddle(self, x_cord):
        new_paddle = Turtle("square")
        new_paddle.color("white")
        new_paddle.penup()
        new_paddle.turtlesize(stretch_wid=5, stretch_len= 1)
        #instructor used what is below, but it achieves the same effect as above
        #new_paddle.shapesize(stretch_wid=5, stretch_len= 1)
        new_paddle.goto(x_cord, 0)
        return new_paddle

    def up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + MOVE_DISTANCE)

    def down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - MOVE_DISTANCE)

