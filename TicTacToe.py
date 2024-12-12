# Function to print the Tic Tac Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Function to check if someone has won
def check_winner(board, player):
    # Define all possible winning combinations
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                            (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                            (0, 4, 8), (2, 4, 6)]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to play the game
def play_game():
    board = [' '] * 9  # Initial empty board
    current_player = 'X'  # Starting with player X
    
    while True:
        print_board(board)
        
        # Take input from the current player
        try:
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        
        # Place the move on the board
        board[move] = current_player
        
        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (tie condition)
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()
