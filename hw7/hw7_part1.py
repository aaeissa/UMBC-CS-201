#File: hw7_part1.py
#Author: Ahmed Eissa
#Date: 4-4-16
#Section: 11
#Email: aeissa2@umbc.edu
#Description: This program takes in a phone number from the user which can consist
# of letter and numbers, and returns the phone number in only numbers


#Function name: convertLetter
#Description: converts an alpha-numeric phone number to a numeric phone number
#Inputs: phoneNum 
#Outputs: finalNum
def convertLetter(phoneNum):

	#capitalize all letters (if any) in the phone number
    upperNum = phoneNum.upper()
    finalNum = ""
    
    for i in upperNum:
        
        #if element is a number, add it to the final phone number
        if i.isdigit() == True:
            finalNum += i
        
        #the following if-elif statements are based upon a traditional phone's "dial pad"
        #where there are three to four numbers per number 
        elif i == "A" or i == "B" or i == "C":
            finalNum += "2"
        
        elif i == "D" or i == "E" or i == "F":
            finalNum += "3"

        elif i == "G" or i == "H" or i == "I":
            finalNum += "4"

        elif i == "J" or i == "K" or i == "L":
            finalNum += "5"

        elif i == "M" or i == "N" or i == "O":
            finalNum += "6"

        elif i == "P" or i == "Q" or i == "R" or i == "S":
            finalNum += "7"
        
        elif i == "T" or i == "U" or i == "V":
            finalNum += "8"

        elif i == "W" or i == "X" or i == "Y" or i == "Z":
            finalNum += "9"

        #include hyphens in the final phone number
        elif i == "-":
            finalNum += i
            

    return(finalNum)



def main():

    print("Welcome to the Telephone Converter.\n")
    
    #get input from user
    phoneNum = input("Enter the phone number: ")

    #call function and catch its return value
    finalNum = convertLetter(phoneNum)

    print(finalNum+"\n")
    

main()
