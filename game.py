# Create a playable Tic-Tac-Toe game with an AI opponent using the minimax algorithm

import math
import random
import time

# Global variables
X = "X"
O = "O"
EMPTY = None
HUMAN = None
AI = None

def main():
    # Play a game of Tic-Tac-Toe
    global HUMAN, AI
    HUMAN = X
    AI = O
    board = initial_state()
    while True:
        # Human's turn
        move = minimax(board)
        board = result(board, move)
        print_board(board)
        if terminal(board):
            break
        # AI's turn
        move = minimax(board)
        board = result(board, move)
        print_board(board)
        if terminal(board):
            break

def initial_state():
    # Return starting state of the board
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    # Return player who has the next turn on a board
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    return X if x_count <= o_count else O

def actions(board):
    # Return set of all possible actions (i, j) available on the board
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions

def result(board, action):
    # Return the board that results from making move (i, j) on the board
    if action not in actions(board):
        raise Exception("Invalid action")
    new_board = [[board[i][j] for j in range(3)] for i in range(3)]
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    # Return the winner of the game, if there is one
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

def terminal(board):
    # Return True if game is over, False otherwise
    if winner(board) != None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

def utility(board):
    # Return 1 if X has won the game, -1 if O has won, 0 otherwise
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0

def print_board(board):
    # Print the board
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == EMPTY:
                print("   ", end="")
            else:
                print(f" {cell} ", end="")
            print("|", end="")
        print()
        print("-------------")

def minimax(board):
    # Return the optimal action for the current player on the board
    if player(board) == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]

def max_value(board):
    # Return the maximum value of the board
    if terminal(board):
        return utility(board), None
    v = -math.inf
    action = None
    for a in actions(board):
        min_v = min_value(result(board, a))[0]
        if min_v > v:
            v = min_v
            action = a
    return v, action


def min_value(board):
    # Return the minimum value of the board
    if terminal(board):
        return utility(board), None
    v = math.inf
    action = None
    for a in actions(board):
        max_v = max_value(result(board, a))[0]
        if max_v < v:
            v = max_v
            action = a
    return v, action

if __name__ == "__main__":
    main()

