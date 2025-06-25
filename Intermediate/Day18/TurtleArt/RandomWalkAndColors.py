from turtle import Turtle, Screen
import random

tim = Turtle()
Screen().colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

random_color()
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")


for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))




## my first bad attempt
# def random_walk(num_steps):
#     for _ in range(num_steps):
#         tim.color(random.choice(colors))
#         tim.pensize(7)
#         tim.speed(100)
#         tim.forward(15)
#
#
# for num_steps in range(10):
#     random_walk(num_steps)
#     tim.right(90)


screen = Screen()
screen.exitonclick()