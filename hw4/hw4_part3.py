#File: hw4_part3.py
#Author: Ahmed Eissa
#Date: 2/29/16
#Section: 07
#Email: aeissa2@umbc.edu
#Description: This program calculates the total cost of all donations raised for a the Polar Bear Plunge charity 
#event by asking for the number of donations, the value of each donation, and the number of total plunges

def main():
    
    #get input/number of pledging donators 
    numPledges = int(input("How many pledges did you get? "))
    
    #initialize a donation counter 
    totalDonations = 0
    
    #iterate through the range of total pledges 
    for i in range (1, numPledges+1): 
        #get value of each individual pledge
        donation = float(input("What is the value of donation %d? " % (i)))
        #add the input to the total amount
        totalDonations += donation

    #get input/number of total plunges
    numPlunges = int(input("How many plunges did you do? "))

    finalDonations = 0
    
    #iterate through range of plunges to calculate total donation amount
    for j in range (1, numPlunges+1):
        finalDonations += totalDonations

    print("Based on your", numPlunges, "plunges you earned $%f for the charity." % (finalDonations))


main()
