#File: hw8_part2.py
#Author: Ahmed Eissa
#Date: 4-25-16
#Section: 11
#Email: aeissa2@umbc.edu
#Description: This program gets input from the user to print a hollow square using 
#a recursive function

#Function name: hollowSquare
#Description: a recursive function that prints a hollow square with the user's height
#and chosen character
#Inputs: sqHeight, sqChar, coutner
#Outputs: None
def hollowSquare(sqHeight, sqChar, counter):

    #base case - printing the first row of the square
    if counter == 1:
        print(sqHeight*sqChar)

    #recursive call - printing the last/bottom line of the square, then decrement
    elif counter == sqHeight:
        print(sqHeight*sqChar)
        hollowSquare(sqHeight, sqChar, counter-1)
        
    #recursive call - printing the middle "hollowed" rows of the square, then decrement
    else: 
        print(sqChar+" "*(sqHeight-2)+sqChar)
        hollowSquare(sqHeight, sqChar, counter-1)
    

def main():

    sqHeight = int(input("Please enter the height of your square: "))

    #validate input
    while sqHeight <= 0:
        sqHeight = int(input("Please enter the height of your square (must be > 0): "))
    
    sqChar = input("Please enter a character for your square: ")

    counter = sqHeight

    hollowSquare(sqHeight, sqChar, counter)

main()
