
# Author: Ahmed Eissa
# File:        hw2_part3.py
# Date:        2/15/16
# Section:     07
# UMBC Email:  aeissa2@umbc.edu
# Description: This program takes a price from the user and separates it into dollars and cents



price = float(input("What is the price? "))

dollar = int(price)

cents = (price - dollar) 

print("The number of dollars is: ", dollar)
print("The number of cents is: %.2f" % cents)
