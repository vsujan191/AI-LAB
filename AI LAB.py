import random

def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, mark):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == mark:
            return True
    return False

def is_full(board):
    return all(str(cell) not in "123456789" for cell in board)

def play_game():
    board = [str(i) for i in range(1, 10)]
    human_symbol = 'X'
    cpu_symbol = 'O'
    
    print("TIC-TAC-TOE GAME (HUMAN vs CPU)")
    print_board(board)

    while True:
        print("Human's Turn (X)")
        while True:
            try:
                move = int(input("Enter position (1-9): "))
                if 1 <= move <= 9 and board[move - 1] not in ['X', 'O']:
                    board[move - 1] = human_symbol
                    break
                else:
                    print("Invalid move. Spot already taken or out of range. Try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")

        print_board(board)

        if check_winner(board, human_symbol):
            print("You Won!")
            break
            
        if is_full(board):
            print("It's a Draw!")
            break

        print("Computer's Turn (O)")
        available_moves = [i for i in range(9) if board[i] not in ['X', 'O']]
        cpu_move = random.choice(available_moves)
        
        print(f"Computer played 'O' at position {cpu_move + 1}")
        board[cpu_move] = cpu_symbol

        print_board(board)

        if check_winner(board, cpu_symbol):
            print("Computer Won!")
            break

        if is_full(board):
            print("It's a Draw!")
            break

if __name__ == "__main__":
    play_game()
