# imports the choice function from the random module
from random import choice
# imports game_actions module
import game_actions

# Prints a string introduction to the game
print(f'Let\'s play Rock, Paper, Scissors!')

opponent_selection = int(input('\nWho do you want to play against?\n\n1. CPU\n2. Player 2\n\nNumber: ').strip())

while opponent_selection not in [1, 2]:

    opponent_selection = int(input('\nChoose number 1 or 2: ').strip())

# Assigns a dictionary of moves to a variable
original_moves = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

print('\n', '~' * 15, 'player 1'.upper(), '~' * 15)

player1 = game_actions.choose_move(original_moves)

# # Prints a string about move choices for the player
# print(f'\nChoose your move\nR - Rock\nP - Paper\nS - Scissors')
#
# # The input function requests a letter from the player and stores it in variable, player_choice
# player_choice = getpass('\nEnter a letter: ').strip().capitalize()


# # while the letter in player_choice is not in the keys of the original_moves dictionary, execute this code block
# while player_choice not in original_moves.keys():
#
#     # Input function requests the player's choice again with a reminder and reassigns the new value to the variable
#     # strip function removes whitespaces before or after the input's string
#     # capitalize function converts the first letter of the input's string into a capital letter
#     player_choice = getpass('Please enter one letter - r, p, s: ').strip().capitalize()

if opponent_selection == 1:
    # items method returns the original_moves dictionary as key-value pairs
    # list function creates a list storing each key-value pair as an item and tuple
    # choice function randomly chooses a key-value tuple in the list and the choice is stored in cpu_choice variable

    cpu_choice = choice(list(original_moves))

    # The play function takes three arguments when invoked:
    # original_moves: a dictionary containing available moves
    # player_choice: a single letter input representing the player's move
    # cpu_choice: a tuple containing a key-value pair representing the CPU's move

    # The play function executes a single game and returns an outcome between the player and opponent
    game_actions.play(original_moves, player1, cpu_choice)

else:

    print('\n', '~' * 15, 'player 2'.upper(), '~' * 15, )

    player2 = game_actions.choose_move(original_moves)

    game_actions.play(original_moves, player1, player2)
