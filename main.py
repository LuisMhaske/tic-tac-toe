import random

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]} \n-----------\n"
          f"{board[3]} | {board[4]} | {board[5]} \n-----------\n"
          f"{board[6]} | {board[7]} | {board[8]}")


def check_winner(board, player):
    winning_combination = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Row
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Column
        [0, 4, 8], [2, 4, 6]  # Diagonal
    ]

    for combo in winning_combination:
        if all(board[i] == player for i in combo):
            return True
        return False


def is_board_full(board):
    return all(cell != '-' for cell in board)


def make_computer_move(board):
    available_moves = [i for i in range(9) if board[i] == '-']

    if not available_moves:
        return None  # No available moves, return None or some other indicator

    return random.choice(available_moves)


def main():
    board = ['-'] * 9
    computer_symbol = 'X'
    user_symbol = 'O'

    print_board(board)

    while True:
        computer_move = make_computer_move(board)
        board[computer_move] = computer_symbol

        print_board(board)

        if check_winner(board, computer_symbol):
            print("Computer Wins!")
            break

        elif is_board_full(board):
            print("Tied")
            break

        break

    while True:
        print_board(board)

        try:
            user_move = int(input("Enter you Move (1-9): ")) - 1
            if 0 <= user_move < 9 and board[user_move] == '-':
                board[user_move] = user_symbol

                if check_winner(board, user_symbol):
                    print_board(board)
                    print("You Win!")
                    break

                elif is_board_full(board):
                    print("Tied!")
                    break
            else:
                print("Invalid Move!! Try Again")
                continue
        except (ValueError, IndexError):
            print("Error: Invalid input. Try again.")
            continue

    print_board(board)

    # if check_winner(board, user_symbol):
    #     print("You Win!")
    #
    #
    # if is_board_full(board):
    #     print("Tied!")



if __name__ == "__main__":
    main()
