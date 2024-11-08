import math
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]): 
            return True
        if all([board[j][i] == player for j in range(3)]): 
            return True
        if all([board[i][i] == player for i in range(3)]): 
            return True
        if all([board[i][2 - i] == player for i in range(3)]):  
            return True
    
            return False
def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "X"):
        return 10 - depth 
    if check_winner(board, "O"):
        return depth - 10 
    if is_full(board):
        return 0 
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X" 
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " " 
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break 
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O" 
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " " 
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break 
        return min_eval
def best_move(board):
    best_val = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"  
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " " 
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)  
    return move
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"] 
    turn = 0
    while True:
        print_board(board)
        if turn % 2 == 0: 
            print("AI's turn")
            i, j = best_move(board)
            board[i][j] = "X"
        else: 
            print("Your turn")
            while True:
                try:
                    i, j = map(int, input("Enter row and column (0-2) separated by space: ").split())
                    if board[i][j] != " ":
                        print("Cell already occupied, try again.")
                        continue
                    break
                except (ValueError, IndexError):
                    print("Invalid input, try again.")
                    continue
            board[i][j] = "O"
        if check_winner(board, "X"):
            print_board(board)
            print("AI wins!")
            break
        elif check_winner(board, "O"):
            print_board(board)
            print("You win!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        turn += 1
if __name__ == "__main__":
    play_game()
