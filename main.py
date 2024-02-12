import random

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}\n-----------\n"
          f"{board[3]} | {board[4]} | {board[5]}\n-----------\n"
          f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_board_full(board):
    return all(cell != '-' for cell in board)

def evaluate(board):
    # Check for a winner
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None  # Game is still ongoing

def minimax(board, depth, maximizing_player):
    eval_result = evaluate(board)
    if depth == 0 or evaluate(board) is not None:
        return eval_result

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = 'X'
                eval = minimax(board, depth - 1, False)
                board[i] = '-'
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = 'O'
                eval = minimax(board, depth - 1, True)
                board[i] = '-'
                min_eval = min(min_eval, eval)
        return min_eval

def make_computer_move(board):
    best_move = -1
    best_eval = float('-inf')
    for i in range(9):
        if board[i] == '-':
            board[i] = 'X'
            eval = minimax(board, 9, False)
            board[i] = '-'
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

def toss():
    return random.choice(['Computer', 'User'])

def main():
    board = ['-'] * 9
    computer_symbol = 'X'
    user_symbol = 'O'

    start_player = toss()
    print(f"{start_player} won the toss and will start first.")

    print_board(board)

    while True:
        if start_player == 'Computer':
            # Computer move
            computer_move = make_computer_move(board)
            if computer_move is not None:
                board[computer_move] = computer_symbol
        else:
            # User move
            try:
                user_move = int(input("Enter your Move (1-9): ")) - 1
                if 0 <= user_move < 9 and board[user_move] == '-':
                    board[user_move] = user_symbol

                    print_board(board)

                    if check_winner(board, user_symbol):
                        print("You Win!")
                        break

                    if is_board_full(board):
                        print("Tied!")
                        break
                else:
                    print("Invalid Move!! Try Again")
                    continue
            except (ValueError, IndexError):
                print("Error: Invalid input. Try again.")
                continue

        print_board(board)

        if check_winner(board, computer_symbol):
            print("Computer Wins!")
            break

        if is_board_full(board):
            print("Tied!")
            break

        start_player = 'User' if start_player == 'Computer' else 'Computer'

if __name__ == "__main__":
    main()
