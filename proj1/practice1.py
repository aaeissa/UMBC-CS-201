#File: hw7_part3.py
#Author: Ahmed Eissa
#Date: 4-18-16
#Section: 11
#Email: aeissa2@umbc.edu
#Description: This program allows two users to play the game Tic-Tac-Toe. Player order
#and symbols are randomized, and users are able to save and load games, as well as play
#many games over and over. 


#in order to randomize player order and symbols used 
import random 

#Function name: printBoard
#Description: prints the Tic Tac Toe game board
#Inputs: boardList
#Outputs: None
def printBoard(boardList):
    
    print(boardList[0], "|", boardList[1], "|", boardList [2])
    print("---------")
    print(boardList[3], "|", boardList[4], "|", boardList [5])
    print("---------")
    print(boardList[6], "|", boardList[7], "|", boardList [8])
    print("\n")

#Function name: placeSymbol
#Description: places the user's move onto the game board
#Inputs: move, boardList, symbol
#Outputs: boardList
def placeSymbol(move, boardList, symbol):

    boardList[move-1] = symbol
    printBoard(boardList)
    return(boardList)

#Function name: winnerCheck
#Description: checks to see if a user's move results in that user winning
#Inputs: player, secondPlayer, symbol, symbolTwo, boardList
#Outputs: winner
def winnerCheck(player, secondPlayer, symbol, symbolTwo, boardList):
    
    #initalize empty string variable 
    winner = ""

    #first row 
    if boardList[0] == symbol and boardList[1] == symbol and boardList[2] == symbol:
        winner = player
    elif boardList[0] == symbolTwo and boardList[1] == symbolTwo and boardList[2] == symbolTwo:
        winner = secondPlayer
    
    #second row 
    elif boardList[3] == symbol and boardList[4] == symbol and boardList[5] == symbol:
        winner = player
    elif boardList[3] == symbolTwo and boardList[4] == symbolTwo and boardList[5] == symbolTwo:
        winner = secondPlayer

    #third row 
    elif boardList[6] == symbol and boardList[7] == symbol and boardList[8] == symbol:
        winner = player
    elif boardList[6] == symbolTwo and boardList[7] == symbolTwo and boardList[8] == symbolTwo:
        winner = secondPlayer

    #first column
    elif boardList[0] == symbol and boardList[3] == symbol and boardList[6] == symbol:
        winner = player
    elif boardList[0] == symbolTwo and boardList[3] == symbolTwo and boardList[6] == symbolTwo:
        winner = secondPlayer

    #second column
    elif boardList[1] == symbol and boardList[4] == symbol and boardList[7] == symbol:
        winner = player
    elif boardList[1] == symbolTwo and boardList[4] == symbolTwo and boardList[7] == symbolTwo:
        winner = secondPlayer

    #third column    
    elif boardList[2] == symbol and boardList[5] == symbol and boardList[8] == symbol:
        winner = player
    elif boardList[2] == symbolTwo and boardList[5] == symbolTwo and boardList[8] == symbolTwo:
        winner = secondPlayer

    #diagonal left-to-right    
    elif boardList[0] == symbol and boardList[4] == symbol and boardList[8] == symbol:
        winner = player
    elif boardList[0] == symbolTwo and boardList[4] == symbolTwo and boardList[8] == symbolTwo:
        winner = secondPlayer

    #diagonal right-to-left    
    elif boardList[2] == symbol and boardList[4] == symbol and boardList[6] == symbol:
        winner = player
    elif boardList[2] == symbolTwo and boardList[4] == symbolTwo and boardList[6] == symbolTwo:
        winner = secondPlayer

    return(winner)

#Function name: drawCheck
#Description: checks to see if the user's move results in a draw, which would end the game
#Inputs: boardList
#Outputs: counter
def drawCheck(boardList):

	#if the board is completely full (and thus hasn't resulted in a winner), the counter should equal 9
    counter = 0
    for item in boardList:
        if item == "O" or item == "X":
            counter += 1
    
    return(counter)

#Function name: moveCheck
#Description: checks to see if the user is attempting to place their symbol where a symbol already exists
#Inputs: move, boardList
#Outputs: True or False 
def moveCheck(move, boardList):
    
    if boardList[move-1] == "O" or boardList[move-1] == "X":
        return False
    else:
        return True  

