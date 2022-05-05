import os
#board
def printBoard(board): 
    print(board[1] + '|' +board[2]+ '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' +board[5]+ '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' +board[8]+ '|' + board[9])
    print('-+-+-')


# check the position player 1 entered
def checkPosition(position):
    if board[position] == ' ':
        drawOnBoard(player , position)

    else :
        print("This position is not empty please enter anthor position ...")
        playing1()

#Drawing symbol in the boared "player 1"
def drawOnBoard(player,position):
    board[position] = player
    printBoard(board)

#The player 1 move
def playing1 ():
    position = int (input("Choose position from 1 to 9 for player 1 : "))
    if position == -1:
        calculateHeuristic(board)
        os._exit(0)
    else:
        checkPosition(position)

#Drawing the symbol on the board "player 2"
def drawOnBoardB(bot,pos):
    board[pos] = bot
    printBoard(board)


#check player 2 move
def checkpos(pos):
    if board[pos] == ' ':
        drawOnBoardB(bot,pos)
    else:
        print("This position is not empty please enter anthor position ...")
        botMove()


#Player 2 move
def botMove ():
    pos = int (input("Choose position from 1 to 9 for player 2 : "))
    if pos == -1:
        calculateHeuristic(board)
        os._exit(0)
    else:
        checkpos(pos)


#check who win
def checkWhoWin(z):
    if (board[z] == player):
        print("Player 1 win")
        calculateHeuristic(board)
        
    else:
        print("Player 2 win")
        calculateHeuristic(board)
        

    os._exit(0)

#check for winner
def checkForTheWinner():
        if(board[1] == board[2] and board[2] == board[3] and board[3] != ' '):
            checkWhoWin(1)
           
        elif(board[1] == board[4] and board[4] == board[7] and board[7] != ' '):

            checkWhoWin(1)
            
        elif(board[2] == board[5] and board[5] == board[8] and board[8] != ' '):

            checkWhoWin(2)

        elif(board[3] == board[6] and board[6] == board[9] and board[9] != ' '):

            checkWhoWin(3)
            
            
        elif(board[3] == board[5] and board[5] == board[7] and board[7] != ' '):

            checkWhoWin(3)
            
            
        elif(board[1] == board[5] and board[5] == board[9] and board[9] != ' '):

            checkWhoWin(1)  
            
        elif(board[4] == board[5] and board[5] == board[6] and board[6] != ' '):

            checkWhoWin(4)
            
            
        elif(board[7] == board[8] and board[8] == board[9] and board[9] != ' '):

            checkWhoWin(7)
       
# calculate the heuristic
def calculateHeuristic(board):
    #player 1 heuristic
    y = 0
    if(board[1] == player  or board[2] == player or board[3] == player):
        if (board[2] != bot and board[3] != bot and board[1] != bot ):
            y = y + 1
    if(board[1] == ' ' and board[2] == ' ' and board[3] == ' '):
            y = y + 1
    if(board[4] == player or board[5] == player or board[6] == player):
        if (board[5] != bot and board[6] != bot and board[4] != bot):
            y = y + 1
    if(board[4] == ' ' and board[5] == ' ' and board[6] == ' '):
            y = y + 1
    if(board[7] == player or board[8] == player or board[9] == player):
        if (board[8] != bot and board[9]!= bot and board[7] != bot ):
            y = y + 1
    if(board[8] == ' ' and board[9] == ' ' and board[7] == ' '):
            y = y + 1
    if(board[1] == player or board[4] == player or board[7] == player):
        if (board[4] != bot and board[7]!= bot and board[1] != bot):
            y = y + 1
    if(board[1] == ' ' and board[4] == ' ' and board[7] == ' '):
            y = y + 1
    if(board[2] == player or board[5] == player or board[8] == player ):
        if (board[5] != bot and board[8]!= bot and board[2] != bot):
            y = y + 1
    if(board[2] == ' ' and board[5] == ' ' and board[8] == ' '):
            y = y + 1
    if(board[3] == player or board[6] == player or board[9] == player):
        if (board[6] != bot and board[9]!= bot and board[3]!= bot):
            y = y + 1
    if(board[3] == ' ' and board[6] == ' ' and board[9] == ' '):
            y = y + 1
    if(board[1] == player or board[5] == player or board[9] == player):
        if (board[5] != bot and board[9]!= bot and board[1]!= bot):
            y = y + 1
    if(board[1] == ' ' and board[5] == ' ' and board[9] == ' '):
            y = y + 1
    if(board[3] == player or board[5] == player or board[7] == player):
        if (board[5] != bot and board[7]!= bot and board[3]!= bot):
            y = y + 1
    if(board[3] == ' ' and board[5] == ' ' and board[7] == ' '):
            y = y + 1
