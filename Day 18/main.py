from random import choice, randint
import turtle as t
"""draw a square"""
timmy_the_turtle = t.Turtle()

# def draw_line(length, degree):
#     timmy_the_turtle.forward(length)
#     timmy_the_turtle.right(degree)
#

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
# for i in range(4):
#     draw_line(100, 90)

# """Dash lines"""
# for _ in range(4):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

"""Draw polygons in succession of increasing side count"""
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

colors = ["pale green", "yellow", "cornflower blue", "lime", "red", "magenta", "coral",
          "dark orchid", "navy", "blue", "orange red"]

# for shape_side_n in range(3, 11):
#     timmy_the_turtle.color(choice(colors))
#     draw_shape(shape_side_n)

"""Draw random travel directions for the turtle"""
directions = [0, 90, 180, 270]
t.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    c_tuple = (r, g, b)
    return c_tuple

timmy_the_turtle.speed("fastest")

def draw_random_movement(length_of_movement):
    """Draws using the turtle in a random path with thick line in random colors"""
    timmy_the_turtle.pensize(10)
    for _ in range(length_of_movement):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.forward(30)
        timmy_the_turtle.setheading(choice(directions))


def draw_spirograph(size_of_gap):
    """Draws using the turtle in a spirograph pattern using random colors"""
    for _ in range(int(360/ size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(5)
#draw_random_movement(200)


"""about tuples 
tuples are like lists however you cannot modify the tuple once it is first created
this is an immutable set"""

a_tuple = (1, 3, 5)
"""should you need a list from a tuple just use this"""
list(a_tuple)

"""Different way of importing
Try avoiding this since it makes it difficult to identify from where a method or function
come from"""
# from turtle import *
#
# from random import *

# import turtle as t
# tim = t.Turtle()



screen = t.Screen()
screen.exitonclick()