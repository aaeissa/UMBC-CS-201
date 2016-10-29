# File: hw3_part4.py
# Author: Ahmed Eissa
# Date: 2/22/16
# Section:     07
# UMBC Email:  aeissa2@umbc.edu
# Description: This program prompts the user for the temperature (in either Fahrenheint or Celsius) and prints out
# whether water is a liquid, gas, or solid at that temperature. 

def main():

    #obtain the user's temperature and if it's in F or C
    temp = float(input("Please enter the temperature: "))
    unit = input("Please enter 'C' for Celsius, or 'F' for Fahrenheit: ")
    print("\n")

    #For "C" temperatures, water will be solid at or below 0 degrees, a liquid greater than 0 and less than 100
    #degrees,and a gas at and above 100 degrees. 
    if unit == "C":
        if temp <= 0:
            print("At this temperature, water is frozen.")
        elif (temp > 0) and (temp < 100):
            print("At this temperature, water is a liquid.")
        else: 
            print("At this temperature, water is a gas.")


    #For "F" temperatures, water will be solid at or below 32 degrees, a liquid greater than 32 and less than 212
    #degrees, and a gas at and above 212 degrees.
    elif unit == "F":
        if temp <= 32:
            print("At this temperature, water is frozen.")
        elif (temp > 32) and (temp < 212):
            print("At this temperature, water is a liquid.")
        else:
            print("At this temperature, water is a gas.")

    print("\n")


main()
