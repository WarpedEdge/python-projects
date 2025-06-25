from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=900, height=800)
def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_clockwise():
    tim.right(10)

def rotate_counter_clockwise():
    tim.left(10)

def clear_reset():
    tim.reset()

screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(rotate_clockwise, "d")
screen.onkey(rotate_counter_clockwise, "a")
screen.onkey(clear_reset, "c")

screen.exitonclick()
