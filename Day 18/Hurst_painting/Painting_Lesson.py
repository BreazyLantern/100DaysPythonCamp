# import colorgram

# colors = colorgram.extract('Hirst.jpg', 425)

"""Color Extraction code from image file"""
from threading import Timer

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


"""Create a Hirst art piece from jpg colorgrade values using Turtle"""
import turtle as t
import random
import time

t.colormode(255)
tim = t.Turtle()
color_list = [(238, 236, 230), (193, 160, 121), (72, 92, 125), (141, 87, 59), (141, 160, 187), (216, 209, 121), (29, 33, 47), (182, 146, 162), (55, 32, 23), (175, 160, 42), (120, 75, 93), (139, 172, 152), (62, 29, 38), (78, 113, 79), (136, 27, 19), (117, 30, 43), (184, 100, 86), (48, 58, 93), (172, 100, 115), (31, 48, 43), (102, 120, 168), (101, 155, 93), (214, 174, 190), (216, 180, 173), (65, 81, 28), (164, 208, 187), (177, 186, 214), (219, 207, 10), (48, 73, 62), (40, 74, 81), (179, 197, 201), (112, 132, 141)]
tim.speed("fastest")
tim.hideturtle()

t1 = time.time()
tim.penup()

"""My method of creating a Hirst painting"""
# y = -220
# tim.setpos(-220, y)
# for __ in range(10):
#     for _ in range(10):
#         tim.dot(20, random.choice(color_list))
#         tim.forward(50)
#     y += 50
#     tim.setpos(-220, y)
# t2 = time.time()
# print(t2 - t1)



"""Instructors method"""
"""Might be better for optimized big O performance"""
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
i = .8
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50*i)

    if dot_count % (10*i) == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500*i**2)
        tim.setheading(0)
t2 = time.time()
print(t2 - t1)

screen = t.Screen()
screen.exitonclick()