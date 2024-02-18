import random

# TODO - Prompt the user to enter a value: R, P or S:
user_score = 0
computer_score = 0
draws = 0

print("Welcome to the world's best game of Rock, Paper, Scissors!\nYou know the rules so let's get playing!\n")
    # use input function to ask user to input R P or S
    # use uppercase method to capitalise
while True:
    user_input = input("Enter R for Rock, P for Paper or S for Scissors: ").upper()
    # use while loop to keep asking until valid response given
    # could use != but more efficient to use 'not in' as checking against multiple values
    # 'not in' used to check if a value is not present in a collection.
    # combination of the not (inverts boolean) and in (checks collection) operators
    while user_input not in ["R", "P", "S"]:
        print("INVALID ENTRY")
        user_input = input("Enter R for Rock, P for Paper or S for Scissors: ").upper()
    # print(user_input)


    # TODO print Rock for R, Paper for P and Scissors for S

    if user_input == 'R':
        print("You chose: 'Rock'")
    elif user_input == 'P':
        print("You chose: 'Paper'")
    elif user_input == 'S':
        print("You chose: 'Scissors'")


    # TODO Prompt the computer to generate 0,1 or 2

    computer_input = random.randint(0, 2)
    # computer_input = random.sample(range(0, 2), 1)
    if computer_input == 0:
        print("Computer chose: 'Rock'")
    elif computer_input == 1:
        print("Computer chose: 'Paper'")
    elif computer_input == 2:
        print("Computer chose: 'Scissors'")


    #  TODO determine the winner of that round

    if user_input == 'R' and computer_input == 2 or user_input == 'P' and computer_input == 0 or user_input == 'S' and computer_input == 1:
        winner = user_input
        print("You win!")
    elif user_input == computer_input:
        winner = None
        print("It's a tie")
    else:
        winner = computer_input
        print("Computer wins!")


    # TODO keep score

    # user_score = 0
    # computer_score = 0
    # draws = 0

    if winner == user_input:
        user_score += 1
    if winner == computer_input:
        computer_score += 1
    if winner is None:
        draws += 1

    # score = user_score, computer_score, draws
    print(f"You: {user_score}, Computer: {computer_score}, Tied games: {draws}")


    # TODO loop the game

    repeat_game = input("Would you like to play again? Y/N: ").upper()
    if repeat_game == "Y":
        print("let's go!")
    else:
        print(f"Game over!\n Final score = You: {user_score}, Computer: {computer_score}, Tied games: {draws}")
        break








