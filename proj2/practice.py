
def find_char(text, pos, word, ori, height, width):
    x = int(pos % width)
    y = int(pos // height)
    x += ori % 3 - 1
    y += ori // 3 - 1
    if text[pos] != word[0]:
        return None
    if len(word) == 1:
        return (x,y)
    if x < width and y < height and x > -1 and y > -1:
        pos = int(width * y + x)
        if text[pos] == word[1]:
            if len(word) > 1:
                resp = find_char(text, pos, word[1:], ori)
                if resp:
                    return resp
        else:
            return None

def main():

    print("Welcome to the Word Search.")
    print("For this, you will import two files: 1. The puzzle board, and 2. The word list.")

    puzzleFile = input("What is the puzzle file you would like to import? ")
    wordList = input("What is the word list file you would like to import? ")

    puzzleList = [] #this will be the 2d list of the game board/word search
    newList = [] #temporary list to create 2d list
    puzzle = open(puzzleFile, "r")
    puzzle = puzzle.readlines()

    for line in puzzle:
        stripped = line.strip()
        for char in stripped:
            if char != " ":
                newList.append(char)
            
        puzzleList.append(newList)
        newList = [] #emptying the list, rinse and repeat

    width = len(puzzle.splitlines()[0])
    height = len(puzzle) / width

    words = open(wordList, "r")
    words = words.readlines()

    keyList = [] #key words from the .txt file 
    for line in words:
        strippedKeys = line.strip()
        keyList.append(strippedKeys)


    for i in range(len(puzzleList)):
        for ori in [0,1,2,3,5,6,7,8]:
            for word in keyList:
                resp = find_char(puzzleList, i, word, ori, height, width)
                if resp:
                    print(word, resp, ori)

main()
