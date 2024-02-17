from getpass import getpass


def choose_move(moves_dictionary):
    # Prints a string about move choices for the player
    print(f'\nChoose your move\nR - Rock\nP - Paper\nS - Scissors')
    # The input function requests a letter from the player and stores it in variable, player_choice
    choice = getpass('\nEnter a letter: ').strip().capitalize()
    # while the letter in player_choice is not in the keys of the original_moves dictionary, execute this code block
    while choice not in moves_dictionary.keys():
        # Input function requests the player's choice again with a reminder and reassigns the new value to the variable
        # strip function removes whitespaces before or after the input's string
        # capitalize function converts the first letter of the input's string into a capital letter
        choice = getpass('Please enter one letter - r, p, s: ').strip().capitalize()

    return choice


def play(moves_dictionary, player_move, opponent_move):

    winning_pairs = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]

    print(f'\nYou \u25BA {moves_dictionary[player_move].upper()} vs. {moves_dictionary[opponent_move].upper()} '
          '\u25C4 Opponent')

    if player_move == opponent_move:

        print(f'\nIt\'s a tie!')

    elif (moves_dictionary[player_move].lower(), moves_dictionary[opponent_move].lower()) in winning_pairs:

        print('\nPlayer 1, you win! \u2665 \u2665 \u2665')

    else:

        print('\nPlayer 1, you lose!')
