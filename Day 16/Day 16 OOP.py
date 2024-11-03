# import from outside module
import another_module

# call element from outside module
print(another_module.another_module)


from turtle import Turtle, Screen

# create another object from class
timmy = Turtle()
# print mem location
# print(timmy)

# turtles doc https://docs.python.org/3/library/turtle.html
# change look of timmy object
timmy.shape("turtle")
# change color to ref color on https://cs111.wellesley.edu/reference/colors
timmy.color("DarkGreen")
# move turtle forward
timmy.forward(100)

# create Screen object
my_screen = Screen()

# retrieve attribute from object
print(my_screen.canvheight)

# call on method from class object
my_screen.exitonclick()
