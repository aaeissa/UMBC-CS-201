#File: hw4_part5.py
#Author: Ahmed Eissa
#Date: 2/29/16
#Section: 07
#Email: aeissa2@umbc.edu
#Description: This program prints the numbers from 1 to 100 (inclusive), but prints a pre-written string in cases
#where the number is divisible by 3, 5, and both 3 and 5. 

def main():

    num = 100
    
    #iterate through 100, inclusive
    for i in range(1, num+1, 1):
        #print the respective pre-written string if the number is divisible by 3, 5, or both 3 and 5
         if (i % 3 == 0) and (i % 5 == 0):
            print("In the future, everyone will be world famous in 15 minutes.")

        elif i % 3 == 0:
            print("Better three hours too soon that a minute too late.")
      
        elif i % 5 == 0:
            print("Where do you see yourself in five years?")
        
        #print the number if it is not divisible by 3 or 5
        else:
            print(i)


main()
