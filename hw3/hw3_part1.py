# File: hw3_part1.py
# Author: Ahmed Eissa
# Date: 2/22/16
# Section:     07
# UMBC Email:  aeissa2@umbc.edu
# Description: This program will take in a floating point number from the user and say whether the number is posit# ive, negative, or zero.  

def main():
  
    #gets input - a float - from the user
    number1 = float(input("Please enter a floating point number: "))
    
    #checks to see if the input is zero
    if number1 == 0.0:
        print("The number", number1, "is equal to zero.")

    #checks to see if the input is positive 
    if number1 > 0: 
        print("The number", number1, "is positive.")
    
    #checks to see if the input is negative
    if number1 < 0:
        print("The number", number1, "is negative.")
    
    print("\n")

main()
