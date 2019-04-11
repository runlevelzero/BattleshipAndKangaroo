
import random

gameBoard          = [[]]
locationOfFlower   = [0,0]
locOfBobby = [0,0]

DIRECTIONS = {"L" : [-1,0], "R" : [1, 0], "U" : [0,-1], "D": [0,1]}

def initializeGame(sizeOfBoard):
    gameBoard = [["[ ]" for i in range(sizeOfBoard)] for j in range(sizeOfBoard)]
    locationOfFlower = [random.randint(0,sizeOfBoard-1), random.randint(0,sizeOfBoard-1)]

def printBoard():
    for line in gameBoard:
        print line

def move(direction):
    repl = [locOfBobby[0], locOfBobby[1]]
    try:
        locOfBobby[0] = locOfBobby[0] + DIRECTIONS[direction][0]
        locOfBobby[1] = locOfBobby[1] + DIRECTIONS[direction][1]
        if locOfBobby[0] < 0:
            locOfBobby[0] = 0
        elif locOfBobby[0] >= len(gameBoard):
            locOfBobby[0] = len(gameBoard) - 1
        if locOfBobby[1] < 0:
            locOfBobby[1] = 0
        elif locOfBobby[1] >= len(gameBoard):
            locOfBobby[1] = len(gameBoard) - 1
        print(locOfBobby)
    except KeyError:
        return locOfBobby

def doUserAction():
    user = raw_input("What do you want to do [MV, PICK, PLANT]")
    if len(user) >= 2:
        if user[0:1] == "MV":
            locOfBobby = move(user [-1])
        elif user == "PICK":
            print()
        elif user == "PLANT":
            print()

def playGame():
    printBoard()
    doUserAction()


move("R")