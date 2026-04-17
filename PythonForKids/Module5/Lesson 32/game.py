# This game is a simple Dice Battle game made using Python. Each player rolls two dice, and their total score is calculated. The + operator is overloaded so that two dice objects can be added directly to get the total score. The player with the higher total wins the game, and if both scores are equal, it is a tie.

import random

# Create Dice class
class Dice:

    # Constructor to generate random dice value
    def __init__(self):
        self.value = random.randint(1, 6)

    # Overload + operator to add two dice values
    def __add__(self, other):
        return self.value + other.value


choice = 1   # Variable to control loop

# Loop to allow replaying the game
while choice == 1:

    # Create dice for Player 1
    d1 = Dice()
    d2 = Dice()

    # Create dice for Player 2
    d3 = Dice()
    d4 = Dice()

    # Calculate scores using overloaded + operator
    player1_score = d1 + d2
    player2_score = d3 + d4

    # Display dice values
    print("\nPlayer 1 dice:", d1.value, d2.value)
    print("Player 2 dice:", d3.value, d4.value)

    # Display total scores
    print("Player 1 total:", player1_score)
    print("Player 2 total:", player2_score)

    # Decide winner
    if player1_score > player2_score:
        print("Player 1 Wins!")
    elif player2_score > player1_score:
        print("Player 2 Wins!")
    else:
        print("It's a Tie!")

    # Ask user to replay
    choice = int(input("\nEnter 1 to play again or 0 to exit: "))

print("Game Over!")