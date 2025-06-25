from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["medium aquamarine", "turquoise", "dodger blue", "gold", "sienna", "blue violet", "red", "pink", "magenta", "green"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.color(random.choice(colors))
        tim.forward(100)
        tim.left(angle)

for num_sides in range(3, 11):
    draw_shape(num_sides)

# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
# for _ in range(8):
#     tim.forward(100)
#     tim.right(45)


screen = Screen()
screen.exitonclick()