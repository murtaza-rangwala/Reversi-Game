# TASK 1 - REVERSI

# Name: Murtaza Hatim Rangwala
# Date: 08/04/2019

'''
The following program is subject to copyright and due credit should be given
to the author
'''

# Importing modules

import copy

# Defining Functions

# Defining a new starting board to begin the game with

def new_board():
    board = [[0] * 8 for i in range(8)]
    board[3][3] = 2
    board[3][4] = 1
    board[4][3] = 1
    board[4][4] = 2
            
    return board


# This function prints a human readable form of the board

def print_board(board):

    count = 1
    print("\n\n\n")
    for i in range(len(board)):
        
        # To display number for each row
        
        oneLine = 8 * (len(board[i]) + 1)
        print("   " + str(count) + "   ",end = '|')
        count += 1
        
        # For loop to print stones and blank areas. Also used to show valid_moves
        
        for j in range(len(board[i])):
            if board[i][j] == 0:
                print("   " + " " + "   ",end = '|')
            elif board[i][j] == '*':
                print("   " + "*" + "   ",end = '|')
            elif board[i][j] == 1:
                print("   " + "B" + "   ",end = '|')
            else:
                print("   " + "W" + "   ",end = '|')
        print("")
        if i == len(board) - 1:
            for p in range(oneLine):
                print('-',end = '')
        else:
            for q in range(8):
                print('-',end = '')
            for k in range(oneLine-8):
                print('.',end = '')
        print("\n")
        
    # To display alphabets for each column
    
    i =  ord('a');
    print("   " + " " + "   ",end = '|')
    for j in range(len(board[0])):
        print("   " + chr(i) + "   ",end = '|')
        i = i + 1
    print('\n')
    

# Calculates the score of both players

def score(board):
    score1 = 0
    score2 = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                score1 += 1
            elif board[i][j] == 2:
                score2 += 1

    return (score1,score2)

# Checks for given conditions for each condition

def enclosing(board,player,pos,direct):

    r,c = pos

    # Setting player's colour and opponent's colour based on passed parameter
    
    if player == 1:
        pCol = 1
        oCol = 2
    elif player == 2:
        pCol = 2
        oCol = 1

    isOCol = True

    # Left

    if direct == (0,-1):
            
        endInd = c

        # Checks if line is enclosed by same colour
        
        for i in range(c-1,-1,-1):
            if board[r][i] == pCol:
                endInd = i
                break

        # Checks if the enclosed part is filled with opponent's colours
        
        for i in range(c-1,endInd,-1):
            if board[r][i] != oCol:
                isOCol = False
        if endInd == c or endInd == c-1:
            isOCol = False

    # Right
    
    elif direct == (0,1):
        endInd = c

        # Checks if line is enclosed by same colour
        
        for i in range(c+1,len(board[r])):
            if board[r][i] == pCol:
                endInd = i
                break

        # Checks if the enclosed part is filled with opponent's colours
        
        for i in range(c+1,endInd):
            if board[r][i] != oCol:
                isOCol = False
        if endInd == c or endInd == c+1:
            isOCol = False

    # Top

    elif direct == (-1,0):
        endInd = r

        # Checks if line is enclosed by same colour
        
        for i in range(r-1,-1,-1):
            if board[i][c] == pCol:
                endInd = i
                break

        # Checks if the enclosed part is filled with opponent's colours
        
        for i in range(r-1,endInd,-1):
            if board[i][c] != oCol:
                isOCol = False
        if endInd == r or endInd == r-1:
            isOCol = False

    # Bottom
    
    elif direct == (1,0):
        endInd = r

        # Checks if line is enclosed by same colour
        
        for i in range(r+1,len(board)):
            if board[i][c] == pCol:
                endInd = i
                break

        # Checks if the enclosed part is filled with opponent's colours
        
        for i in range(r+1,endInd):
            if board[i][c] != oCol:
                isOCol = False
                break
        if endInd == r or endInd == r+1:
            isOCol = False


    # Bottom Right
    
    elif direct == (1,1):
        endInd = r
        j = c+1

        # Checks if line is enclosed by same colour
        
        for i in range(r+1,len(board)):
            if j < len(board):
                if board[i][j] == pCol:
                    endInd = i
                    break
                else:
                    j += 1

        # Checks if the enclosed part is filled with opponent's colours
        
        j = c + 1
        for i in range(r+1,endInd):
            if board[i][j] != oCol:
                isOCol = False
            j += 1
        if endInd == r or endInd == r+1:
            isOCol = False

    # Top Left
    
    elif direct == (-1,-1):
        endInd = r
        j = c-1

        # Checks if line is enclosed by same colour
        
        for i in range(r-1,-1,-1):
            if j > 0:
                if board[i][j] == pCol:
                    endInd = i
                    break
                else:
                    j -= 1

        # Checks if the enclosed part is filled with opponent's colours
        
        j = c-1
        for i in range(r-1,endInd,-1):
            if board[i][j] != oCol:
                isOCol = False
            j = j - 1
        if endInd == r or endInd == r-1:
            isOCol = False

    # Bottom Left
    
    elif direct == (1,-1):
        endRow = r
        j = c-1

        # Checks if line is enclosed by same colour
        
        for i in range(r+1,len(board)):
            if j > 0:
                if board[i][j] == pCol:
                    endRow = i
                    break
                else:
                    j -= 1

        # Checks if the enclosed part is filled with opponent's colours
        
        j = c-1
        for i in range(r+1,endRow):
            if board[i][j] != oCol:
                isOCol = False
            j -= 1
        if endRow == r or endRow == (r+1):
            isOCol = False

    # Top Right
    
    elif direct == (-1,1):
        endRow = r
        j = c+1

        # Checks if line is enclosed by same colour
        
        for i in range(r-1,-1,-1):
            if j < len(board):
                if board[i][j] == pCol:
                    endRow = i
                    break
                else:
                    j += 1

        # Checks if the enclosed part is filled with opponent's colours
        
        j = c+1
        for i in range(r-1,endRow,-1):
            if board[i][j] != oCol:
                isOCol = False
            j += 1
        if endRow == r or endRow == r-1:
            isOCol = False

    return isOCol