#Player 2 heuristic 
    t = 0
    if(board[1] == bot or board[2] == bot or board[3] == bot ):
        if (board[2] != player and board[3]!= player and board[1] != player):
            t = t + 1
    if (board[2] ==' ' and board[3] == ' ' and board[1] == ' '):
            t = t + 1
    if(board[4] == bot or board[5] == bot or board[6] == bot):
        if (board[5] != player and board[6]!= player and board[4] != player):
            t = t + 1
    if (board[4] ==' ' and board[5] == ' ' and board[6] == ' '):
            t = t + 1
    if(board[7] == bot or board[8] == bot or board[9] == bot):
        if (board[8] != player and board[9]!= player and board[7] != player):
            t = t + 1
    if (board[7] ==' ' and board[8] == ' ' and board[9] == ' '):
            t = t + 1
    if(board[1] == bot or board[4] == bot or board[7] == bot):
        if (board[4] != player and board[7]!= player and board[1] != player):
            t = t + 1
    if (board[1] ==' ' and board[4] == ' ' and board[7] == ' '):
            t = t + 1
    if(board[2] == bot or board[5] == bot or board[8] == bot):
        if (board[5] != player and board[8]!= player and board[2] != player):
            t = t + 1
    if (board[2] ==' ' and board[5] == ' ' and board[8] == ' '):
            t = t + 1
    if(board[3] == bot or board[9] == bot or board[6] == bot):
        if (board[6] != player and board[9]!= player and board[3] != player):
            t = t + 1
    if (board[9] ==' ' and board[3] == ' ' and board[6] == ' '):
            t = t + 1
    if(board[1] == bot or board[5] == bot or board[9] == bot):
        if (board[5] != player and board[9]!= player and board[1] != player):
            t = t + 1
    if (board[1] ==' ' and board[5] == ' ' and board[9] == ' '):
            t = t + 1
    if(board[3] == bot or board[5] == bot or board[7] == bot):
        if (board[5] != player and board[7]!= player and board[3] != player):
            t = t + 1
    if (board[5] ==' ' and board[3] == ' ' and board[7] == ' '):
            t = t + 1

    Heuristic = y - t
    print ("The Heuristic : " , y ," - " , t ," = ", Heuristic)

#main
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '};

printBoard(board)

#player choose symbol
print("___________________________________")

player = str.upper (input("Choose X or O : "))

print("___________________________________")

if (player == 'X'):
        bot = 'O'
        print("Player 2 symbol : "+ bot)
        print("___________________________________")
        print("Player 1 symbol : "+player)
elif(player == 'O'):
        bot = 'X'
        print("Player 2 symbol : "+ bot)
        print("___________________________________")
        print("Player 1 symbol : "+player)
else:
    while(player != 'X' or player != 'O'):
        player = str.upper (input("Choose X or O : "))
        print("___________________________________")
        if player == 'X':
            bot = 'O'
            break
        elif player == 'O':
            bot = 'X'
            break
    print("Player 2 symbol : "+ bot)

    print("___________________________________")

    print("Player 1 symbol : "+player)

x = 0
for x in range (4):
        print("___________________________________")
        playing1()
        checkForTheWinner()
        print("___________________________________")
        botMove()
        checkForTheWinner()

playing1()
      
calculateHeuristic(board)