# TODO import all relevant modules
import pprint
import random
from art import logo, vs, bye
from game_data import data

def compare():
    score = 0
    game_active = True
    a_assign = random.choice(data)
    b_assign = random.choice(data)

    while b_assign == a_assign:
        b_assign = random.choice(data)

    while game_active:
        print(logo)
        print(f"Current Score {score}")
        print(f"Compare A: {a_assign["name"]}, a {a_assign["description"]}, from {a_assign["country"]}.")
        print(a_assign["follower_count"])
        print(vs)
        print(f"Compare B: {b_assign["name"]}, a {b_assign["description"]}, from {b_assign["country"]}.")
        print(b_assign["follower_count"])
        user_answer = input("Who has more followers? Type 'A' or 'B'").lower()
        if user_answer == "a" and a_assign["follower_count"] > b_assign["follower_count"] or user_answer == "b" and a_assign["follower_count"] < b_assign["follower_count"]:
            score += 1
            print(f"Correct choice! Your current score: {score}")
            a_assign = b_assign
            b_assign = random.choice(data)
            while b_assign == a_assign:
                b_assign = random.choice(data)
        else:
            print(f"Incorrect choice! Your final score: {score}")
            game_active = False
    play_again = input("Do you want to play again? 'Y' or 'N'? ").lower()
    if play_again == "y":
        compare()
    else:
        print("\n" * 40)
        print(bye)
compare()


