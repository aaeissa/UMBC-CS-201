#File: hw5_part1.py
#Author: Ahmed Eissa
#Date: 3-8-16
#Section: 07
#Email: aeissa2@umbc.edu
#Description: This program calculates the appropriate tip for a person at a restaurant based upon the level of service provided by the waiter/waitress 


def main():
    
    #get user input 
    bill = float(input("What is the total bill? "))
    service = input("What was the level of service?\n(Please choose excellent, good, or bad): ")
    
    #continue to prompt user for level of service if they do not correctly input one of three possible choices
    while (service != "excellent") and (service != "good") and (service != "bad"):
        service = input("What was the level of service?\n(Please choose excellent, good, or bad): ")

    #display bill total and level of service to user
    print("The bill was $%.3f" % (bill))
    print("The service was", service)
    
    #excellent service is a 25% tip; good service is a 20% tip; bad service is a 10% tip
    if service == "excellent":
        tip = bill * .25
    if service == "good":
        tip = bill * .20
    if service == "bad":
        tip = bill * .10
    
    #because tip must be $2 minimum, it is automatically set to $2 if the calcualted tip is less than $2 
    if tip < 2:
        tip = 2

    #display tip to user
    print("The tip is $%.3f" % (tip))

    grandTotal = bill + tip

    #display total inlcuding bill and tip to user
    print("The grand total with tip is $%.3f" % (grandTotal))
 
main()
