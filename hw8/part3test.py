def newChar(stripped, charList):

    #length of the word is one (or less)                                                                                                                              
    if len(stripped) == 1:
        return stripped


    #elif len(stripped) > 1:
    #two adjacent letters are the same                                                                                                                                
    if stripped[0] == stripped[1]:
        newChar(stripped[1:], charList)

    #two adjacent letters are NOT the same                                                                                                                            
    else:
        return stripped[0] + newChar(stripped[1:], charList)


def main():

    stripped = "aabbccddaa"
    charList = []


    charList = newChar(stripped, charList)

    print(charList)

main()
