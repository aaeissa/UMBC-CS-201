# Author: Ahmed Eissa
# File:        hw2_part1.py
# Date:        2/15/16
# Section:     07
# UMBC Email:  aeissa2@umbc.edu
# Description: This program provides an expected output for a series of equations, and explains the actual output based on the order of operations 
 
#Question 1
#Expected output: 55

num1 = (7+4)*5
print("num1 evaluates to:", num1) 

#Actual output: 55
#Explanation: My answer was coorect - parentheses first (11), then multiplication (55)



#Question 2
#Expected output: 1

num2 = 15%7
print("num2 evaluates to:", num2)

#Actual output: 1
#Explanation: My answer was correct - 7 goes into 15 twice, with 1 remainder



#Question 3
#Expected output: 0

num3 = (32 % 36)
print("num3 evaluates to:", num3)

#Actual output: 32 
#Explanation: My answer was incorrect. I originally though it would be 0 because 36 does not go into 32, however this actually results in a remiander of 32



#Question 4
#Expected output: 12

num4 = (5-3) + (10-5) * (8%3)
print("num4 evaluates to:", num4)

#Actual output: 12
#Explanation: My answer was correct - parentheses results in 2 + 5 * 2, multiplication (10), addition (12)



#Question 5
#Expected output: 4.5

num5 = 21 / 7 / 4 * (3 + 3)
print("num5 evaluates to:", num5) 

#Actual output: 
#Explanation: My answer was correct - parentheses first (6), then division (21/7 = 3), then division (3/4 =.75), then multiplication (4.5)



#Question 6
#Expected output: 14

num6 = 9 / 3 + 21 - 5 * 2
print("num6 evaluates to:", num6)

#Actual output: 14
#Explanation: My answer was correct - division first (3), then multiplication (10), then addition (24), then subtraction (14)


#Question 7
#Expected output: 14

num7 = 7 % 5 + 6 * 2
print("num7 evaluates to:", num7)
 
#Actual output: 14
#Explanation: division first (2), then multiplication (12), then addition (14)



#Question 8
#Expected output: 17.304

num8 = 35.2 / 2.3 + (332 % 33) 
print("num8 evaluates to:", num8)

#Actual output: 17.304
#Explanation: My answer was correct - parentheses first (2), then division (15.304), then addition (17.304)



#Question 9
#Given equation: num9 = 55 / 10 + 45 / 0.2
#Solved equation: num9 = 55 / (10 + 45) / .2 
#Target number: 5.0

num9 = 55 / (10 + 45) / .2
print("num9 evaluates to:", num9, "and should be", 5.0)



#Question 10
#Given equation: num10 = 65 // 20 + 10 - 4 % 4
#Solved equation: num10 = 65 // (20 + 10 - 4 % 4)
#Target number: 2

num10 = 65 // (20 + 10 - 4 % 4)
print("num10 evaluates to:", num10, "and should be", 2)





