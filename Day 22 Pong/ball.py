from turtle import Turtle

#constants
MOVE_DISTANCE = 20

class Ball(Turtle):
    """The ball used in the Pong game, will move across the screen in certain directions"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 10
        self.x_move = 10
        #my initialized setup for the ball to go to the upper right
        #self.setheading(45)

    def move(self):
        """move the ball"""
        #my method of forward movement of the ball
        #self.forward(MOVE_DISTANCE)

        #my suggested method of bounce
        # if self.ycor() > 280 or self.ycor() < -280:
        #     self.y_move *= -1
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1