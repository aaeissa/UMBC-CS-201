# File: hw3_part3.py
# Author: Ahmed Eissa
# Date: 2/22/16
# Section:     07
# UMBC Email:  aeissa2@umbc.edu
# Description: This program is a simple "Guess Who"-like game which narrows down and identifies the user's 
# character after a series of questions

def main():

    #the first question presented to the user will divide the man/woman possibilities in half 
    woman = str(input("Is your character a woman? (y/n): "))

    #if the character is a woman, they will be prompted about the eye color, which will result in one of two 
    #possible characters 
    if woman == "y":
        eyes = str(input("Does your character have blue eyes? (y/n): "))

        if eyes == "y":
            print("Your character is Jane!")
        
        else: 
            print("Your character is Marni!")

    #if the character is not a woman, they will be prompted about whether or not the character has eye glasses, 
    #which only one character wears
    if woman == "n":
        glasses = str(input("Does your character wear glasses? (y/n): "))

        if glasses == "y":
            print("Your character is Adrian!")
        
        #if the character does not wear glasses, the user will be prompter about whether or not the character has
        #a beard, which only one remaining character has. 
        elif glasses == "n":
            beard = str(input("Does your character have a beard? (y/n): "))

            if beard == "y":
                print("Your character is Peder!")
            
            else: 
                print("Your character is Zhang!")

main()
