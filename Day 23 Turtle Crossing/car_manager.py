import random
from random import randint
from turtle import Turtle


#constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        ran_ycor = randint(-240, 280)
        self.setpos(300, ran_ycor)


    def car_movement(self):
        if self.xcor() < -300:
            self.setx(300)
        self.goto(self.xcor() - MOVE_INCREMENT,self.ycor())