# Function to create a list of all valid moves

def valid_moves(board,player):
    validatedList = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0 or board[i][j] == "*":
                if enclosing(board,player,(i,j),(0,1)):
                    validatedList.append((i,j))
                if enclosing(board,player,(i,j),(0,-1)):
                    validatedList.append((i,j))
                if enclosing(board,player,(i,j),(1,0)):
                    validatedList.append((i,j))
                if enclosing(board,player,(i,j),(-1,0)):
                    validatedList.append((i,j))
                if enclosing(board,player,(i,j),(1,1)):
                    validatedList.append((i,j))
                if enclosing(board,player,(i,j),(-1,1)):
                    validatedList.append((i,j))
                if enclosing(board,player,(i,j),(1,-1)):
                    validatedList.append((i,j))
                if enclosing(board,player,(i,j),(-1,-1)):
                    validatedList.append((i,j))
    return validatedList


# Manipulates the board after a move has been made

def next_state(board,player,pos):
    r,c = pos
    next_player = 0
    direction = []

    # To check if position played is a valid move
    
    if pos in valid_moves(board,player):

        # Checking for the direction the valid move is played in
        
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i == 0 and j == 0:
                    pass
                else:
                    if enclosing(board,player,pos,(i,j)):
                        direction.append((i,j))

        # Loops through all valid directions
        
        for k in range(len(direction)):
            m = 1
            i,j = direction[k]
            row = r + m * i
            col = c + m * j
            
            while board[row][col] != player:
                if player == 1:
                    board[row][col] = 1
                elif player == 2:
                    board[row][col] = 2
                m += 1
                row = r + m * i
                col = c + m * j

        # Sets next player
        
        if player == 1:
            board[r][c] = 1
            if valid_moves(board,2):
                next_player = 2
            
        elif player == 2:
            board[r][c] = 2
            if valid_moves(board,1):
                next_player = 1

    elif valid_moves(board,player) != []:
        board = None

    return (board,next_player)


# Converts user input string to python indices

def position(string):
    
    charLst = ['a','b','c','d','e','f','g','h']
    r = None
    c = None

    if string[0] in charLst and (int(string[1]) > 0 and int(string[1]) <= 8):   
        for i in range(len(charLst)):
            if string[0] == charLst[i]:
                c = i
                break

        r = int(string[1]) - 1
        return (r,c)
    else:
        return None


# Facilitates Multiplayer game

