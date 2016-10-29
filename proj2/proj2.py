#File: proj2.py
#Author: Ahmed Eissa
#Date: 5-9-16
#Section: 11
#Email: aeissa2@umbc.edu
#Description: This program will take in two .txt files - a wordsearch board and a
#list of the words in the wordsearch, and use recursion to find if the words are 
#present in the wordsearch, and if so, where the begin and in what direction they
#are spelled

#Function name: wordSearch
#Description: recursively searches in 8 different directions 
#Inputs: direction, i, rows, j, columns, puzzleList, word, wordIndex
#Outputs: True or False
def wordSearch(direction, i, rows, j, columns, puzzleList, word, wordIndex):

    wordLength = len(word)

    #base case: if the index (attempt counter) is the same as the word length,
    #the word has been found
    if wordLength == wordIndex+1:
        return True
        
    #recursive case: search in all 8 possible directions; check for boundaries (ensure search remains within puzzle);
    #compare the next letter in the given direction with the next letter in the word; call the recursive function or 
    #return False
    else:
            
        if direction == 1:
            if i-1 >= 0 and i-1 <= rows-1 and j-1 >= 0 and j-1 <= columns-1: #North East
                if puzzleList[i-1][j-1] == word[wordIndex+1]:
                    return wordSearch(direction, i-1, rows, j-1, columns, puzzleList, word, wordIndex+1)
                else: 
                    return False
            else: 
                return False 

        elif direction == 2: 
            if i-1 >= 0 and i-1 <= rows-1 and j >= 0 and j <= columns-1: #North
                if puzzleList[i-1][j] == word[wordIndex+1]:
                    return wordSearch(direction, i-1, rows, j, columns, puzzleList, word, wordIndex+1)
                else:
                    return False
            else:
                return False 

        elif direction == 3:
            if i-1 >= 0 and i-1 <= rows-1 and j+1 >= 0 and j+1 <= columns-1: #North West
                if puzzleList[i-1][j+1] == word[wordIndex+1]:
                    return wordSearch(direction, i-1, rows, j+1, columns, puzzleList, word, wordIndex+1)
                else: 
                    return False
            else: 
                return False

        elif direction == 4:
            if i >= 0 and i <= rows-1 and j-1 >= 0 and j-1 <= columns-1:  #West
                if puzzleList[i][j-1] == word[wordIndex+1]:
                    return wordSearch(direction, i, rows, j-1, columns, puzzleList, word, wordIndex+1)
                else: 
                    return False 
            else: 
                return False 

        elif direction == 5:
            if i >= 0 and i <= rows-1 and j+1 >= 0 and j+1 <= columns-1: #East
                if puzzleList[i][j+1] == word[wordIndex+1]:
                    return wordSearch(direction, i, rows, j+1, columns, puzzleList, word, wordIndex+1)
                else:
                    return False
            else: 
                return False 

        elif direction == 6:
            if i+1 >= 0 and i+1 <= rows-1 and j-1 >= 0 and j-1 <= columns-1: #South West
                if puzzleList[i+1][j-1] == word[wordIndex+1]:
                    return wordSearch(direction, i+1, rows, j-1, columns, puzzleList, word, wordIndex+1)
                else: 
                    return False 
            else: 
                return False 

        elif direction == 7:
            if i+1 >= 0 and i+1 <= rows-1 and j >= 0 and j <= columns-1: #South
                if puzzleList[i+1][j] == word[wordIndex+1]:
                    return wordSearch(direction, i+1, rows, j, columns, puzzleList, word, wordIndex+1)
                else: 
                    return False
            else:
                return False 

        elif direction == 8:
            if i+1 >= 0 and i+1 <= rows-1 and j+1 >= 0 and j+1 <= columns-1: #South East 
                if puzzleList[i+1][j+1] == word[wordIndex+1]:
                    return wordSearch(direction, i+1, rows, j+1, columns, puzzleList, word, wordIndex+1)
                else:
                    return False
            else: 
                return False 
def main():

    print("Welcome to the Word Search.")
    print("For this, you will import two files: 1. The puzzle board, and 2. The word list.")

    puzzleFile = input("What is the puzzle file you would like to import? ")
    wordList = input("What is the word list file you would like to import? ")

    puzzleList = [] #this will be the 2d list of the word search
    newList = [] #temporary list to create 2d list
    puzzle = open(puzzleFile, "r")
    puzzleLines = puzzle.readlines()


    for line in puzzleLines:
        stripped = line.strip() #remove white space
        for char in stripped:
            if char != " ": #take out the spaces from the wordsearch
                newList.append(char)

    puzzleList.append(newList)
    newList = [] #emptying the list, rinse and repeat
    
    words = open(wordList, "r")
    wordLines = words.readlines()

    keyList = [] #key words from the .txt file 
    for line in wordLines:
        strippedKeys = line.strip() #remove white space
        keyList.append(strippedKeys)

    
    rows = len(puzzleList) #horizonatal 
    columns = len(puzzleList[0]) #vertical 
    wordIndex = 0 #counter that will be passed in to the recursive function to iterate through words


    for word in keyList: #iterate over words from the relevant .txt file
        
        firstLetter = word[wordIndex] #first letter of the current word; used to begin the recursive search

        for i in range(rows): #iterate over the rows
            for j in range(columns): #iterate over the columns to find an exact location
                if puzzleList[i][j] == firstLetter: #if a letter matches the first letter of the current word, search recursively in all 8 directoins
                    myBool = wordSearch(1, i, rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(2, i ,rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(3, i, rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(4, i, rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(5, i, rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(6, i, rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(7, i, rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(8, i, rows, j, columns, puzzleList, word, wordIndex)
            
            if myBool == False:
            	print("The word", word, "does not appear in the puzzle.")

            elif myBool == True:
            	print("The word", word, "starts in", str(puzzleList[i])+",", str(puzzleList[j]))  

    
    puzzle.close()
    words.close()

main()
