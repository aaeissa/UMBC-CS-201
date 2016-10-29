#File: hw8_part1.py
#Author: Ahmed Eissa
#Date: 4-25-16
#Section: 11
#Email: aeissa2@umbc.edu
#Description: This program gets a list of integers from the user and uses a recursive
#function to identify the maximum value in the list

#Function name: maxInt
#Description: a recursive function that gets the maximum integer from a lsit
#Inputs: intList
#Outputs: intList (maxVar in recursive calls)
def maxInt(intList):

	#base case - when the length of the list is one
    if len(intList) == 1:
        return intList[0]
    

    elif len(intList) > 1:
    	#recursive call with the list at the next position
        maxVar = maxInt(intList[1:])
        
        #compare it against the element at the first index
        if maxVar > intList[0]:
            return(maxVar)
            
        else:
            return(intList[0])

def main():

    intList = []
    userInput = 0
    
    #validate input
    while userInput != -1:
        userInput = int(input("Enter a number to append to the list, or -1 to stop: "))
        if userInput != -1:
        	intList.append(userInput)
    
    listMax = maxInt(intList)

    print("The list you entered is: ", intList)
    print("The maximum value in the list is: ", listMax)

main()
