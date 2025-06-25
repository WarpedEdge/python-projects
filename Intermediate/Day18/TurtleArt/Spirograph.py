from turtle import Turtle, Screen
import random

tim = Turtle()
Screen().colormode(255)

def random_color():
    """sets each color to a random from 0-255, assigns to a tuple, then returns that tuple value"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    """Draws a spirograph by dividing 360 by the size of the gap inputted, also making each circle a random color"""
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()