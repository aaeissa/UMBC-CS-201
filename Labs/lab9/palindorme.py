
def isPalindrome(myString):
    tempString = myString
    length = len(tempString)
    #print("length is", length)
    
    half = (length/2)
    #print("half is", int(half))

    myBool = True
    
    #print("the index of half+1 is", myString[int(half)+1])

    for i in range(int(half)):
        if myString[i] != myString[int(half)+1]:
            myBool = False
        elif myString[i] == myString[int(half)+1]:
            myBool = True

    print(myBool)


def main():
    print("Should print: True\nPrints: ",end="")
    isPalindrome("oozyratinasanitaryzoo")
    print("Should print: False\nPrints: ",end="")
    isPalindrome("18101181")

main()



