#File: hw4_part2.py
#Author: Ahmed Eissa
#Date: 2/29/16
#Section: 07
#Email: aeissa2@umbc.edu
#Description: This program will output every third letter from a string given by a user

def main():
     
     #get user string
     userSentence = input("Please enter a sentence: ")
     
     #set user string as a list of characters
     sentenceList = list(userSentence) 

     #display original string to user
     print("Original sentence:\n%s" % (userSentence))
     print("Every third letter:")

     #get length of string; if the character's "position" (sequential number in the list) is divisible by 3, print
     #the character
     for i in range(len(sentenceList)):
         if (i % 3) == 0:
             print(sentenceList[i], end = "")

     print("\n")


main()
