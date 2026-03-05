import random
from colorama import init, Fore, Style
init(autoreset=True)

choices = ['rock', 'paper', 'scissors']


def display_choices():
    print(Fore.CYAN + "\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors\n")


def player_move():
    move = ''
    while move not in ['1', '2', '3']:
        move = input(Fore.GREEN + "Enter your choice (1-3): " + Style.RESET_ALL)

        if move not in ['1', '2', '3']:
            print(Fore.RED + "Invalid choice! Please select 1, 2, or 3.")

    return choices[int(move) - 1]


def ai_move():
    return random.choice(choices)


def check_winner(player, ai):
    if player == ai:
        return "Tie"
    elif (player == 'rock' and ai == 'scissors') or \
         (player == 'paper' and ai == 'rock') or \
         (player == 'scissors' and ai == 'paper'):
        return "Player"
    else:
        return "AI"


def rock_paper_scissors():
    print(Fore.YELLOW + "Welcome to Rock-Paper-Scissors!")

    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)

    while True:
        display_choices()

        player = player_move()
        ai = ai_move()

        print(Fore.BLUE + f"\n{player_name} chose: {player}")
        print(Fore.MAGENTA + f"AI chose: {ai}")

        result = check_winner(player, ai)

        if result == "Tie":
            print(Fore.YELLOW + "It's a tie!")
        elif result == "Player":
            print(Fore.GREEN + f"Congratulations {player_name}, you won!")
        else:
            print(Fore.RED + "AI wins!")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again != 'yes':
            print(Fore.CYAN + "Thanks for playing!")
            break


if __name__ == "__main__":
    rock_paper_scissors()