#File: hw4_part1.py
#Author: Ahmed Eissa
#Date: 2/29/16
#Section: 07
#Email: aeissa2@umbc.edu
#Description: This program takes in two integers as input from the user and creates a multiplication table 

def main():

   #getting input; the first number is which number will be used to mulitply by, the second number
   #will be how far the table will go
   first_int = int(input("Enter the base number: "))
   second_int = int(input("Enter the max number: "))

   #this for loop takes the first number and multiplies it by every number from 0 through the second number
   for num in range(second_int + 1):
       print("%d*%d=%d" % (first_int, num, first_int*num))

main()
