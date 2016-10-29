#File: hw6_part2.py
#Author: Ahmed Eissa
#Date: 3-28-16
#Section: 11
#Email: aeissa2@umbc.edu
#Description: This program takes in a number from the user and displays a triangle, square, parallelogram, or
# all three shapes, depending on which option they select.


#Function name: drawTriangle
#Description: prints a triangle of "*" 
#Inputs: input1 
#Outputs: none
def drawTriangle(input1):

    counter = 1
    #print one * per line, increasing by 1 each line until loop count = user input
    while counter <= input1:
        print("*" * counter)
        counter += 1

    return()

#Function name: drawSquare
#Description: prints a square of "*"
#Inputs: input1
#Outputs: none
def drawSquare(input1):

    counter = 0
    #prints an amount of "*" on an amount of lines equal to user input
    while counter < input1:
        print("*" * input1)
        counter += 1
    return()

#Function name: drawParallelogram
#Description: prints a parallelogram of "*"
#Inputs: input1
#Outputs: none
def drawParallelogram(input1):
    
    #prints first line without spaces
    print("*" * input1)
    #prints the original line with one space before it, increasing one additional space per line
    for i in range(1, input1):
        print(" " * i + "*" * input1)

    return()


def main():
    
    #initialize sentinel for loop
    input1 = -1
    
    #get valid input, prompt if invalid
    while input1 <= 0:
        input1 = int(input("Please enter a positive integer: "))

    #initialize sentinel for loop
    shape = "invalid"
    
    #get shape input, prompt if invalid 
    while shape != "triangle" and shape != "parallelogram" and shape != "square" and shape != "all":
        shape = input("Please choose the shape: square, parallelogram, triangle, or all: ")

    #call function to print triangle
    if shape == "triangle":
        drawTriangle(input1)

    #call function to print square
    if shape == "square":
        drawSquare(input1)

    #call function to print parallelogram
    if shape == "parallelogram":
        drawParallelogram(input1)

    #call function to print all 3 shapes
    if shape == "all":
        drawSquare(input1)
        print("\n")
        drawParallelogram(input1)
        print("\n")
        drawTriangle(input1)
        print("\n")

main()
