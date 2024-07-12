import random
# we know the rule:-- rock > scissors;-- scissors > paper;-- paper > rock
def condition_for_win(user, opponent):      # Checking the conditions if the player win or lose
    if ((user == 'r' and opponent == 's') or
            (user == 's' and opponent == 'p') or
            (user == 'p' and opponent == 'r')):
        return True

def for_printing(user, computer):
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

def play_Rock_Paper_Scissors():
    print()
    print("Welcome to the Rock-Paper-Scissors game. "
          "\nHere are the available options: "
          "\n-- 'r' for rock\n-- 'p' for paper\n-- 's' for scissors")
    user = input("What's your choice? Enter one: ")
    computer = random.choice(['r', 'p', 's'])

    # checking the conditions for user and opponent's choices.
    if user == computer:
        print()
        for_printing(user, computer)
        print("It's a tie.. Please try again.")

    elif condition_for_win(user, computer):
        print()
        for_printing(user, computer)
        print('Congratulations, You win!!...')

    else:
        print()
        for_printing(user, computer)
        print('Bad luck.. You lose')

    again_play()

def again_play():
    print()
    print("Do you want to play again??\nIf yes then enter 'y' and if no then enter 'n'")
    user_again = input('Enter your option: ')
    if user_again == 'y':
        play_Rock_Paper_Scissors()
    elif user_again == 'n':
        print('Thanks for playing. Hope you enjoyed.')
        exit()
    else:
        print()
        print('Invalid input, Please try with right one.')
        again_play()

play_Rock_Paper_Scissors()
