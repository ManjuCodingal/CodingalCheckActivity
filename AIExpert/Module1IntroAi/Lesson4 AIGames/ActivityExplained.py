import random # This module provides functions for generating random numbers, selecting random items. Here can be used for AI move selection
from colorama import init, Fore, Style # colorama allows us to print colored text in the terminal. We will use it to differentiate player and AI moves visually. 
# Init: initializes colorama, and autoreset=True means that after each print statement, the color will reset to default, so we don't have to manually reset it every time.
# Fore: contains constants for foreground colors (e.g., Fore.RED, Fore.BLUE); used to color text.
# Style: contains constants for text styles (e.g., Style.RESET_ALL); used to reset text formatting after coloring.
init(autoreset=True)

def display_board(board): # Displaying board function prints the current state of the tic-tac-toe board. It uses colorama to color the X's and O's differently for better visual distinction.
    print() # For spacing and readability; This prints a blank line before the board. To separate the board from 'Player X turn: 1' text.

    # The colored function is defined inside display_board to color each cell based on its content (X, O, or empty). The board is printed in a 3x3 grid format with colored symbols.
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else: # for empty cells (which are still digits), we can color them yellow to indicate they are available spots.
            return Fore.YELLOW + cell + Style.RESET_ALL
    # Board layout: The board is a list of 9 elements representing the 3x3 grid. Each cell is printed with its corresponding color based on whether it contains 'X', 'O', or a digit (indicating an empty spot). The grid lines (Vertical bars '|' and horizontal dividers '---+---+---') are colored cyan for better visibility.    
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']: # The while loop continues until the player inputs a valid symbol (X or O). The input is converted to uppercase to ensure it matches the expected format.
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()
    if symbol == 'X':
        return ('X', 'O') # If the player chooses 'X', they will be 'X' and the AI will be 'O'. Otherwise, if the player chooses 'O', they will be 'O' and the AI will be 'X'. This function returns a tuple eg.('X','O')containing the player's symbol and the AI's symbol based on the player's choice.
    # AI gets the opposite symbol of the player's choice. If player chooses 'X', AI gets 'O', and if player chooses 'O', AI gets 'X'.
    else:
        return ('O', 'X')

def player_move(board, symbol): # Handling players move: This function prompts the player to enter their move (a number between 1 and 9 corresponding to the board positions). It validates the input to ensure it's a valid move (i.e., the chosen cell is not already occupied) and updates the board with the player's symbol.
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        # [move - 1] is indexing in terms of the board list, which is zero-indexed. The player inputs a number from 1 to 9, but the board list is indexed from 0 to 8. So, we subtract 1 from the player's input to get the correct index for the board list.

        # board[move - 1] checks the content of the chosen cell. If it's still a digit, it means that cell is empty and available for a move. If it's not a digit (i.e., it contains 'X' or 'O'), it means that cell is already occupied, and the player must choose another move.
        try:
            move = int(input("Enter your move (1-9): "))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")
    board[move - 1] = symbol # Once a valid move is entered, the board is updated with the player's symbol at the chosen position (adjusting for zero-based indexing by subtracting 1 from the move).

def ai_move(board, ai_symbol, player_symbol): # Ai move logic
    for i in range(9): # iterates over all positions
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol # Simulates placing the AI's symbol in the current position (i) on a copy of the board. This allows the AI to check if this move would result in a win without modifying the actual game board.
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
    for i in range(9): # If no winning move is found, the AI checks if the player has a winning move in the next turn. It simulates the player's move in each empty spot and checks if it would result in a win for the player. If it finds such a move, it places its own symbol there to block the player from winning.
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return
    possible_moves = [i for i in range(9) if board[i].isdigit()] # If neither a winning move nor a blocking move is found, the AI selects a random available spot on the board and places its symbol there. 
    move = random.choice(possible_moves) # possible_moves is a list of indices for all empty spots on the board (where the board still contains digits). random.choice(possible_moves) selects one of those indices randomly for the AI's move.
    board[move] = ai_symbol # The AI places its symbol in the randomly chosen empty spot on the board.

def check_win(board, symbol): # Checking for win conditions: This function checks if the given symbol (either player's or AI's) has won the game by checking all possible winning combinations (rows, columns, diagonals). It returns True if a win condition is met, otherwise False.
    win_conditions = [ # The win_conditions list contains tuples of indices that represent the winning combinations on the tic-tac-toe board. Each tuple corresponds to a row, column, or diagonal where three of the same symbols (X or O) would indicate a win.
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical
        (0, 4, 8), (2, 4, 6) # Diagonal
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol: # This checks if the three positions specified in the current win condition (cond) all contain the same symbol. If they do, it means that symbol has won the game, and the function returns True. If none of the win conditions are met after checking all of them, the function returns False, indicating that there is no winner yet.
            return True # if winning condition is met, return True
    return False # no winning condition met, return False

def check_full(board): # Check if board is full, ie no remaing moves
    return all(not spot.isdigit() for spot in board) # all() checks if all elements in the board list satisfy the condition that they are not digits. If all spots on the board are filled with 'X' or 'O' (i.e., no digits remain), it returns True, indicating that the board is full. If there is at least one digit (indicating an empty spot), it returns False.

def tic_tac_toe(): # Main game loop: This function manages the overall flow of the tic-tac-toe game. It initializes the game board, handles player and AI turns, checks for win conditions after each move, and prompts the player to play again after a game concludes.
    print("Welcome to Tic-Tac-Toe!")
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    while True:
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # The board is initialized as a list of strings representing the numbers 1 to 9, which correspond to the positions on the tic-tac-toe grid. This allows players to choose their move by entering the number of the desired cell.
        player_symbol, ai_symbol = player_choice() #  player_choice() determine symbols for player and AI
        turn = 'Player' # player always goes first, so we set turn to 'Player' at the start of each game. The game loop will alternate turns between the player and the AI until a win condition is met or the board is full (resulting in a tie).
        game_on = True # game_on is a boolean variable that controls the main game loop. It is set to True at the start of each game, allowing the loop to run. When a win condition is met or the board is full, game_on is set to False, which breaks the loop and ends the current game. After the game concludes, the player is prompted to play again, and if they choose not to, the program will exit.

        while game_on:
            display_board(board) # current state of the board is displayed at the beginning of each turn, allowing the player to see the updated board after each move. This helps the player make informed decisions about their next move based on the current game state.
            if turn == 'Player':
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print("Congratulations! " + player_name + ", you have won the game!")
                    game_on = False
                else:
                    if check_full(board): # If the board is full after the player's move and there is no winner, it means the game is a tie. The board is displayed one last time to show the final state, and a message indicating that it's a tie is printed. The game loop is then broken to end the current game.
                        display_board(board)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'AI'
            else:
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print("AI has won the game!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'Player'
        play_again = input("Do you want to play again? (yes/no): ").lower() # After a game concludes (either by a win or a tie), the player is prompted to decide if they want to play again. The input is converted to lowercase to standardize the response. If the player types 'yes', the main game loop will start a new game. If the player types anything other than 'yes', a thank you message is printed, and the program exits.
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__": # Running the game. It calls the tic_tac_toe() function to start the game. 
    tic_tac_toe()