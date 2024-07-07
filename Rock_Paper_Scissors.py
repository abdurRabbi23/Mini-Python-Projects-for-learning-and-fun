import random


# we know the rule:-- rock > scissors;-- scissors > paper;-- paper > rock
def condition_for_win(user, opponent):      # Checking the conditions if the player win or lose
    if ((user == 'r' and opponent == 's') or
            (user == 's' and opponent == 'p') or
            (user == 'p' and opponent == 'r')):
        return True


def play_Rock_Paper_Scissors():
    print("Welcome to the Rock-Paper-Scissors game. "
          "\nHere are the available options: "
          "\n-- 'r' for rock\n-- 'p' for paper\n-- 's' for scissors")
    user = input("What's your choice? Enter one: ")
    computer = random.choice(['r', 'p', 's'])

    # checking the conditions for user and opponent's choices.
    if user == computer:
        print()
        if user == 'r':
            print("Your choice is: 'Rock'")
        elif user == 'p':
            print("Your choice is: 'Paper'")
        elif user == 's':
            print("Your choice is: 'Scissors'")

        if computer == 'r':
            print("The opponent's choice is: 'Rock'")
        elif computer == 'p':
            print("The opponent's choice is: 'Paper'")
        elif computer == 's':
            print("The opponent's choice is: 'Scissors'")

        print("It's a tie.. Please try again.")

    elif condition_for_win(user, computer):
        print()
        if user == 'r':
            print("Your choice is: 'Rock'")
        elif user == 'p':
            print("Your choice is: 'Paper'")
        elif user == 's':
            print("Your choice is: 'Scissors'")

        if computer == 'r':
            print("The opponent's choice is: 'Rock'")
        elif computer == 'p':
            print("The opponent's choice is: 'Paper'")
        elif computer == 's':
            print("The opponent's choice is: 'Scissors'")

        print('Congratulations, You win!!...')
    else:
        print()
        if user == 'r':
            print("Your choice is: 'Rock'")
        elif user == 'p':
            print("Your choice is: 'Paper'")
        elif user == 's':
            print("Your choice is: 'Scissors'")

        if computer == 'r':
            print("The opponent's choice is: 'Rock'")
        elif computer == 'p':
            print("The opponent's choice is: 'Paper'")
        elif computer == 's':
            print("The opponent's choice is: 'Scissors'")

        print('Bad luck.. You lose')


play_Rock_Paper_Scissors()