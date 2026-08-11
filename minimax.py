# Steps:
# 1)printing the game board
# 2)take player input
# 3) check for win or tie
# 4) switch the player 
# 5) check for win or tie again 
# 6) add minimax algorithm 

import math
import random
from itertools import permutations
def printBoard(board):
    x=0
    for i in range(0,9,3):
        x+=1
        print(" |".join(board[i:i+3]))
        if x!=3:
            print("__|__|__")

def checkWin(player, playerName):
    global winner
    winCombs=[[0,4,8],[6,4,2],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
    for i,j,k in permutations(player,3):
        if [i,j,k] in winCombs:
            print(playerName,"won!")
            winner=True
            break
    if winner==False and len(turn)==0:
            print("its a tie, no one won!")
            winner=True
def checkforWin(player):
     winCombs=[[0,4,8],[6,4,2],[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
     for i,j,k in permutations(player,3):
             if [i,j,k] in winCombs:   
                 return True
     return False
def checkTie():
    if checkforWin(playerInputs)==False and checkforWin(compInputs)==False and len(turn)==0:
        return True
    else:
        return False
def playerInput():
    no=int(input("select the position:"))
    while no not in turn:
        no=int(input("that spot is taken, pick again:"))
    board[no]=s
    playerInputs.append(no)
    turn.remove(no)

# def compPlay():
#     choice=random.choice(turn)
#     turn.remove(choice)
#     compInputs.append(choice)
#     if s=='X':
#         board[choice]="O"
#     else:
#         board[choice]="X"
def compPlay():
    bestScore=-math.inf
    bestMove=None
    for move in turn[:]:
        board[move]=bot
        compInputs.append(move)
        turn.remove(move)
        score=minimax(board,False)
        turn.append(move)
        board[move]=str(move)
        compInputs.remove(move)
        if score > bestScore:
            bestScore = score
            bestMove = move
    turn.remove(bestMove)
    compInputs.append(bestMove)
    board[bestMove] = bot 

def minimax(state, isMax):
     if checkforWin(compInputs):
          return 1
     elif checkforWin(playerInputs):
          return -1
     elif checkTie():
          return 0
     if isMax:
          bestScore=-math.inf
          for move in turn[:]:
               state[move]=bot
               turn.remove(move)
               compInputs.append(move)
               score=minimax(state,False)
               turn.append(move)
               compInputs.remove(move)
               state[move] = str(move)
               bestScore=max(bestScore,score)
          return bestScore
     else:
              bestScore=math.inf
              for move in turn[:]:
                   state[move]=s
                   turn.remove(move)
                   playerInputs.append(move)
                   score=minimax(state,True)
                   turn.append(move)
                   state[move] = str(move)
                   playerInputs.remove(move)
                   bestScore=min(bestScore,score)
              return bestScore      
     
     
winner=False
s=str(input("you want X or O:"))
if s=='X':
     bot="O"
else:
   bot="X"
board=["0","1","2","3","4","5","6","7","8"]
turn=[0,1,2,3,4,5,6,7,8]
playerInputs=[]
compInputs=[]
while winner==False:
    printBoard(board)
    playerInput()
    checkWin(playerInputs,"PLAYER")
    if winner==True:
        printBoard(board)
        break
    compPlay()
    checkWin(compInputs,"COMPUTER")
    if winner==True:
            printBoard(board)
            break