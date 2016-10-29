#File: hw4_part4.py
#Author: Ahmed Eissa
#Date: 2/29/16
#Section: 07
#Email: aeissa2@umbc.edu
#Description: This program will count the number of vowels that appear in a string and display that number 

def main():
    
    #get input/user's string
    userString = input("Please enter a string: ")

    counter = 0
    
    #iterate through each character in the strong to check if the character is a vowel 
    for i in userString:
        if (i=='a') or (i=='e') or (i=='i') or (i=='o') or (i=='u') or (i=='y') or (i=="A") or (i=="E") or (i=="I") or (i=="O") or (i=="U") or (i=="Y"):
            #if character is a vowel, increment counter
            counter = counter + 1

    print("There are %d vowels in the string '%s'" % (counter, userString))

main()
