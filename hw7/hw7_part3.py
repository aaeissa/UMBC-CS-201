#File: hw7_part3.py
#Author: Ahmed Eissa
#Date: 4-4-16
#Section: 11
#Email: aeissa2@umbc.edu
#Description: This program reads in a .txt or .dat file and counts the total words, 
#average word length, and total amount of sentences. 


def main():

	#get input from user
	fname = input("Please enter the name of the file to open: ")
	

	lengthVar = len(fname) - 4

	#error check to ensure that user input is a ".txt" or ".dat" file
	#reprompt if invalid input
	while fname[lengthVar:] != ".txt" and fname[lengthVar:] != ".dat":
		print("\tThe file must end in .txt or .dat to be valid.")
		fname = input("\tPlease enter the name of the file to open: ")
		lengthVar = len(fname) - 4

	#open file, read mode
	file = open(fname, "r")
	#read in all file lines
	openFile = file.readlines()

	numLines = 0
	numWords = 0
	numChars = 0
	
	for line in openFile:
		line = line.strip() #remove all white space from line when it's a string
		wordsList = line.split() #remove all white space
		numWords += len(wordsList) #get length of words list

		#iterate over each word in the lists that were made from the file's lines		
		for word in wordsList:
			#count characters in each word 
			for char in word:
				numChars += 1
		
		#count total number of periods, as a metric for counting total sentences
		for char in line:
			if char == ".":  
				numLines += 1

	#average character count in each word 	
	averageLength = numChars / numWords

	#display total word count, average word length, and total sentence count to user
	print("\n")
	print("The file", fname, "has", numWords, "words in it.")
	print("On avergae, each word is", averageLength, "characters long.")	
	print("There are", numLines, "sentences in the file.")
	
	#close the open/read file
	file.close()

main()
