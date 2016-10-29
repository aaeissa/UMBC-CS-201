

def letterCount(letter, myString):
    
    count = 0

    for l in myString:
        if l == letter:
            count += 1
    print(count)

def main():
    
    print("Should print: 3\nPrints: ",end="")
    letterCount("a","aardvark")
main()
