import random

# TODO - create a game of Rock, Paper, Scissors using functions


# TODO - Prompt the user to enter a value: R, P or S AND print Rock for R, Paper for P and Scissors for S:

options = 'R', 'S', 'P'


def user():
    user_input = input("Enter R for Rock, P for Paper or S for Scissors: ").upper()
    while user_input not in options:
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
    computer_input = random.choice(options)
    if computer_input == 'R':
        print("Computer chose: 'Rock'")
    elif computer_input == 'P':
        print("Computer chose: 'Paper'")
    elif computer_input == 'S':
        print("Computer chose: 'Scissors'")
    return computer_input


#  TODO determine the winner of that round

# unlike above functions, this one is not independent
# it requires the input from previous functions to run
# these are passed as placeholder parameters on defining function
# it doesn't matter what they say as long as they are used in the function
# when called - these palceholders will be replaced by the above functions
# it returns 3 scores, these will be needed down the line
# if you don't return them - they will be stuck within the function forever
def win_round(player1, player2, user_score, computer_score, draws):
    if (player1 == 'R' and player2 == 'S') or \
            (player1 == 'P' and player2 == 'R') or \
            (player1 == 'S' and player2 == 'P'):
        user_score += 1
        print("You win!")
    elif player1 == player2:
        draws += 1
        print("It's a tie")
    else:
        computer_score += 1
        print("Computer wins!")
    print(f"You: {user_score}, Computer: {computer_score}, Tied games: {draws}")
    return user_score, computer_score, draws




    # TODO loop the game
# attempted to play the game by importing functions into a function. It did not work
# lots of deleting code but this was one legacy effort
# def play_game():
#   player1 = user()
#   player2 = computer()
#   determine_winner = win_round(player1, player2, user_score, computer_score, draws)



# The 'main' trick
# when function dev runs this FILE, they should see the tests
# when using dev imports this MODULE, they should not see the tests


# if __name__ == "__main__":
#     play_game()

