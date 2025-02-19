"""This module implements a Tic Tac Toe game with a simple command-line interface."""

import random
import os

PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'
EMPTY_SQUARE = '_'
MAX_ROUNDS = 5

def prompt(text):
    """Prints a prompt to the console with a '=>' prefix."""
    print(f"=> {text}")

def clear_screen():
    """Clears the console screen based on the operating system."""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def initialize_board():
    """Initializes and returns an empty Tic Tac Toe board."""
    ttt_board = [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
]
    return ttt_board

def display(board):
    """Displays the current state of the Tic Tac Toe board."""
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("-" * 13)

def available_spaces(board):
    """Finds and returns all available spaces on the board."""
    available = []

    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY_SQUARE:
                # Convert 2D index to 1D position (1-9) / "flatten"
                position = row * 3 + column + 1
                available.append(str(position))
    return available

def join_or(options_list, separator = ', ', connector = 'or'):
    """Joins a list of items into a human-readable string."""
    if not options_list:
        return ''
    lst = options_list[:-1]
    last_element = str(options_list[-1])
    result = ''

    if len(options_list) == 1:
        return str(options_list[0])
    if len(options_list) == 2:
        return f"{options_list[0]} {connector} {options_list[1]}"
    for option in lst:
        result += str(option) + separator
    return f"{result}{connector} {last_element}"

def get_position_coords(position):
    """Converts a 1D board position to 2D coordinates."""
    row = position // 3 # integer division to get the row
    column = position % 3 # modulo to get the column
    return row, column

def player_turn(board):
    """Handles the player's turn in the Tic Tac Toe game."""
    options = join_or(available_spaces(board))
    prompt(f"Choose an available square number: {options}")
    player_choice = input()

    while player_choice not in available_spaces(board):
        prompt("Please choose a valid option.")
        player_choice = input()

    #Convert the player's choice to 2D coordinates to fit a valid position in the list
    player_choice = int(player_choice) - 1 # Turn the choice into 0-based index
    row, column = get_position_coords(player_choice)
    # Place the player's symbol on the board
    board[row][column] = PLAYER_MARKER

def offensive_and_defensive_moves(board):
    """
    Checks for offensive and defensive moves for both players.
    If available, the function returns the board position for the move.    
    """
    #check rows
    for marker in [COMPUTER_MARKER, PLAYER_MARKER]:
        for row in range(3):
            if board[row].count(marker) == 2 and EMPTY_SQUARE in board[row]:
                empty_position = board[row].index(EMPTY_SQUARE)
                return row, empty_position
        #check columns
        for column in range(3):
            column_values = [board[row][column] for row in range(3)]
            if column_values.count(marker) == 2 and EMPTY_SQUARE in column_values:
                empty_position = column_values.index(EMPTY_SQUARE)
                return  empty_position, column
        #check main diagonal
        main_diagonal = [board[i][i] for i in range(3)]
        if main_diagonal.count(marker) == 2 and EMPTY_SQUARE in main_diagonal:
            empty_position = main_diagonal.index(EMPTY_SQUARE)
            return empty_position, empty_position

        #check anti-diagonal
        anti_diagonal = [board[i][2-i] for i in range(3)]
        if anti_diagonal.count(marker) == 2 and EMPTY_SQUARE in anti_diagonal:
            empty_position = anti_diagonal.index(EMPTY_SQUARE)
            return empty_position, 2 - empty_position

    #if no threat is found
    return None

def computer_turn(board):
    """
    Checks for offensive and defensive moves for the computer.
    If any, the function places the the computer marker on the board.
    """
    #check for ofensive opportunities or threats
    if offensive_and_defensive_moves(board):
        row, column = offensive_and_defensive_moves(board)
        board[row][column] = COMPUTER_MARKER
    else:
        computer_choice = random.choice(available_spaces(board))
        row, column = get_position_coords(int(computer_choice) - 1)
        board[row][column] = COMPUTER_MARKER

def winner(board):
    """
    The function scans the board for winning combinations.
    If it finds a winning combination, it returns the winning symbol.
    It returns none it there is no winner.
    """
    #check rows
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2]
            and board[row][0] != EMPTY_SQUARE):
            return board[row][0] # return winning symbol

    #check columns
    for column in range(3):
        if (board[0][column] == board[1][column] == board[2][column]
            and board[0][column] != EMPTY_SQUARE):
            return  board[0][column]

    #check diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY_SQUARE:
        return board[0][0]

    #check anti-diagonal
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY_SQUARE:
        return board[2][0]

    #No winner
    return False

def is_tie(board):
    """Checks for a tie."""
    return all(square != EMPTY_SQUARE for row in board for square in row)

def game_status(board):
    """
    Evaluates the current game status.
    Returns the winner's symbol, 'Tie' if it's a tie, or None if the game continues.
    """
    if winner(board):
        return winner(board)

    if is_tie(board):
        return 'Tie'

    return None #Game continues

def take_turn(board, player):
    """Manages a single turn for either player or computer."""
    if player == PLAYER_MARKER:
        player_turn(board)
    else:
        computer_turn(board)
    display(board)
    return game_status(board)

def get_valid_input(prompt_message, valid_choices):
    """Gets and validates user input against a list of valid choices."""

    while True:
        user_input = input(prompt_message).lower()
        if user_input in valid_choices:
            return user_input
        prompt(f"That is not a valid choice. Please choose from: {', '.join(valid_choices)}")

def wants_to_play_again():
    """Asks if the player wants to play again."""
    return get_valid_input("Play again? Press y for 'yes' and 'n' for no", ['y', 'n']) == 'y'

def play_tic_tac_toe():
    """Function responsible for the gameplay."""

    computer_score = 0
    player_score = 0
    prompt("Welcome to Tic Tac Toe")
    prompt("What is your name?")
    player_name = input()

    while True:
        board = initialize_board()
        display(board)
        prompt(f"{player_name}'s score: {player_score} - Computer score: {computer_score}")
        first_move = get_valid_input(
            "Who should go first?\n Press 'c' for Computer or 'h' for Human",['c', 'h']
        )

        if first_move == 'h':
            current_player = PLAYER_MARKER
        else:
            prompt("Computer goes first.")
            current_player = COMPUTER_MARKER
        while True:
            result = take_turn(board, current_player)

            if result:
                if winner(board) == PLAYER_MARKER:
                    prompt(f"{player_name} wins the round!")
                    player_score += 1
                elif winner(board) == COMPUTER_MARKER:
                    prompt("Computer wins the round!")
                    computer_score += 1
                else:
                    prompt("It's a tie.")
                break
            current_player = COMPUTER_MARKER if current_player == PLAYER_MARKER else PLAYER_MARKER

        if ((computer_score + player_score) == MAX_ROUNDS
            or computer_score == 3 or player_score == 3):
            if player_score > computer_score:
                prompt(f"{player_name} wins!!!")
            else:
                prompt("Computer wins!!!")

        # Wait for user to proceed before clearing screen
        input("Press Enter to continue to the next round...")

        clear_screen()  # Clear the screen after user input

        if not wants_to_play_again():
            break

        clear_screen()

    prompt("Thanks for playing!")

play_tic_tac_toe()
