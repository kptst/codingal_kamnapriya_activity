import random

# Initialize board
board = [" " for _ in range(9)]

# Display the board
def print_board():
    print()
    for i in range(3):
        row = "|".join(board[i*3:(i+1)*3])
        print(" " + row)
        if i < 2:
            print("---|---|---")
    print()

# Check win
def check_winner(brd, player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diagonals
    ]
    return any(all(brd[pos] == player for pos in line) for line in wins)

# Check tie
def is_tie(brd):
    return " " not in brd

# Get available moves
def available_moves(brd):
    return [i for i, v in enumerate(brd) if v == " "]

# AI move
def ai_move():
    for move in available_moves(board):
        # Try to win
        board_copy = board[:]
        board_copy[move] = "O"
        if check_winner(board_copy, "O"):
            return move

    for move in available_moves(board):
        # Try to block
        board_copy = board[:]
        board_copy[move] = "X"
        if check_winner(board_copy, "X"):
            return move

    # Else pick random
    return random.choice(available_moves(board))

# Player move
def player_move():
    while True:
        try:
            move = int(input("Choose your move (1-9): ")) - 1
            if move in available_moves(board):
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()

    while True:
        # Player move
        move = player_move()
        board[move] = "X"
        print_board()
        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        if is_tie(board):
            print("🤝 It's a tie!")
            break

        # AI move
        print("AI is making a move...")
        move = ai_move()
        board[move] = "O"
        print_board()
        if check_winner(board, "O"):
            print("😔 AI wins!")
            break
        if is_tie(board):
            print("🤝 It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
