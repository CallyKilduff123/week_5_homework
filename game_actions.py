from sys import exit as exit_game
from getpass import getpass
from random import choice


def choose_opponent():

    opponent_choice = input('\nWho do you want to play against?\n\n1. CPU\n2. Player 2\n\nChoose a number: ').strip()

    while opponent_choice not in ['1', '2']:

        opponent_choice = input('\nChoose number 1 or 2: ').strip()

    opponent_choice = int(opponent_choice)

    return opponent_choice


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
        player_choice = getpass('Please enter one letter - r, p or s: ').strip().capitalize()

    return player_choice


def play(moves_dictionary, player_move, opponent_move, player_scores, opponent_scores):

    winning_pairs = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]

    print('\n', '~' * 15, 'GAME', '~' * 15, f'\nYou \u25BA {moves_dictionary[player_move].upper()} vs.'
                                            f' {moves_dictionary[opponent_move].upper()} \u25C4 Opponent')

    if player_move == opponent_move:

        print(f'\n\u2666 It\'s a tie! \u2666')

        player_scores['Ties'] += 1
        opponent_scores['Ties'] += 1
        return player_scores, opponent_scores

    elif (moves_dictionary[player_move].lower(), moves_dictionary[opponent_move].lower()) in winning_pairs:

        print('\nPlayer 1, you win! \u2665 \u2665 \u2665')

        player_scores['Wins'] += 1
        opponent_scores['Losses'] += 1
        return player_scores, opponent_scores

    else:

        print('\nPlayer 1, you lose!')

        player_scores['Losses'] += 1
        opponent_scores['Wins'] += 1

        return player_scores, opponent_scores


def ask_play(player1_score, player2_score, cpu_score):

    play_again_choice = input('\nDo you want to...\n1. Play again?\n2. View full Scoreboard\n3. End Game\n\nChoose a '
                              'number: ')

    while play_again_choice not in ['1', '2', '3']:

        play_again_choice = input('\nChoose a number - 1, 2 or 3: ')

    if play_again_choice == '1':

        return 1

    elif play_again_choice == '2':
        while True:
            print('\n{:7s} {:7s} {:7s} {:7s}'.format(' ' * 7, 'Player1', 'Player2', 'CPU'))
            print('{:7s} {:7s} {:7s} {:7s}'.format(' ' * 7, '-' * 7, '-' * 7, '-' * 7))
            print('{:7s} {:<7} {:<7} {:<7}'.format('Wins', player1_score['Wins'], player2_score['Wins'], cpu_score['Wins']))
            print('{:7s} {:<7} {:<7} {:<7}'.format('Ties', player1_score['Ties'], player2_score['Ties'], cpu_score['Ties']))
            print('{:7s} {:<7} {:<7} {:<7}'.format('Losses', player1_score['Losses'], player2_score['Losses'],
                                                   cpu_score['Losses']))

            play_again_choice = input('\nDo you want to...\n1. Play again?\n2. View full Scoreboard\n3. End '
                                      'Game\n\nChoose a number: ')

            while play_again_choice not in ['1', '2', '3']:

                play_again_choice = input('\nChoose a number - 1, 2 or 3: ')

            if play_again_choice == '1':

                return 1

            elif play_again_choice == '3':

                exit_game('\nThanks for playing!')

    elif play_again_choice == '3':

        exit_game('\nThanks for playing!')


if __name__ == '__main__':

    # Assigns a dictionary of moves to a variable
    original_moves = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

    player = choose_move(original_moves)
    cpu_choice = choice(list(original_moves))

    # play(original_moves, player, cpu_choice)
