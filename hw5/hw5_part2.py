def main():

    #get user input
    numCopies = int(input("How many copies do you want? "))

    #initialize varibales for the sliding scale pricing model
    costOne = 0
    costTwo = 0
    costThree = 0
    costFour = 0


    if numCopies < 100:
        #iterate through the first range of copy prices
        for i in range(1, numCopies+1):
            costOne += 0.08

    elif (numCopies > 100) and (numCopies <= 1000):
        #iterate through the first range of copy prices
        for i in range(1, 101):
            costOne += 0.08
        #iterate through the second range of copy prices
        for i in range(101, numCopies+1):
            costTwo += 0.06

    elif (numCopies > 1000) and (numCopies <= 10000):
        #iterate through the first range of copy prices
        for i in range(1, 101):
            costOne += 0.08
        #iterate through the second range of copy prices
        for i in range(101, 1001):
            costTwo += 0.06
        #iterate through the third range of copy prices
        for i in range(1001, numCopies+1):
            costThree += 0.05

    elif numCopies > 10000:
        #iterate through first range of copy prices
        for i in range(1, 101):
            costOne += 0.08
        #iterate through second range of copy prices
        for i in range(101, 1001):
            costTwo += 0.06
        #iterate through third range of copy prices
        for i in range(1001, 10001):
            costThree += 0.05
        #iterate through fourth and final range of copy prices
        for i in range(10001, numCopies+1):
            costFour += 0.04

    #calculating the total cost of user's copies
    if numCopies <= 100:
        totalCost = costOne


    #price if user's copies falls in second range
    elif (numCopies > 100) and (numCopies <= 1000):
        totalCost = costOne + costTwo

    #price if user's copies falls in third range
    elif (numCopies > 1000) and (numCopies <= 10000):
        totalCost = costOne + costTwo + costThree

    #price if user's copies falls in fourth and final range
    else:
        totalCost = costOne + costTwo + costThree + costFour

    #display total cost of copies to user
    print("The total cost for", numCopies, "is $%.1f" % (totalCost))

main()




