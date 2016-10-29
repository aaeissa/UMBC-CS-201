
# Author: Ahmed Eissa
# File:        hw2_part2.py
# Date:        2/15/16
# Section:     07
# UMBC Email:  aeissa2@umbc.edu
# Description: This program transforms pseudocode into a python program that gets a price and quantity from a 
#              user and provides them the total cost 




price = float(input("What is the price of the book? ")) 
amount = int(input("How many copies of this book would you like? "))
order = price * amount 

tax = .065 * order
shipping = 1.95 * amount

total = tax + shipping + order


print("The total cost of your order is: ", total)
