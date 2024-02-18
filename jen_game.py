# imports the choice function from the random module
from random import choice
# imports game_actions module
import game_actions

# Prints a string introduction to the game
print(f'Let\'s play Rock, Paper, Scissors!')

player1_wins = 0
cpu_wins = 0
player2_wins = 0
play_again = 'y'

while play_again == 'y':

    opponent_selection = int(input('\nWho do you want to play against?\n\n1. CPU\n2. Player 2\n\nNumber: ').strip())

    while opponent_selection not in [1, 2]:

        opponent_selection = int(input('\nChoose number 1 or 2: ').strip())

    print('\n', '~' * 15, 'player 1'.upper(), '~' * 15)

    # Assigns a dictionary of moves to a variable
    original_moves = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

    player1 = game_actions.choose_move(original_moves)

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
        player1_wins, cpu_wins = game_actions.play(original_moves, player1, cpu_choice, player1_wins, cpu_wins)

        print('\n', '~' * 15, 'WINS', '~' * 15, f'\nPlayer 1: {player1_wins}\nPlayer 2: {player2_wins}\nCPU: {cpu_wins}')

        play_again = input('\nDo you want to play again? Y or N: ').lower()

    else:

        print('\n', '~' * 15, 'player 2'.upper(), '~' * 15, )

        player2 = game_actions.choose_move(original_moves)

        player1_wins, player2_wins = game_actions.play(original_moves, player1, player2, player1_wins, player2_wins)

        print('\n', '~' * 15, 'WINS', '~' * 15,
              f'\nPlayer 1: {player1_wins}\nPlayer 2: {player2_wins}\nCPU: {cpu_wins}')

        play_again = input('\nDo you want to play again? Y or N: ').lower()

