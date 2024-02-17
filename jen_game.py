import random
import game_actions

# Assigned a dictionary of player moves to a variable
original_moves = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

# Printed a string of choices for the player
print(f'Let\'s play Rock, Paper, Scissors!\n\nR - Rock\nP - Paper\nS - Scissors')

# The input function requests a letter from the player and stores it in a variable, player_choice
player_choice = input('\nEnter your letter choice: ').capitalize()

# while the length of the player's choice is not equal to 1 or is a decimal 0-9, execute this code
while len(player_choice) != 1 or player_choice.isdecimal():

    # Requests the player's choice again and reminds them of entering one letter
    player_choice = input('Please enter one letter: ').capitalize()


for index_move, key in enumerate(original_moves.items()):

    moves_list = list(original_moves.items())
    opponent = random.choice(moves_list)

    if player_choice == key[0]:

        print(f'\nYou: {key[1].upper()} vs. Opponent: {opponent[1].upper()}')

        opponent_move = moves_list.index(opponent)

        game_actions.play(index_move, opponent_move)

