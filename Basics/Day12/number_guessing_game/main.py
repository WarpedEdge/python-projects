from art import logo
from random import randint

def guessing_game():
    play_again = True
    difficulty = ""
    guesses = 0
    while play_again:
        play_game = input("Do you want to play the Guessing Game? Type 'yes' or 'no'.\n").lower()
        if play_game == "no":
            play_again = False
            return
        print(logo)
        mode_select = input("What difficulty do you want to play on? 'easy' gives 10 guesses while 'hard' gives 5.\n")
        if mode_select == "easy":
            guesses = 10
        else:
            guesses = 5
        random_number = random.randint(1, 100)
        while guesses > 0:
            #print(f"psst the number is {random_number}.")
            player_guess = int(input(f"You have {guesses} guesses. Choose a number between 1-100.\n"))
            if player_guess == random_number:
                guesses = 0
                print("You guessed correct! You win!")
            elif player_guess < random_number:
                guesses -= 1
                print(f"Too low. You have {guesses} guesses left.")
            elif player_guess > random_number:
                guesses -= 1
                print(f"Too high. You have {guesses} guesses left.")
        print("Game has ended.")
guessing_game()