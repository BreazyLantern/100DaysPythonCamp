import random
import turtle
from symbol import return_stmt
from turtle import Turtle, Screen



# joe = Turtle()
# joe.color("red")
#
# bill = Turtle()
# bill.color("blue")
#
# rick = Turtle()
# rick.color("purple")
#
# sam = Turtle()
# sam.color("yellow")
#
# paul = Turtle()
# paul.color("orange")

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")

y_pos = [-70, -40, -10, 20, 50, 80]
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtle.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        ran_distance = random.randint(0, 10)
        turtle.forward(ran_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner")
            #saw that there can be two winners.
            break




screen.exitonclick()