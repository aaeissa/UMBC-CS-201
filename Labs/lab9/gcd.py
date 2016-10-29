

def gcd(x, y):
    smaller = 0
    if x > y:
        smaller = y
    else: 
        smaller = x
    
    gcdvar = 0
    for i in range(1, smaller+1):
        if ((x % i == 0) and (y % i == 0)):
            gcdVar = i

    return gcdVar

def main():
    print("Should print: 15\nPrints: ",end="")
    print(gcd(30, 15))
    print("Should print: 7\nPrints: ",end="")
    print(gcd(7, 49))
    print("Should print: 45\nPrints: ",end="")
    print(gcd(45, 45))
main()
