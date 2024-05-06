def print_board(board):
    """
    Function to print the Tic-Tac-Toe board.
    
    Parameters:
    - board (list of lists): The 3x3 grid representing the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Function to check if there is a winner.
    
    Parameters:
    - board (list of lists): The 3x3 grid representing the Tic-Tac-Toe board.
    
    Returns:
    - bool: True if there is a winner, False otherwise.
    """
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Function to check if the board is full.
    
    Parameters:
    - board (list of lists): The 3x3 grid representing the Tic-Tac-Toe board.
    
    Returns:
    - bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Function to play Tic-Tac-Toe game.
    """
    # Initialize the board and player
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    # Main game loop
    while not check_winner(board) and not is_board_full(board):
        print_board(board)
        try:
            # Get player input
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            # Validate input and update the board
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = player
                    player = "O" if player == "X" else "X"
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid row or column. Please enter values between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter integers only.")

    # Print the final board
    print_board(board)

    # Determine the winning player
    winning_player = "X" if player == "O" else "O"

    # Print the result
    if check_winner(board):
        print("Player " + winning_player + " wins!")
    else:
        print("It's a tie!")

# Start the game
tic_tac_toe()
