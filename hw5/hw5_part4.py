#File: hw5_part4.py
#Author: Ahmed Eissa
#Date: 3-8-16
#Section: 07
#UMBC Email: aeissa2@umbc.edu
#Description: This program is a game that allows students to compete for extra 
#credit points. The program will alternate between two students whow ill take turns
#"taking" points

def main():

	print("Welcome to the Extra Credit Challenge!!!")

	#get input to beging ame
	extraCredit = int(input("Enter the number of points to play for (13-21): "))
	
	#error check to ensure that user selects a valid amount of starting points
	while (extraCredit < 13) or (extraCredit > 21):
		print("Error: You can play for 13-21 points")
		extraCredit = int(input("Enter the number of points to play for (13-21): "))

	#display the start of the game
	print("\n")
	print("Player 2 starts.")

	#initialize varibale to keep track of who wins the game
	counter = 0

	#continue to allow players to take away 1-3 points as long as at least 3 points
	#remain in the game
	while extraCredit >= 3:
		
		print("There are %d points left." % (extraCredit))

		secondNum = int(input("Player 2, how many points do you take? (1-3): "))
		
		#error check that player 2 does not take less or more points than is allowed		
		while (secondNum < 1) or (secondNum > 3):
			print("Error: You can take 1-3 points.")
			secondNum = int(input("Player 2, how many points do you take? (1-3): "))

		print("\n")

		#update amount of points left
		extraCredit -= secondNum

		#if player 2 takes last amount of points, update counter(winning) varibale
		if extraCredit == 0:
			counter += 2
		
		print("There are %d points left." % (extraCredit))

		#allow player 1 to take a turn as long as there are more than 3 points, 
		#else go to the next structure
		if extraCredit >= 3:
			firstNum = int(input("Player 1, how many points do you take? (1-3): "))
				
			#error check that player 2 does not take less or more points than is allowed		
			while (firstNum < 1) or (firstNum > 3):
				print("Error: You can take 1-3 points.")
				firstNum = int(input("Player 1, how many points do you take? (1-3): "))
			
			#update amount of points left
			extraCredit -= firstNum

			#if player 2 takes last amount of points, update counter(winning) varibale
			if extraCredit == 0:
				counter += 1

			print("\n")

	#when there are less than 3 points, only allow players to take 1-2 points per turn
	while (extraCredit > 0) and (extraCredit < 3):
		
		print("There are %d points left." % (extraCredit))
	
		secondNum = int(input("Player 2, how many points do you take? (1-2): "))
		
		#error check to ensure player 2 only takes 1-2 points		
		while (secondNum < 1) or (secondNum > 2):
			print("Error: You can take 1-2 points.")
			secondNum = int(input("Player 2, how many points do you take? (1-2): "))

		#update amount of points left
		extraCredit -= secondNum
		
		#if player 2 takes last amount of points, update counter(winning) varibale
		if extraCredit == 0:
			counter += 2
	
		print("\n")

		print("There are %d points left." % (extraCredit))

		#only allow player 1 a turn if points remain
		while extraCredit > 0:
			firstNum = int(input("Player 1, how many points do you take? (1-2): "))
			
			#error check to ensure that player 1 only takes 1-2 points	
			while (firstNum < 1) or (firstNum > 2):
				print("Error: You can take 1-2 points.")
				firstNum = int(input("Player 1, how many points do you take? (1-2): "))

			#update amount of points left
			extraCredit -= firstNum

			#if player 1 takes last amount of points, update counter(winning) varibale
			if extraCredit == 0:
				counter += 1
		
	#when there are no points left, display who the winner is
	if extraCredit == 0:	
		
		#Player 2 wins
		if counter == 2:
			print("Congratulations! Player 2 has won!!!")
		
		#Player 1 wins
		if counter == 1:
			print("Congratulations! Player 1 has won!!!")

	
main()
