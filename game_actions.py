from getpass import getpass
from random import choice


def choose_move(moves_dictionary):
    # Prints a string about move choices for the player
    print(f'Choose your move\nR - Rock\nP - Paper\nS - Scissors')
    # The input function requests a letter from the player and stores it in variable, player_choice
    player_choice = getpass('\nEnter a letter: ').strip().capitalize()
    # while the letter in player_choice is not in the keys of the original_moves dictionary, execute this code block
    while player_choice not in moves_dictionary.keys():
        # Input function requests the player's choice again with a reminder and reassigns the new value to the variable
        # strip function removes whitespaces before or after the input's string
        # capitalize function converts the first letter of the input's string into a capital letter
        player_choice = getpass('Please enter one letter - r, p, s: ').strip().capitalize()

    return player_choice


def play(moves_dictionary, player_move, opponent_move, player_wins, opponent_wins):

    winning_pairs = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]

    print('\n','~' * 15, 'GAME', '~' * 15, f'\nYou \u25BA {moves_dictionary[player_move].upper()} vs. '
                                      f'{moves_dictionary[opponent_move].upper()} \u25C4 Opponent')

    if player_move == opponent_move:

        print(f'\n\u2666 It\'s a tie! \u2666')

        return player_wins, opponent_wins

    elif (moves_dictionary[player_move].lower(), moves_dictionary[opponent_move].lower()) in winning_pairs:

        print('\nPlayer 1, you win! \u2665 \u2665 \u2665')

        player_wins += 1

        return player_wins, opponent_wins

    else:

        print('\nPlayer 1, you lose!')

        opponent_wins += 1

        return player_wins, opponent_wins


if __name__ == '__main__':

    # Assigns a dictionary of moves to a variable
    original_moves = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

    player = choose_move(original_moves)
    cpu_choice = choice(list(original_moves))

    # play(original_moves, player, cpu_choice)
