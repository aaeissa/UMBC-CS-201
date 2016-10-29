 for i in range(len(myList)):
            if listNum == myList[i]:
                checkCounter += 1
        
        if checkCounter > 0:
            inList = True

        while inList == True:
            print("The number", listNum, "is already in the list.")
            listNum = int(input("Please enter a number: "))
            
            for i in range(len(myList)):
                if listNum == myList[i]:
                    secondCheck += 1
            
            if secondCheck == 0:
                inList = False
            

        if inList == False:
            myList.append(listNum)
            counter += 1  










   while x == True:

            if listNum == myList[i]:
                print("The number", listNum, "is already in the list.")
                listNum = int(input("Please enter a number: "))

            elif listNum != myList[i]:
                check += 1

            if check == counter:
                x == False



        for i in range(len(myList)):                                                                    
            while listNum == myList[i]:                                                                 
               print("The number", listNum, "is already in the list.")                                  
               listNum = int(input("Please enter a number: "))     






 for i in range(len(myList)):
            if listNum == myList[i]:
                print("The number", listNum, "is already in the list.")

                while check == True:
                    listNum = int(input("Please enter a number: "))

                    for j in range(len(myList)):
                        if listNum != myList[j]:
                             checkCount += 1
                    if checkCount == counter:
                        check == False
