from numpy import *
import random
boats = []
oof   = ""
with open("oof.oof") as f:
    content = f.readlines()
    for line in content:
        oof += line

def gen_board(n):
    board = [["." for i in range(n)] for j in range(n)]
    return board

def makeBoat(n,size):
    for num in '.'*n:
        num1 = random.randint(0,size-1)
        num2 = random.randint(0,size-1)
        while board[num1][num2] == 'B':
            num1 = random.randint(0, size-1)
            num2 = random.randint(0, size-1)
        boat = [num1,num2]
        addBoatToBoard(boat, board)

def addBoatToBoard(boat, board):
    if board[boat[0]][boat[1]] == '.':
        board[boat[0]][boat[1]] = 'B'
        boats.append(boat)

def playGame():
    print("find the boat")
    i = 0
    while i < 4:
        x = raw_input("give me x coordinate: ")
        y = raw_input("give me y coordinate: ")
        try:
            if board[int(y)][int(x)] == 'B':
                print("YOU'VE SUNK MY BATTLESHIP")
            else:
                print(oof)
                break
        except TypeError:
            print("That's not a number you dense cabbage")
        except IndexError:
            print("That's not in range you dense cabbage")
        i += 1

board = gen_board(5)
makeBoat(4,5)

#print(board)

for line in board:
    print
playGame()