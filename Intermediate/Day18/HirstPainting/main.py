import random
import colorgram
from turtle import Turtle, Screen

tim = Turtle()
Screen().colormode(255)


color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69),
              (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12),
              (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229),
              (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198),
              (65, 231, 239), (217, 88, 51)]

tim.speed("fastest")
position = 0

def dot_reposition():
    global position
    tim.goto(0, position)
    position += 3

def dot_row():
    for _ in range(10):
        tim.hideturtle()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
    for _ in range(10):
        dot_reposition()

dot_time = 0

while dot_time < 10:
    dot_row()
    dot_time += 1

screen = Screen()
screen.exitonclick()





## testing at first moved to bottom of code##
#colors = colorgram.extract('crappydotpainting.jpg', 30)
# print(colors)
# first_color = colors[0]
# print(first_color)
# rgb = first_color.rgb
# print(f"{rgb} <-- rgb variable")

## extracted the colors and then commented out ##
# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_list.append(new_color)
# print(rgb_list)