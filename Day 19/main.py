from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    tim.right(10)
def move_back():
    tim.backward(10)
def clear():
    tim.home()
    tim.clear()


"""Task is to create a turtle that will take input keys for movement and drawing on screen
then clear the screen using said inputs"""

screen.listen()             #functions as inputs example
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()