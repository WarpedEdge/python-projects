import random
from art import logo, vs, bye
from game_data import data

def compare():
    score = 0
    game_active = True
    choice_a = random.choice(data)
    choice_b = random.choice(data)

    while choice_b == choice_a:
        choice_b = random.choice(data)

    while game_active:
        print(logo)
        print(f"Current Score {score}")
        print(f"Compare A: {choice_a["name"]}, a {choice_a["description"]}, from {choice_a["country"]}.")
        print(vs)
        print(f"Compare B: {choice_b["name"]}, a {choice_b["description"]}, from {choice_b["country"]}.")
        user_answer = input("Who has more followers? Type 'A' or 'B'").lower()
        if user_answer == "a" and choice_a["follower_count"] > choice_b["follower_count"] or user_answer == "b" and choice_a["follower_count"] < choice_b["follower_count"]:
            score += 1
            print(f"Correct choice! Your current score: {score}")
            choice_a = choice_b
            choice_b = random.choice(data)
            while choice_b == choice_a:
                choice_b = random.choice(data)
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


