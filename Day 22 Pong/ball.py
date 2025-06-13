from turtle import Turtle

class Ball(Turtle):
    """The ball used in the Pong game, will move across the screen in certain directions"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.move_speed = .1
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
        """invert the y move distance"""
        self.y_move *= -1
    
    def bounce_x(self):
        """invert the x move distance"""
        self.x_move *= -1
        self.move_speed *=.9
        print(self.move_speed)

    def reset_position(self):
        """reset the ball position and invert the movement direction"""
        self.move_speed = .1
        self.goto(0,0)
        self.bounce_x()