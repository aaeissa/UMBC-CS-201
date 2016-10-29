#File: pallindrome.py
#Author: Ahmed Eissa
#Date: 3-3-16
#Section: 07
#Email: aeissa2@umbc.edu
#Description: This program takes in a string from the user, reverses it, and determines if the string 
#is a pallindrome or not. 

def main():
    sentence = input("Enter a string: ")
    
    newSentence = []
    for c in sentence:
        newSentence.append(c)

    negSentence = []
    for i in newSentence[::-1]:
        negSentence.append(i)
        
    counter = 0    
    for j in range(len(newSentence)):
        if newSentence[j] != negSentence[j]:
            counter == counter
        else:
            counter += 1
        
    if counter == len(newSentence):
        print(sentence, "is a pallindrome.")

    else:
        print(sentence, "is not a pallindrome.")

main()
