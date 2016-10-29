# File: hw3_part2.py
# Author: Ahmed Eissa
# Date: 2/22/16
# Section:     07
# UMBC Email:  aeissa2@umbc.edu
# Description: This program takes multiple inputs from the user in order to create a weighted-grade calculator 

def main():

    #the user will provide inputs for the weight their class assigns to homeworks/exams/discussion and the grades
    #they received for their homeworks/exams/discussions
    hw_weight = float(input("Please enter the homework weight: "))
    hw_grade = float(input("Please enter the homework grade: "))
    exam_weight = float(input("Please enter the exam weight: "))
    exam_grade = float(input("Please enter the exam grade: "))
    disc_weight = float(input("Please enter the dsicussion weight: "))
    disc_grade = float(input("Please enter the discussion grade: "))

    #the user's grade in the class will be the sum of their individual grades multiplied by the respective weight
    total = (hw_weight * hw_grade) + (exam_weight * exam_grade) + (disc_weight * disc_grade)

    print("The final numerical grade is: ", total)

    #the following if-elif structure checks to see if the user has an earned an A, B, C, D, or F in the class - 
    #the parameters for the grades have been set by their course
    if total >= 90:
        print("This earns you an A in the class.")
        
    elif (total >= 80) and (total < 90):
        print("This earns you a B in the class.")

    elif (total >= 70) and (total < 80):
        print("This earns you a C in the class.")

    elif (total >= 60) and (total < 70):
        print("This earns you a D in the class.")

    else:
        print("This earns you an F in the class.")

main()
