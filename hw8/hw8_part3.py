#File: hw8_part3.py
#Author: Ahmed Eissa
#Date: 4-25-16
#Section: 11
#Email: aeissa2@umbc.edu
#Description: This program opens and reads the file input.txt and uses a recursive
#function to create a list of unique characters

#Function name: newChar
#Description: a recursive function that appends unique characters from a text file 
#into a list
#Inputs: stripped, charList, index
#Outputs: charList 
def newChar(stripped, charList, index):
    
    #base case - when the the index/counter is at the end of the string
    if index == len(stripped):
        return charList

    #recursive call - append a character to the list if it's not in it,
    #increment through the string recursively
    else:
        if stripped[index] not in charList:
            charList.append(stripped[index])
        return newChar(stripped, charList, index+1)
            
def main():

    myFile = open("input.txt", "r")
    stripped = myFile.read() #string from the text file
    charList = []
    index = 0 #counter

    charList = newChar(stripped, charList, index)

    print(charList)

    myFile.close()

main()
