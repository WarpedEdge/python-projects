import turtle
import pandas

FONT = 'Arial', 8, 'normal'

# Screen configuration
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=730, height=500)
turtle.shape(image)

# Read CSV data
data = pandas.read_csv("50_states.csv")

# Convert the column into a list
all_states = data.state.to_list()


# loop through game_is_on until "Exit" entered or all 50/50 guessed
game_is_on = True
correct_guesses = 0
correct_states = []
while game_is_on:
    answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # When exiting the game, write to csv the missing states
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_states:
                missing_states.append(state)
                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv("missing_states.csv")
        game_is_on = False
    # If the guess is correct and not already in the correct_states list
    elif answer_state in all_states and answer_state not in correct_states:
        hidden_turtle = turtle.Turtle()
        hidden_turtle.hideturtle()
        hidden_turtle.penup()
        correct_states.append(answer_state)
        state_data = data[data.state == answer_state]
        hidden_turtle.goto(state_data.x.item(), state_data.y.item())
        hidden_turtle.write(arg=answer_state, font=FONT)
        correct_guesses += 1
        print(correct_states)
        # end game at 50 points
        if correct_guesses == 50:
            turtle.write("YOU WIN!", align="center", font=('Arial', 20, 'normal'))
            game_is_on = False
            screen.exitonclick()
    # If guessing same correct state
    elif answer_state in correct_states:
        print("You already guessed that state. Try again")
    else:
        print("Wrong")

