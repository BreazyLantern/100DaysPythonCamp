from symbol import if_stmt

import pandas
import turtle


#states naming project
#!!! Please note that if the state does not align properly with its image it may be due to having this program run on another system
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)


#this line of code is used for finding and adjusting the coordinate position of the state names in the csv
"""def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""
#self attempt for challenge decided not to do this OOP style since I wanted to try and keep this in the main.py

student = 1

if student == 0:
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()

    states_with_coors = pandas.read_csv("50_states.csv")
    correct_guess = []


    while len(correct_guess) < 51:
        title = f"{len(correct_guess)}/50 States Correct"
        answer_state = screen.textinput(title=title, prompt="What's another state's name").title()
        guessed_state = states_with_coors[states_with_coors.state == answer_state]

        if not guessed_state.empty:
            if answer_state not in correct_guess:
                correct_guess.append(answer_state)
                x = guessed_state["x"].item()
                y = guessed_state["y"].item()
                text.goto(x, y)
                text.write(answer_state)
else:
    #Instructor method
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    guessed_states = []
    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another state's name").title()
        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)

screen.exitonclick()