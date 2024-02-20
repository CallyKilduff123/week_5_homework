# imports exit function from the sys module, it will be called by using exit_game
from sys import exit as exit_game
# imports the getpass function from the getpass module
from getpass import getpass
# imports the choice function from the random module
from random import choice


# ------------------------------------------------------------------------------------------------------------------
# def statement declares a function called choose_opponent with no parameters
def choose_opponent():

    # input function asks the player to choose an opponent and requests their input, 1 or 2
    # strip method removes whitespaces at the beginning and end of the input string
    # the player's choice, a string, is assigned to the opponent_choice variable
    opponent_choice = input('\nWho do you want to play against?\n\n1. CPU\n2. Player 2\n\nChoose a number: ').strip()

    # while the value in opponent_choice is not in this list, execute this code
    # while loop checks if the player input either 1 or 2
    while opponent_choice not in ['1', '2']:

        # input function reminds player to input either 1 or 2
        # strip method removes whitespaces before and after the input string
        # the new value is reassigned to the opponent_choice variable
        opponent_choice = input('\nChoose number 1 or 2: ').strip()

    # At this point, the player has input either 1 or 2
    # int function converts the string in opponent_choice to an integer and stores it in opponent_choice variable
    opponent_choice = int(opponent_choice)

    # return statement returns the value in opponent_choice to be accessed outside this function
    return opponent_choice


# ------------------------------------------------------------------------------------------------------------------
# def statement declares the function choose_move with one parameter, moves_dictionary
def choose_move(moves_dictionary):

    # Prints a string about move choices for the player
    print(f'Choose your move\nR - Rock\nP - Paper\nS - Scissors')

    # getpass function prevents the input of the player being echoed to the console
    # get pass function hides their move choice from other players
    # strip method removes whitespaces before and after the input string
    # capitalize method ensures the 1st letter is uppercase and the new value is stored in player_choice variable
    player_choice = getpass('\nEnter a letter: ').strip().capitalize()

    # while the string in player_choice is not a key in the original_moves dictionary, execute this code
    while player_choice not in moves_dictionary.keys():

        # Input function requests the player's choice again with a reminder and reassigns the new value to the variable
        # strip function removes whitespaces before and after the input's string
        # capitalize function converts the first letter of the input's string into a capital letter
        player_choice = getpass('Please enter one letter - r, p or s: ').strip().capitalize()

    # return statement returns the value in player_choice, either 'R' 'P' or 'S' string
    return player_choice


# ------------------------------------------------------------------------------------------------------------------
# def statement defines the play function with 5 parameters
# moves_dictionary: is expecting a dictionary with key-value pairs like, 'R': 'Rock'
# player_move: is expecting a value like 'R' to represent the player's move choice
# opponent_move: is also expecting a value like 'S' to represent the opponent's move choice
# player_scores: is expecting a dictionary of wins, ties and losses for Player1
# opponent_scores: is expecting a dictionary of wins, ties and losses for the opponent, either CPU or Player2
def play(moves_dictionary, player_move, opponent_move, player_scores, opponent_scores):

    # a list with each item as a tuple is assigned to winning_pairs variable
    # each item defines how player1 would win with the 1st value in the tuple as their choice
    # the 2nd value in the tuple is the opponent's choice and their loss scenario
    winning_pairs = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]

    # prints a string that outlines the move choices of Player1 and their opponent
    # the values in player_move and opponent_move are used as keys to identify the value in the dictionary
    # the value will print the full move's name related to the key - 'P': 'Paper'
    # upper method converts all the characters in the string into uppercase
    print('\n', '~' * 15, 'GAME', '~' * 15, f'\nYou \u25BA {moves_dictionary[player_move].upper()} vs.'
                                            f' {moves_dictionary[opponent_move].upper()} \u25C4 Opponent')

    # if the values in player_move and opponent_move are equal, execute this code
    if player_move == opponent_move:

        # prints a string declaring the game's result was a tie
        print(f'\n\u2666 It\'s a tie! \u2666')

        # 1 is added to the current value of the key 'Ties' in the player_scores' dictionary
        # the updated value is reassigned to player_scores' dictionary
        player_scores['Ties'] += 1

        # 1 is added to the current value of the key 'Ties' in the opponent_scores dictionary
        # the updated value is reassigned to opponent_scores' dictionary
        opponent_scores['Ties'] += 1

        # return statement returns the updated dictionaries, player_scores and opponent_scores
        # these values will be used outside the function
        return player_scores, opponent_scores

    # if the pair of values from player_move key and the opponent_move key (from the moves_dictionary)
    # is also present as a pair of values in the winning pairs list, execute this code
    elif (moves_dictionary[player_move].lower(), moves_dictionary[opponent_move].lower()) in winning_pairs:

        # prints a string declaring Player1 as the winner
        print('\nPlayer 1, you win! \u2665 \u2665 \u2665')

        # 1 is added to the current value of the key 'Wins' in the player_scores' dictionary
        # the updated value is reassigned to player_scores' dictionary
        player_scores['Wins'] += 1

        # 1 is added to the current value of the key 'Losses' in the opponent_scores dictionary
        # the updated value is reassigned to opponent_scores' dictionary
        opponent_scores['Losses'] += 1

        # return statement returns the updated dictionaries, player_scores and opponent_scores
        # these values will be used outside the function
        return player_scores, opponent_scores

    # if player_move and opponent_move are NOT equal and also NOT present in the winning_pairs list, execute this code
    else:

        # prints a string informing Player1 they lose
        print('\nPlayer 1, you lose!')

        # 1 is added to the current value of the key 'Losses' in the player_scores dictionary
        # the updated value is reassigned to player_scores' dictionary
        player_scores['Losses'] += 1

        # 1 is added to the current value of the key 'Wins' in the opponent_scores dictionary
        # the updated value is reassigned to opponent_scores' dictionary
        opponent_scores['Wins'] += 1

        # return statement returns the updated dictionaries, player_scores and opponent_scores
        # these values will be used outside the function
        return player_scores, opponent_scores


