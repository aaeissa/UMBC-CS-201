
#File: hw6_part2.py
#Author: Ahmed Eissa
#Date: 3-28-16
#Section: 11
#Email: aeissa2@umbc.edu
#Description: This program creates a list of integers from 2 to 500. It then removes all multiples of the 
#integers 2 through 25, and finaly prints the list's contents, which are only prime numbers 

def main():
	
	#initialize empty list and the list's maximum range
	primeList = []
	maxNum = 500

	#add the all integers including and between 2 and 500 to the empty list
	for i in range(2, maxNum+1):
		primeList.append(i)
		
	#counter will be the variable that represents the multiples we will remove from the list
	counter = 2
	
	#only check for multiples up to 25
	while counter < 26:

		#iterate through list to remove multiples of 2-25
		for i in primeList:
			#if list element divides evenly by the counter, remove it from the list
			if i % counter == 0 and i != counter:
				primeList.remove(i)
		counter += 1

	
	#initialize empty string
	myString = ""
	
	#add integers from primeList into string format to display to the user
	for i in primeList:
		myString += str(i) + " "

	#display prime numbers to the user
	print(myString)
	
main()

