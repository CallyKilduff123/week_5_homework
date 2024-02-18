import failed_functions
import random

user_score = 0
computer_score = 0
draws = 0

while True:
    player1 = failed_functions.user()
    player2 = failed_functions.computer()
    (user_score, computer_score, draws) = failed_functions.win_round(player1, player2, user_score, computer_score, draws)
    repeat_game = input("Would you like to play again? Y/N: ").upper()
    if repeat_game == "Y":
        print("let's go!")
    else:
        print(f"Game over!\n Final score = You: {user_score}, Computer: {computer_score}, Tied games: {draws}")
        break
