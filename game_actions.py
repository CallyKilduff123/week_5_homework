
def play(player_index, opponent_index):

    if player_index == opponent_index:

        print(f'\nIt\'s a tie!')

    elif player_index == 0 and opponent_index == 2:

        print('\nYou Win!')

    elif player_index == 1 and opponent_index == 0:

        print('\nYou Win!')

    elif player_index == 2 and opponent_index == 1:

        print('\nYou Win!')

    else:
        print('\nYou lose!')


