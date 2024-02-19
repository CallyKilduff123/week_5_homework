import failed_functions

# initiate scores outside of the loop
# in the loop, call on functions and store in variables
# e.g. player1 returns the output from user (R,P or S)
# user score, computer score and draws is stored as a tuple

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
        print(f"Game over!\nFinal score = You: {user_score}, Computer: {computer_score}, Tied games: {draws}")
        break
