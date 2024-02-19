# imports the choice function from the random module
from random import choice
# imports game_actions module, custom module
import game_actions

# Prints a string introduction to the game
print(f'Let\'s play Rock, Paper, Scissors!')

# Created dictionaries to track the scores of player1, player 2 and CPU
# Assigned them to three variables
player1_wins = {'Wins': 0, 'Ties': 0, 'Losses': 0}
player2_wins = {'Wins': 0, 'Ties': 0, 'Losses': 0}
cpu_wins = {'Wins': 0, 'Ties': 0, 'Losses': 0}

# Stored 1 integer in play_again variable for the while_loop to track player's 'play again' choice
play_again = 1

# while play_again variable is equal to 1, execute this code
while play_again == 1:

    # choose_opponent() function requests the player to choose their opponent, CPU or Player 2
    # The player's choice, 1 or 2, is assigned to the opponent_selection variable
    opponent_selection = game_actions.choose_opponent()

    # Prints a string indicating the next move is Player 1's choice
    print('\n', '~' * 15, 'Player 1'.upper(), '~' * 15)

    # Assigns a dictionary of moves to original_moves variable
    original_moves = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

    # the choose_move() function requests the player to choose a move rock, paper or scissors
    # It uses the getpass() function to hide the player's choice
    # It stores one letter, R, P or S, in variable, player1
    player1 = game_actions.choose_move(original_moves)

    # if the value in opponent_selection is equal to 1, execute this code.
    if opponent_selection == 1:

        # list function creates a list, storing each key from the dictionary as an item, R, P and S
        # choice function randomly chooses a key item in the list
        # the random choice, R, P or S, is stored in cpu_choice variable
        cpu_choice = choice(list(original_moves))

        # The play function passes 5 arguments when invoked
        # original_moves: a dictionary containing available moves
        # player1: a single letter input representing the Player 1's move
        # cpu_choice: a single letter representing the CPU's move
        # player1_wins: the dictionary scoreboard for Player 1
        # cpu_wins: the dictionary scoreboard for CPU

        # The play function executes a game and returns 2 values, representing the outcome of the game
        # The 2 new values are reassigned to player1_wins and cpu_wins, dictionaries
        player1_wins, cpu_wins = game_actions.play(original_moves, player1, cpu_choice, player1_wins, cpu_wins)

        # Concatenates and prints a string that outlines the number of wins for each player
        print('\n', '~' * 15, 'WINS', '~' * 15,
              f'\nPlayer 1: {player1_wins['Wins']} | Player 2: {player2_wins['Wins']} | CPU: {cpu_wins['Wins']}')

        # the ask_play function takes 3 arguments
        # player_wins: the dictionary scoreboard for Player 1
        # player2_wins: the dictionary scoreboard for Player 2
        # cpu_wins: the dictionary scoreboard for CPU

        # ask_play function provides a string menu to choose whether to play again, view the scoreboard or exit the game
        # it returns one value, 1, and stores it in play_again to continue the while loop and play another game
        # OR it stays in a while loop when viewing the full scoreboard
        # OR it exits the game
        play_again = game_actions.ask_play(player1_wins, player2_wins, cpu_wins)

    # If the opponent_selection variable is equal to 2, execute this code
    else:

        # Prints a string indicating the next move is Player 2's choice
        print('\n', '~' * 15, 'Player 2'.upper(), '~' * 15, )

        # the choose_move() function requests the player to choose a move rock, paper or scissors
        # It uses the getpass() function to hide the player's choice
        # It stores one letter, R, P or S, in variable, player2
        player2 = game_actions.choose_move(original_moves)

        # The play function passes 5 arguments when invoked
        # original_moves: a dictionary containing available moves
        # player1: a single letter input representing the Player 1's move
        # player2: a single letter representing the Player 2's move
        # player1_wins: the dictionary scoreboard for Player 1
        # player2_wins: the dictionary scoreboard for Player 2

        # The play function executes a game and returns 2 values, representing the outcome of the game
        # The 2 new values are reassigned to player1_wins and cpu_wins, dictionaries
        player1_wins, player2_wins = game_actions.play(original_moves, player1, player2, player1_wins, player2_wins)

        # Concatenates and prints a string that outlines the number of wins for each player
        print('\n', '~' * 15, 'WINS', '~' * 15,
              f'\nPlayer 1: {player1_wins['Wins']} | Player 2: {player2_wins['Wins']} | CPU: {cpu_wins['Wins']}')

        # the ask_play function takes 3 arguments
        # player_wins: the dictionary scoreboard for Player 1
        # player2_wins: the dictionary scoreboard for Player 2
        # cpu_wins: the dictionary scoreboard for CPU

        # ask_play function provides a string menu to choose whether to play again, view the scoreboard or exit the game
        # it returns one value, 1, and assigns it to play_again, continuing the while loop and playing another game
        # OR it stays in a while loop when viewing the full scoreboard
        # OR it exits the game
        play_again = game_actions.ask_play(player1_wins, player2_wins, cpu_wins)
