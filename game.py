import copy

def init_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print('---------')
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print('\n---------')

def valid_move(x, y, board):
    if x < 1 or y < 1 or x > 3 or y > 3:
        return False
    elif board[x-1][y-1] != ' ':
        return False
    return True

def has_ending(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':  # rows
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':  # columns
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':  # diagonals
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':  # diagonals
        return board[0][2]

    if ' ' not in [cell for row in board for cell in row]:  # draw
        return 'draw'
    return False

def player_move(board):
    while True:
        x, y = map(int, input("Enter your move (row, column): ").split(','))
        if valid_move(x, y, board):
            return x-1, y-1
        else:
            print("Invalid move. Try again.")

def ai_move(board):
    best_score = float('-inf')
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def minimax(board, depth, maximizing_player):
    result = has_ending(board)
    if result:
        if result == 'X':
            return -1
        elif result == 'O':
            return 1
        else:  # Draw
            return 0

    if maximizing_player:
        maxEval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    maxEval = max(maxEval, eval)
        return maxEval
    else:  # Minimizing player
        minEval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    minEval = min(minEval, eval)
        return minEval

def tic_tac_toe():
    board = init_board()
    current_player = 'X'  # X always starts

    while True:
        print_board(board)
        if current_player == 'X':
            x, y = player_move(board)
            board[x][y] = 'X'
        else:  # AI's turn
            x, y = ai_move(board)
            board[x][y] = 'O'

        ending = has_ending(board)
        if ending:
            print_board(board)
            if ending == 'X':
                print("X wins!")
            elif ending == 'O':
                print("O wins!")
            else:
                print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
