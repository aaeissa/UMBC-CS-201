

def convertToDict(info):
	
	stateFile = info.readlines()
	myDict = {}
	states = ""

	for line in stateFile:
		states = line.strip()
		key, value = states.split(",")
		myDict[key] = value

	return(myDict)

def main():

    print("Welcomet to the State Abbreviator.")

    info = open("states.txt", "r")
    
    myDict = convertToDict(info)

    userInput = ""
    while userInput != "exit" and userInput != "Exit":
        userInput = input("Please enter the state to abbreviate (list to get list and exit to exit): ").strip()

        if userInput == "list":
            for key in sorted(myDict):
                print(key)

        else:
            fullName = myDict.keys()
            abbreviation = myDict.values()             
            
            if userInput in fullName:
            	print("The abbreviation of the state: ", userInput, "is", myDict[userInput])

            else: 
                print("Sorry. That is not a state.")
            	        
                    
    print("Thank you for using the State Abbreviator.")

    info.close()
       
main()
