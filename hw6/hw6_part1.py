
#File: hw6_part1.py
#Author: Ahmed Eissa
#Date: 3-28-16
#Section: 07
#Email: aeissa2@umbc.edu
#Description: This program takes in a list of 8 integers from the user and check to ensure that each integer
#in the list is unique; it then prints the list's contens 


def main():

    #initialize empty list and counter variable
    myList = []
    counter = 0
   
    #keep prompting and checking for input while user attempts are less than 8
    while counter < 8:
        #initialize counter for error check
        checkCounter = 0
        
        #get user input
        listNum = int(input("Please enter a number: "))
       
        #iterate through list elements to check if input matches an existing element
        for i in range(len(myList)):
            #if input matches an existing element, error check counter is increased
            if listNum == myList[i]:
                checkCounter += 1

        #display error message
        if checkCounter > 0:
            print("The number", listNum, "is already in the list.")

        #add user input to the list if it is a unique value 
        else:
            myList.append(listNum)
            counter += 1
                    
    #display list contents
    ("\n")
    print("The contents in the list are: ")
    for i in myList:
        print(i)
    

main()

