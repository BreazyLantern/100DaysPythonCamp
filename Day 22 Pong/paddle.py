from turtle import Turtle

#Constants
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        # instructor used what is below, but it achieves the same effect as above
        # self.shapesize(stretch_wid=5, stretch_len= 1)
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

