
def wordSearch(direction, i, rows, j, columns, puzzleList, word, wordIndex):

    wordLength = len(word)
 
    if wordLength == wordIndex+1:
        found = True
        return(found)
        
 
    if puzzleList[i][j] == word[wordIndex+1]:
        print("something")

        if direction == 1:
            if i-1 >= 0 and i-1 <= rows-1 and j-1 >= 0 and j-1 <= columns-1: #NE
                wordSearch(direction, i-1, rows, j-1, columns, puzzleList, word, wordIndex+1)
                
        if direction == 2: 
            if i-1 >= 0 and i-1 <= rows-1 and j >= 0 and j <= columns-1: #N
                wordSearch(direction, i-1, rows, j, columns, puzzleList, word, wordIndex+1)
                
        if direction == 3:
            if i-1 >= 0 and i-1 <= rows-1 and j+1 >= 0 and j+1 <= columns-1: #NW 
                wordSearch(direction, i-1, rows, j+1, columns, puzzleList, word, wordIndex+1)

        if direction == 4:
            if i >= 0 and i <= rows-1 and j-1 >= 0 and j-1 <= columns-1:  #W
                wordSearch(direction, i, rows, j-1, columns, puzzleList, word, wordIndex+1)
                
        if direction == 5:
            if i >= 0 and i <= rows-1 and j+1 >= 0 and j+1 <= columns-1: #E
                wordSearch(direction, i, rows, j+1, columns, puzzleList, word, wordIndex+1)

        if direction == 6:
            if i+1 >= 0 and i+1 <= rows-1 and j-1 >= 0 and j-1 <= columns-1: #SW 
                wordSearch(direction, i+1, rows, j-1, columns, puzzleList, word, wordIndex+1)

        if direction == 7:
            if i+1 >= 0 and i+1 <= rows-1 and j >= 0 and j <= columns-1: #S
                wordSearch(direction, i+1, rows, j, columns, puzzleList, word, wordIndex+1)

        if direction == 8:
            if i+1 >= 0 and i+1 <= rows-1 and j+1 >= 0 and j+1 <= columns-1: #SE 
                wordSearch(direction, i+1, rows, j+1, columns, puzzleList, word, wordIndex+1)


    else:
        found = False
        return(found)



def main():

    print("Welcome to the Word Search.")
    print("For this, you will import two files: 1. The puzzle board, and 2. The word list.")

    puzzleFile = input("What is the puzzle file you would like to import? ")
    wordList = input("What is the word list file you would like to import? ")

    puzzleList = [] #this will be the 2d list of the game board/word search
    newList = [] #temporary list to create 2d list
    puzzle = open(puzzleFile, "r")
    puzzle = puzzle.readlines()

    for line in puzzle:
        stripped = line.strip()

        for char in stripped:
            if char != " ":
                newList.append(char)

    puzzleList.append(newList)
    newList = [] #emptying the list, rinse and repeat
    
    words = open(wordList, "r")
    words = words.readlines()

    keyList = [] #key words from the .txt file 
    for line in words:
        strippedKeys = line.strip()
        keyList.append(strippedKeys)

    
    rows = len(puzzleList)
    columns = len(puzzleList[0])
    wordIndex = 0


    for word in keyList:
        
        firstLetter = word[wordIndex]

        for i in range(rows):
            for j in range(columns):
                if puzzleList[i][j] == firstLetter: 
                    myBool = wordSearch(1, i, rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(2, i ,rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(3, i, rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(4, i, rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(5, i, rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(6, i, rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(7, i, rows, j, columns, puzzleList, word, wordIndex)
                    myBool = wordSearch(8, i, rows, j, columns, puzzleList, word, wordIndex)

        print(myBool)
main()