# ------------------------------------------------------------------------------------------------------------------
# def statement defines ask_play function with 3 parameters
# player1_score: is expecting a dictionary of wins, ties and losses for Player1
# player2_score: is expecting a dictionary of wins, ties and losses for Player2
# cpu_score: is expecting a dictionary of wins, ties and losses for CPU
def ask_play(player1_score, player2_score, cpu_score):

    # input function requests the player's input to play again, viet full scoreboard or end game
    # strip method removes white space before and after the input string
    # input is assigned to play_again_choice variable
    play_again_choice = input('\nDo you want to...\n1. Play again?\n2. View full Scoreboard\n3. End Game\n\nChoose a '
                              'number: ').strip()

    # while the value in play_again_choice is not in this list, execute this code
    while play_again_choice not in ['1', '2', '3']:

        # input function reminds player to input a number
        # strip method removes white space before and after the input string
        # input is assigned to play_again_choice variable
        play_again_choice = input('\nChoose a number - 1, 2 or 3: ').strip()

    # if play_again_choice is equal to 1, as a string
    if play_again_choice == '1':

        # return statement returns the value of 1, an integer, to be used outside this function
        return 1

    # if play_again_choice is equal to 2, as a string
    elif play_again_choice == '2':

        # The while True loop creates an infinite loop to execute this block of code
        # It will continue until exited by a statement like break or return or the exit_game function
        while True:
            # print function prints title strings and the values of the dictionaries from each player
            # format method presents 7s strings and 7 digits, left justified < with spaces
            # if there are not enough characters or digits to fill the 7, whitespaces take their place
            print('\n{:7s} {:7s} {:7s} {:7s}'.format(' ' * 7, 'Player1', 'Player2', 'CPU'))
            print('{:7s} {:7s} {:7s} {:7s}'.format(' ' * 7, '-' * 7, '-' * 7, '-' * 7))
            print('{:7s} {:<7} {:<7} {:<7}'.format('Wins', player1_score['Wins'], player2_score['Wins'], cpu_score['Wins']))
            print('{:7s} {:<7} {:<7} {:<7}'.format('Ties', player1_score['Ties'], player2_score['Ties'], cpu_score['Ties']))
            print('{:7s} {:<7} {:<7} {:<7}'.format('Losses', player1_score['Losses'], player2_score['Losses'],
                                                   cpu_score['Losses']))

            # input function requests the player's input to play again, viet full scoreboard or end game
            # strip method removes white space before and after the input string
            # input is assigned to play_again_choice variable
            play_again_choice = input('\nDo you want to...\n1. Play again?\n2. View full Scoreboard\n3. End '
                                      'Game\n\nChoose a number: ')

            # while the value in play_again_choice is not in this list, execute this code
            while play_again_choice not in ['1', '2', '3']:

                # input function reminds player to input a number
                # strip method removes white space before and after the input string
                # input is assigned to play_again_choice variable
                play_again_choice = input('\nChoose a number - 1, 2 or 3: ').strip()

            # if play_again_choice is equal to 1, as a string
            if play_again_choice == '1':

                # return statement returns the value of 1, an integer, to be used outside this function
                return 1

            # if play_again_choice is equal to 3, as a string
            elif play_again_choice == '3':

                # exit function is being called exit_game
                # prints a string with thanks and terminates the program immediately
                exit_game('\nThanks for playing!')

    # if play_again_choice is equal to 3, as a string
    elif play_again_choice == '3':

        # exit function is being called exit_game
        # prints a string with thanks and terminates the program immediately
        exit_game('\nThanks for playing!')


# if script is being run as the main program, directly executed
# then variable __name__ is equal to '__main__'
# the code inside this if block will only execute if it is being directly execute and NOT executed as a module
# executed as a module, __name__ variable would equal to game_actions, the module name
if __name__ == '__main__':

    # scoreboard dictionaries
    player1_wins = {'Wins': 0, 'Ties': 0, 'Losses': 0}
    player2_wins = {'Wins': 0, 'Ties': 0, 'Losses': 0}
    cpu_wins = {'Wins': 0, 'Ties': 0, 'Losses': 0}

    # TEST 1 - Choose an opponent
    opponent = choose_opponent()
    print(opponent)

    # TEST 2 - Choose a move
    original_moves = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    player = choose_move(original_moves)
    print(player)

    # TEST 3 - Play a game
    cpu = choice(list(original_moves))
    player1_wins, cpu_wins = play(original_moves, player, cpu, player1_wins, cpu_wins)
    print(player1_wins, cpu_wins)

    # TEST 4 - Play again, view scoreboard or exit
    play_again = ask_play(player1_wins, player2_wins, cpu_wins)
    print(play_again)
