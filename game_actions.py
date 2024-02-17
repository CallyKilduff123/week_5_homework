def play(moves_dictionary, player_move, opponent_move):

    winning_pairs = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]

    print(f'\nYou: {moves_dictionary[player_move].upper()} vs. Opponent: {opponent_move[1].upper()}')

    if player_move == opponent_move[0]:

        print(f'\nIt\'s a tie!')

    elif (moves_dictionary[player_move].lower(), opponent_move[1].lower()) in winning_pairs:

        print('\nYou Win!')

    else:

        print('\nYou lose!')
