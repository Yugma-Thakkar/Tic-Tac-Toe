import re
from unicodedata import ucd_3_2_0

# def check_win(moves[]):
    # for i in range(0, len(moves)):
        # if moves[i] 

def game():
    u1 = input("Player 1, please enter your name: ")
    u2 = input("Player 2, please enter your name: ")

    print("Welcome to Tic Tac Toe, " + u1 + " and " + u2 + "!")

    pattern = r"\d:\d"
    moves1 = []
    moves2 = []

    for i in range(0, 9):
        if i % 2 == 0:
            move = input("Player 1, its your move: ")
            if re.match(pattern, move):
                if (move > (3, 3)):
                    print('Error! Cannot enter value greater than (3, 3)')
                    break
                moves1.append(move)
                print(moves1[i])
            else:
                print('Input syntax incorrect')
                break
            #check if u1 won
        
        else: 
            move = input("Player 2, its your move")
            if re.match(pattern, move):
                if move > (3,3):
                    print('Error! Cannot enter value greater than (3, 3)')
                    break
                moves2.append(move)
                print(moves2[i])
            else:
                print('Input syntax incorrect')
                break
            #check if u2 won
        
game()