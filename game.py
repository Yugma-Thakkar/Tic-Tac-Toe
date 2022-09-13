board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def printBoard(board):
    for i in range(0, len(board)):
        print("{}|{}|{}".format(board[i][0], board[i][1], board[i][2]))
        if (i != 2):
            print("-----")


def game(board):
    printBoard(board)

printBoard(board)
