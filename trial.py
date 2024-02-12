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
