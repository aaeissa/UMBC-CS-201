
def wordSearch(puzzleList, word, wordIndex):

	currentLetter = word[wordIndex] #this is initially passed in as 0
	wordLength = len(word)
	direction = ""

	if wordLength == wordIndex+1:
		return (direction)


	rows = len(puzzleList) #12 in this example 
	columns = len(puzzleList[0]) #12 in this example

	for i in range(rows):
		for j in range(columns):
			if puzzleList[i][j] == currentLetter:
				
				if i-1 >= 0 and i-1 <= rows-1 and j-1 >= 0 and j-1 <= columns-1: 
					if puzzleList[i-1][j-1] == word[wordIndex+1]:
						direction = "NW"
						wordSearch(puzzleList, word, wordIndex+1)
                                
				if i-1 >= 0 and i-1 <= rows-1 and j >= 0 and j <= columns-1:
					if puzzleList[i-1][j] == word[wordIndex+1]:
						direction = "N" 
						wordSearch(puzzleList, word, wordIndex+1)

				if i-1 >= 0 and i-1 <= rows-1 and j+1 >= 0 and j+1 <= columns-1: 
                                        if puzzleList[i-1][j+1] == word[wordIndex+1]:
						direction = "NE"
						wordSearch(puzzleList, word, wordIndex+1)

				if i >= 0 and i <= rows-1 and j-1 >= 0 and j-1 <= columns-1: 
                                        if puzzleList[i][j-1] == word[wordIndex+1]:
						direction = "W"
						wordSearch(puzzleList, word, wordIndex+1)
		
				if i >= 0 and i <= rows-1 and j+1 >= 0 and j+1 <= columns-1: 
                                        if puzzleList[i][j+1] == word[wordIndex+1]:
						direction = "E"
						wordSearch(puzzleList, word, wordIndex+1)

				if i+1 >= 0 and i+1 <= rows-1 and j-1 >= 0 and j-1 <= columns-1: 
                                        if puzzleList[i+1][j-1] == word[wordIndex+1]:
						direction = "SW"
                                                wordSearch(puzzleList, word, wordIndex+1)

				if i+1 >= 0 and i+1 <= rows-1 and j >= 0 and j <= columns-1: 
                                        if puzzleList[i+1][j] == word[wordIndex+1]:
						direction = "S"
                                                wordSearch(puzzleList, word, wordIndex+1)

				if i+1 >= 0 and i+1 <= rows-1 and j+1 >= 0 and j+1 <= columns-1: 
                                        if puzzleList[i+1][j+1] == word[wordIndex+1]:
						direction = "SE"
                                                wordSearch(puzzleList, word, wordIndex+1)

	return()

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

	puzzleLen = len(puzzleList) #length of the puzzle, total number of rows

	words = open(wordList, "r")
	words = words.readlines()

	keyList = [] #key words from the .txt file 
	for line in words:
		strippedKeys = line.strip()
		keyList.append(strippedKeys)

	numKeys = len(keyList) #amount of key words in the puzzle

	wordIndex = 0
	direction = ""
	for word in keyList:
		direction = wordSearch(puzzleList, word, wordIndex)
		print(word, direction)
		
	

main()

#We have recommended that when coding up Project 2, 
#students break finding the word into two parts: 
#1) finding the first letter of the word, and 
#2) searching for the word in the eight different directions, starting at that point.  
#Only the second function needs to be recursive -- 
#the first may be accomplished using for loops instead.
