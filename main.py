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

def make_computer_move(board):
    available_moves = [i for i in range(9) if board[i] == '-']
    return random.choice(available_moves) if available_moves else None

def main():
    board = ['-'] * 9
    computer_symbol = 'X'
    user_symbol = 'O'

    print_board(board)

    while True:
        # Computer move
        computer_move = make_computer_move(board)
        if computer_move is not None:
            board[computer_move] = computer_symbol
        else:
            print("Tied!")
            break

        print_board(board)

        if check_winner(board, computer_symbol):
            print("Computer Wins!")
            break

        if is_board_full(board):
            print("Tied!")
            break

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
        except (ValueError, IndexError):
            print("Error: Invalid input. Try again.")

if __name__ == "__main__":
    main()
