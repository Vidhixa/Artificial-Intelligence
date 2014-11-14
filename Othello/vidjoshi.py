'''
Homework 3.2
Created on Oct 17, 2014
@author: Vidhixa
Agent for Othello

'''

import gamePlay
from copy import deepcopy
from gamePlay import opponent

#Positional strategy for calculating heurisitic
positional = ((),(99, -8, 8, 6, 6, 8, -8, 99),
            (99, -8, 8, 6, 6, 8, -8, 99),
            (-8, -24, -4, -3, -3, -4, -24, -8),
            (8, -4, 7, 4, 4, 7, -4, 8),
            (6, -3, 4, 0, 0, 4, -3, 6),
            (6, -3, 4, 0, 0, 4, -3, 6),
            (8, -4, 7, 4, 4, 7, -4, 8),
            (-8, -24, -4, -3, -3, -4, -24, -8),
            (99, -8, 8, 6, 6, 8, -8, 99))

#Value returns the heuristic value of a particular board position
def value(board, color, maximizingPlayer): 
    new = deepcopy(board)
 
    #we use i and j to refer to indices at positional
    i=0
    j=0    
 
    #values to calculate positional advantage of self and opponent 
    valueSelf = 0
    valueOpp = 0 
    
    #Traversing each board position to calculate the advantage based on the         
    for row in board:
        j = 0
        i += 1
        for elem in row:
            value = positional[i][j] 
            if elem == color:
                #if we are maximizing player, we keep adding advantage to self since it is self color
                # else add in opponent
                if maximizingPlayer:
                    valueSelf = valueSelf + value
                else:
                    valueOpp = valueOpp + value
            else:
                #if we are maximizing player, we keep subtracting since its not our color advantage to self
                #else subtract from opponent
                if maximizingPlayer:
                    valueSelf = valueSelf - value
                else:
                    valueOpp = valueOpp - value
            j +=1
                 
    #The positional advantage of whole board will be subtraction of self advantage and opponents advantage    
    boardCount = valueSelf-valueOpp
 
    #calculating number of available moves in future; for self and opponent
    myMoves = successor(new, color)
    oppMoves = successor(new, opponent(color))
     
    #Taking the ratio of moves 
    #If opponent comes to "pass" in future; set m as 10 which is desirable
    #if self has "pass" in future; set m as -10 since it is undesirable                 
    if not myMoves=="pass" and not oppMoves=="pass":
        if len(myMoves) > len(oppMoves):
            m = len(myMoves) / float((len(myMoves) + len(oppMoves)))
        else:
            m = -(len(myMoves)) / float((len(myMoves) + len(oppMoves)))
    elif myMoves=="pass":
        m = -10
    else:
        m = 10        
   
    #The heurisitic will scale mobility and add positional advantage
    heuristic = (100 * m) +  boardCount    

    return heuristic   
        

#Returns my calculated move
def nextMove(board, color, time):
    #Seems to be a good depth to work with
    maxDepth = 3
    
    #Defining alpha and beta for pruning purpose
    alpha = float("-inf")
    beta = float("inf")
    
    #Taking the second return argument to be best move
    bestMove =  minimax(board, color, maxDepth, alpha, beta, True)[1]
    return bestMove

#Minimax with alpha beta pruning
def minimax(board, color, depth, alpha, beta, maximizingPlayer):
    #By default if we do not get any move, we use "pass"
    bestMove = "pass"
    
    #Successor function called on current board 
    moves = successor(board, color)
    if depth == 0 or moves== "pass":
        return value(board, color, maximizingPlayer),"pass"
    
    #Recursing over self and opponent
    if maximizingPlayer: 
        for move in moves:
            newBoard = deepcopy(board)
            gamePlay.doMove(newBoard,color, move)
            child = newBoard
            x = minimax(child, gamePlay.opponent(color), depth - 1, alpha, beta, False)[0]
            
            #alpha will select the maximum value
            if alpha < x:
                alpha = x
                bestMove = move 
                
            #pruning condition
            if beta <= alpha:
                break             
        #maxplayer will always return the best move    
        return alpha,bestMove
    
    #opponents best play
    else:
        for move in moves:
            newBoard = deepcopy(board)
            gamePlay.doMove(newBoard,color, move)
            child =  newBoard
            y = minimax(child, gamePlay.opponent(color), depth - 1, alpha, beta, True)[0]
            
            #beta will select the minimum value
            if beta > y:
                beta = y
                
            #pruning condition   
            if beta <= alpha:
                break
             
        #Doesn't matter what move we pass, this will never be returned to nextmove    
        return beta, "pass"

#Finding valid  successor moves
def successor(board, color): 
    moves = [] 
    for i in range(8):
        for j in range(8):
            if gamePlay.valid(board, color, (i,j)):
                moves.append((i,j))
    #If no valid move, we "pass"
    if len(moves) == 0:
        return "pass"
    else:
        return moves

    

    