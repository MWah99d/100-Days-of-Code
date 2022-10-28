import random
import turtle

# ## Image and code to extract colors from it ## #

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("Hirst Colours.jpg", 30)
# for color in colors:
#     # r = color.rgb.r
#     # g = color.rgb.g
#     # b = color.rgb.b
#     # new_color = (r, g, b)
#     # rgb_colors.append(new_color)
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(rgb_colors)

# ## ---------------------------------------- ## #

color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]
turtle.colormode(255)
timmy = turtle.Turtle("arrow")
timmy.up()
timmy.speed(0)
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
