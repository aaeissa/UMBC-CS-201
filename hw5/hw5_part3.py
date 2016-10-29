#File: hw5_part3.py
#Author: Ahmed Eissa
#Date: 3-8-16
#Section: 07
#UMBC Email: aeissa2@umbc.edu
#Description: This program will take in a standard phone number from the user and 
#print it back out in a standard format

def main():

	#get input from user
	phoneNum = input("Please enter the phone number: ")
	
	#initialize empty string
	newNum = ""

	#iterate through phoneNum, only adding the numbers provided into the new strong
	for c in phoneNum:
		#add character from original string to new string only if it does not contain
		#a non-numerical character
		if (c != "(") and (c != ")") and (c != "-"):
			newNum += c

	#display the number to the user in the standardized format
	print("("+newNum[0]+newNum[1]+newNum[2]+") "+newNum[3]+newNum[4]+newNum[5]+"-"+newNum[6]+newNum[7]+newNum[8]+newNum[9])

main()