#Function name: saveGame
#Description: writes the current board, player, and symbol to a .txt file
#Inputs: boardList, player, symbol
#Outputs: saved
def saveGame(boardList, player, symbol):
    
    results = open("tic.txt", "w")
                
    for item in boardList:
        results.write(item)
                
    results.write(player)
    results.write(symbol)

    print("File Saved.")
    saved = True
    results.close()

    return(saved)

#Function name: loadGame
#Description: reads in the game board, last player and their symbol from a .txt file
#Inputs: boardList
#Outputs: boardList, lastPlayer, lastSymbol, loaded
def loadGame(boardList):
    
    results = open("tic.txt", "r")
    savedGame = results.read()

    #create new List to match existing game board format
    newList = []
    for line in savedGame:
        for c in line:
            newList.append(c)

    #first nine characters of the .txt file will be the game board
    boardLength = len(newList) - 2
    for i in range(0, boardLength):
        boardList[i] = newList[i]
        
    #second to last character of the .txt file will be the last player
    lastPlayer = newList[9]   
    #last character of the .txt file will be the last symbol  
    lastSymbol = newList[10]   

    loaded = True

    return(boardList, lastPlayer, lastSymbol, loaded)


def main():

    playAgain = "yes"

    #game will continue to play as long as user enters a variant of "yes" (when the game is over)
    while playAgain != "no" and  playAgain != "No" and playAgain != "NO" and playAgain != "n" and playAgain != "N":

        print("Welcome to Tic-Tac-Toe.\nThis is for two players.")
       
        #to get a random player between 1 and 2
        player = random.randint(1,2)

        #match players with their turns 
        if player == 1:
            player = "1"
            secondPlayer = "2"
        elif player == 2:
            player = "2"
            secondPlayer = "1"
    
    	#to get a random symbol between 1 and 2
        symbol = random.randint(1, 2)
    
    	#match the players with their symbols 
        if symbol == 1:
            symbol = "O"
            symbolTwo = "X"
        elif symbol == 2:
            symbol = "X"
            symbolTwo = "O"


        print("Player " + player + " will go first and will play with the " + symbol + ".")

        #initialize empty board
        boardList = [0] * 9
        counter = 1
    
    	#fill empty game board 1-9
        for i in range(len(boardList)):
            boardList[i] = str(counter)
            counter += 1

        printBoard(boardList)
        winnerVar = ""
        winner = ""
        drawVar = 0
        fullBoard = 9
        saved = False
        loaded = False

        #allow players to take turns if there is no winner, draw, or the game is not saved
        while winner != player and winner != secondPlayer and drawVar != 9 and saved != True:

            #first turn
            print("Player " + player + " what is your choice?")
            move = int(input("(1-9) or -1 to save or -2 to load: "))
            
            #input validation
            while move < -2 or move > 9:
                print("Player " + player + " what is your choice?")
                move = int(input("(1-9) or -1 to save or -2 to load: "))

            #loading the game
            if move == -2:
                boardList, lastPlayer, lastSymbol, loaded = loadGame(boardList)
                
                #matching the player order from the last game
                player = lastPlayer
                if player == "1":
                    secondPlayer = "2"
                elif player == "2":
                    secondPlayer = "1" 

                #matching the symbol order from the last game
                symbol = lastSymbol
                if symbol == "X":
                    symbolTwo = "O"
                elif symbol == "O":
                    symbolTwo = "X"

                print("Game loaded.")
                printBoard(boardList)

                #once a game is loaded, give the last player a turn
                if loaded == True:
                    print("Player " + player + " what is your choice?")
                    move = int(input("(1-9) or -1 to save or -2 to load: "))
                    
                    while move < -2 or move > 9:
                        print("Player " + player + " what is your choice?")
                        move = int(input("(1-9) or -1 to save or -2 to load: "))

                    #save game    
                    if move == -1:
                        saved = saveGame(boardList, player, symbol)
                    #check 
                    else:
                        moveVar = moveCheck(move, boardList)
                        #reprompt user for a valid, empty space                       
                        while moveVar == False:
                            print("That space is already taken.")
                            move = int(input("(1-9) or -1 to save or -2 to load: "))
                            moveVar = moveCheck(move, boardList)
            
            #saving the game
            elif move == -1:
                saved = saveGame(boardList, player, symbol)   
            
            #checking to ensure that player chose an empty space        
            else:
                moveVar = moveCheck(move, boardList)
                #reprompt user for a valid, empty space
                while moveVar == False:
                    print("That space is already taken.")
                    move = int(input("(1-9) or -1 to save or -2 to load: "))
                    moveVar = moveCheck(move, boardList)

            #if the user is not saving or loading, place their move on the board and check to see if it's a winning/tying move    
            if move != -1 and move != -2:    
                boardList = placeSymbol(move, boardList, symbol)
                winnerVar = winnerCheck(player, secondPlayer, symbol, symbolTwo, boardList)
            
            #if the move was a winning move, reassign the proper variables
            if winnerVar == player:
                winner = player
                print("Player " + winner + " wins.")
            
            elif winner != player:
                drawVar = drawCheck(boardList)
                if drawVar == fullBoard:
                    print("The game results in a draw.")
                
            #conditions for the second turn to happen
            if winner != player and drawVar != fullBoard and saved != True: 	
        	
                print("Player " + secondPlayer + " what is your choice?")
                move = int(input("(1-9) or -1 to save or -2 to load: "))

                #input validation 
                while move < -2 or move > 9:
                    print("Player " + secondPlayer + " what is your choice?")
                    move = int(input("(1-9) or -1 to save or -2 to load: "))
             
                #loading the game                                                                                                                                                                                     
                if move == -2:
                    boardList, lastPlayer, lastSymbol, loaded = loadGame(boardList)

                    #matching the player order from the last game
                    player = lastPlayer
                    if player == "1":
                        secondPlayer = "2"
                    elif player == "2":
                        secondPlayer = "1"

                    #matching the symbol order from the last game
                    symbol = lastSymbol
                    if symbol == "X":
                        symbolTwo = "O"
                    elif symbol == "O":
                        symbolTwo = "X"

                    print("Game loaded.")
                    printBoard(boardList)

                    #allow the last player to have their turn
                    if loaded == True:
                        print("Player " + player + " what is your choice?")
                        move = int(input("(1-9) or -1 to save or -2 to load: "))
                        while move < -2 or move > 9:
                            print("Player " + player + " what is your choice?")
                            move = int(input("(1-9) or -1 to save or -2 to load: "))

                    #allow player to save the game
                    if move == -1:
                        saved = saveGame(boardList, player, symbol)

                   	#check 
                    else:
                        moveVar = moveCheck(move, boardList)
                        #reprompt user for a valid, empty space                       
                        while moveVar == False:
                            print("That space is already taken.")
                            move = int(input("(1-9) or -1 to save or -2 to load: "))
                            moveVar = moveCheck(move, boardList)

                #save game
                if move == -1:
                    saved = saveGame(boardList, secondPlayer, symbolTwo)

                #checking to ensure that player chose an empty space        
                else:
                    moveVar = moveCheck(move, boardList)
                    #reprompt user for a valid, empty space
                    while moveVar == False:
                        print("That space is already taken.")
                        move = int(input("(1-9) or -1 to save or -2 to load: "))
                        moveVar = moveCheck(move, boardList)

                #if user is not saving or loading, place their symbol on the game board and check to see if it wins/ties the game
                if move != -1 and move != -2:
                    boardList = placeSymbol(move, boardList, symbolTwo)
                    winnerVar = winnerCheck(player, secondPlayer, symbol, symbolTwo, boardList)

                #reassign variables to display winner
                if winnerVar == secondPlayer:
                    winner = secondPlayer
                    print("Player " + winner + " wins.")

                #reassign variables to display draw
                if winner != secondPlayer:
                    drawVar = drawCheck(boardList)
                    if drawVar == fullBoard:
                        print("The game results in a draw.")



        #variable to determine whether or not to loop game over again               
        playAgain = input("Play again? ")

        if playAgain == "no" or playAgain == "No" or playAgain == "NO" or playAgain == "n" or playAgain == "N":
            print("Thank you for playing.")
main()
