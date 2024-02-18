import random

# TODO - create a game of Rock, Paper, Scissors using functions
# define a function (with def)
# identifiers must be 1 word so use _
# can take in arguments via():
# best function names are verbs


# TODO - Prompt the user to enter a value: R, P or S AND print Rock for R, Paper for P and Scissors for S:
def user():
    user_input = input("Enter R for Rock, P for Paper or S for Scissors: ").upper()
    while user_input not in ["R", "P", "S"]:
        print("INVALID ENTRY")
        user_input = input("Enter R for Rock, P for Paper or S for Scissors: ").upper()
    if user_input == 'R':
        print("You chose: 'Rock'")
    elif user_input == 'P':
        print("You chose: 'Paper'")
    elif user_input == 'S':
        print("You chose: 'Scissors'")
    return user_input


# TODO Prompt the computer to generate 0, 1 or 2

def computer():
    computer_input = random.randint(0, 2)
    if computer_input == 0:
        print("Computer chose: 'Rock'")
    elif computer_input == 1:
        print("Computer chose: 'Paper'")
    elif computer_input == 2:
        print("Computer chose: 'Scissors'")
    return computer_input


#  TODO determine the winner of that round
# This is not working as a function - only returns computer wins - it is not reading the answers
# def win_round(user, computer):
#     player1 = user()
#     player2 = computer()
#     print(f"Computer chose: {player2}")
#     if (player1 == 'R' and player2 == '2') or \
#        (player1 == 'P' and player2 == '0') or \
#        (player1 == 'S' and player2 == '1'):
#         print("You win!")
#         winner = player1
#     elif player1 == player2:
#         print("It's a tie")
#         winner = None
#     else:
#         print("Computer wins!")
#         winner = player2
#     return winner

def win_round():
    if (user == 'R' and computer == 2) or \
            (user == 'P' and computer == 0) or \
            (user == 'S' and computer == 1):
        winner = user
        print("You win!")
    elif user == computer:
        winner = None
        print("It's a tie")
    else:
        winner = computer
        print("Computer wins!")
    return winner

# def win_round(user_input, computer_input):
#     if (user_input == 'R' and computer_input == 2) or \
#             (user_input == 'P' and computer_input == 0) or \
#             (user_input == 'S' and computer_input == 1):
#         winner = user_input
#         print("You win!")
#     elif user_input == computer_input:
#         winner = None
#         print("It's a tie")
#     else:
#         winner = computer_input
#         print("Computer wins!")
#     return winner


  # TODO keep score
# def keep_score(winner):
#     user_score = 0
#     computer_score = 0
#     draws = 0
#     if winner == user:
#         user_score += 1
#     if winner == computer:
#         computer_score += 1
#     if winner is None:
#         draws += 1
#     print(f"You: {user_score}, Computer: {computer_score}, Tied games: {draws}")
#     return keep_score

def keep_score():
    user_score = 0
    computer_score = 0
    draws = 0
    if win_round == user:
        user_score += 1
    if win_round == computer:
        computer_score += 1
    if win_round is None:
        draws += 1
    print(f"You: {user_score}, Computer: {computer_score}, Tied games: {draws}")
    return keep_score


    # TODO loop the game
def play_game():
    user()
    computer()
    win_round()
    keep_score()
# def repeat_game(user_score, computer_score, draws):
#     repeat = input("Would you like to play again? Y/N: ").upper()
#     if repeat == "Y":
#         print("let's go!")
#     else:
#         print(f"Game over!\n Final score = You: {user_score}, Computer: {computer_score}, Tied games: {draws}")




# The 'main' trick
# when function dev runs this FILE, they should see the tests
# when using dev imports this MODULE, they should not see the tests

#
if __name__ == "__main__":
    play_game()