def run_two_players():

    
    player = 1
    flag = True
    board = new_board()

    # Displaying initial board

    validMoves = valid_moves(new_board(),player)

    for ind in range(len(validMoves)):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i,j) == validMoves[ind] and board[i][j] == 0:
                    board[i][j] = '*'

    print_board(board)

    score1,score2 = score(board)
    print("\nSCORES")
    print("Player 1: " + str(score1))
    print("Player 2: " + str(score2))

    print("\nPlayer 1")

    userChoice = input("\nPlease enter a position (q to quit): ")

    # Keep looping till user quits or game finishes

    while userChoice != "q":
        
        pos = position(userChoice)

        if pos is not None:

            board,player = next_state(board,player,pos)

            if board is None:
                print("ERROR")
                flag = False

            # Displays result after game
            
            if player == 0:
                score1,score2 = score(board)
                print("\nSCORES")
                print("Player 1: " + str(score1))
                print("Player 2: " + str(score2))
                if score1 > score2:
                    print("\nPlayer 1 Wins")
                elif score2 > score1:
                    print("\nPlayer 2 Wins")
                else:
                    print("\nIt's a Tie")
                flag = False

            else:

                # Converts all the previous * signifying valid moves to blank spaces

                for i in range(len(board)):
                    for j in range(len(board[i])):
                        if board[i][j] == '*':
                            board[i][j] = 0

                validMoves = valid_moves(board,player)

                for ind in range(len(validMoves)):
                    for i in range(len(board)):
                        for j in range(len(board[i])):
                            if (i,j) == validMoves[ind] and board[i][j] == 0:
                                board[i][j] = '*'
                
                print_board(board)

                # Displays scoreboard

                score1,score2 = score(board)
                print("\nSCORES")
                print("Player 1: " + str(score1))
                print("Player 2: " + str(score2))

                if not flag:
                    break

                print("\nPlayer " + str(player) + "'s turn")

                userChoice = input("\nPlease enter a position (q to quit): ")
                
            
# Facilitates single player game

def run_single_player():

    player = 1
    flag = True

    # Generates Initial board
    
    board = new_board()

    validMoves = valid_moves(new_board(),player)

    for ind in range(len(validMoves)):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i,j) == validMoves[ind] and board[i][j] == 0:
                    board[i][j] = '*'

    print_board(board)

    score1,score2 = score(board)
    print("\nSCORES")
    print("Player 1: " + str(score1))
    print("Player 2: " + str(score2))

    print("\nYour Turn")

    userChoice = input("\nPlease enter a position (q to quit): ")

    # Keeps looping till user quits or game finishes

    while userChoice != "q":    

        if player == 1:

            pos = position(userChoice)

            if pos is not None:

                board,next_player = next_state(board,player,pos)

        elif player == 2:

            for i in range(len(board)):
                    for j in range(len(board[i])):
                        if board[i][j] == '*':
                            board[i][j] = 0

            validmoves = valid_moves(board,player)
            scoreCases = []
            temp_board = copy.deepcopy(board)

            for ind in range(len(validmoves)):
                a,b = validmoves[ind]
                if board[a][b] == 0:
                    temp_board,tempplayer = next_state(temp_board,player,validmoves[ind])
                    s1,s2 = score(temp_board)
                    scoreCases.append(s2)
                    temp_board = copy.deepcopy(board)
                else:
                    scoreCases.append(0)
                    temp_board = copy.deepcopy(board)

            scoreCases1 = sorted(scoreCases, reverse = True)

            for i in range(len(scoreCases)):
                if scoreCases[i] == scoreCases1[0]:
                    board,next_player = next_state(board,player,validmoves[i])
                    break
        

        if board is None:
            print("ERROR")
            flag = False

        player = next_player

        if player == 2:

            for i in range(len(board)):
                    for j in range(len(board[i])):
                        if board[i][j] == '*':
                            board[i][j] = 0

            print_board(board)

            score1,score2 = score(board)
            print("\nSCORES")
            print("Player 1: " + str(score1))
            print("Player 2: " + str(score2))
            
            print("\nCOMPUTER'S TURN")


        elif player == 1:

            validMoves = valid_moves(board,player)

            for ind in range(len(validMoves)):
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        if (i,j) == validMoves[ind] and board[i][j] == 0:
                            board[i][j] = '*'

            print_board(board)

            score1,score2 = score(board)
            print("\nSCORES")
            print("Player 1: " + str(score1))
            print("Player 2: " + str(score2))

            print("\nYour Turn")

            userChoice = input("\nPlease enter a position (q to quit): ")

        else:

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '*':
                        board[i][j] = 0
            print_board(board)
            score1,score2 = score(board)
            print("\nSCORES")
            print("Player 1: " + str(score1))
            print("Player 2: " + str(score2))
            if score1 > score2:
                print("\nPlayer 1 Wins")
            elif score2 > score1:
                print("\nPlayer 2 Wins")
            else:
                print("\nIt's a Tie")
            flag = False

        if not flag:
            break

    
counter = 1
Continue = "yes"
while Continue == "yes":

    if counter != 1:
        Continue = input("Do you want to play again (yes/no): ")
        
    print("\t\t\t\n\nPYTHON ASSIGNMENT 1")
    print("\n\t\t\t\tREVERSI")
    print("\n\n\t\t\t\tMENU")
    print("\n\t\t\t1. Single Player Game")
    print("\n\t\t\t2. Multiplayer Game")
    choice = int(input("\n\n\t\tEnter your choice: "))
    print("\n\n\n\n")

    if choice == 1:
        run_single_player()
    elif choice == 2:
        run_two_players()
    else:
        print("Invalid Choice")

    counter += 1


    
        
    
    


            









    
