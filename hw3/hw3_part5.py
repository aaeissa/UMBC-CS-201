# File: hw3_part5.py
# Author: Ahmed Eissa
# Date: 2/22/16
# Section:     07
# UMBC Email:  aeissa2@umbc.edu
# Description: This program assumes that a month begins on a Monday and tells a user which day of the week any 
# given day of the month is on. 


def main():

    #obtain day of the month from the user
    day = int(input("Please enter the day of the month: "))
    
    #days must be a part of a 31-day month, or else input is invalid 
    if (day <= 0) or (day > 31):
        print("Invalid day.\n")
    
    #the first day of the month is a Monday; any other day mod 7 with a remainder of 1 is also a Monday
    elif (day == 1) or (day % 7 == 1):
        print("Today is Monday!\n")

    #the second day of the month is a Tuesday; any other day mod 7 with a remainder of 2 is also a Tuesday
    elif (day == 2) or (day % 7 == 2):
        print("Today is Tuesday!\n")

    #the third day of the month is a Wednesday; any other day mod 7 with a remainder of 3 is also a Wednesday
    elif (day == 3) or (day % 7 == 3): 
        print("Today is Wednesday!\n")

    #the fourth day of the month is a Thursday; any other day mod 7 with a remainder of 4 is also a Thursday
    elif (day == 4) or (day % 7 == 4):
        print("Today is Thursday!\n")
        
    #the fifth day of the month is a Friday; any other day mod 7 with a remainder of 5 is also a Friday
    elif (day == 5) or (day % 7 == 5):
        print("Today is Friday!\n")
        
    #the sixth day of the month is a Saturday; any other day mod 7 with a remainder of 6 is also a Saturday
    elif (day == 6) or (day % 7 == 6):
        print("Today is Saturday!\n")

    #the seventh day of the month is a Sunday; any other day mod 7 with a remainder of 0 is also a Sunday
    elif (day == 7) or (day % 7 == 0):
        print("Today is Sunday!\n")

main()
