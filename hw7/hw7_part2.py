#File: hw7_part2.py
#Author: Ahmed Eissa
#Date: 4-4-16
#Section: 11
#Email: aeissa2@umbc.edu
#Description: This program serves as a currency exchange application. It can take in
#Retriever Bux and US Dollars. 

#initalize constants; Retriever Bux and US DOllar exchange rates
BUX_MULTIPLIER = 8
DOLLAR_MULTIPLIER = 0.125

#Function name: convertDollarsTo
#Description: converts US Dollars to Retriever Bux
#Inputs: amount
#Outputs: dollars
def convertDollarsTo(amount):    

    #exchaning dollars
    dollars = amount * BUX_MULTIPLIER 
    
    dollars = format(dollars, '.2f')

    return(dollars)

#Function name: convertBux
#Description: converts Retriever Bux to US Dollars
#Inputs: amount
#Outputs: bux
def convertBuxTo(amount):
    #exchanging bux
    bux = amount * DOLLAR_MULTIPLIER

    bux = format(bux, '.2f')

    return(bux)

#Function name: goodbye
#Description: prints a goodbye statement to the user
#Inputs: none
#Outputs: none
def goodbye():
    
    print("Goodbye, and thank you for using the Currency Converter.")


def main():

    print("Welcome to the Currency Converter.")
    print("What would you like to do?")

    choice = 0 
    amount = 0
    conversion = 0

    #get input from user
    choice = int(input("1. Convert US Dollars to Retriever Bux\n2. Convert Retriever Bux to US Dollars\n3. Exit\nEnter your choice: "))

    #error check to ensure user chooses from the list
    while choice < 1 or  choice > 3:
        choice = int(input("This is an invalid choice.\nEnter your choice: "))
    
    if choice == 1:
        #get currency amount
        amount = float(input("How much do you want to convert?: "))
        
        #convert USD to Bux
        conversion = convertDollarsTo(amount)

        print(amount, "US dollars equates to", conversion, "Retriever Bux.") 

        #exit currency exchange 
        goodbye()

    elif choice == 2:

        #get currency amount
        amount = float(input("How much do you want to convert?: "))

        #convert Bux to USD
        conversion = convertBuxTo(amount)

        print(amount, "Retriever Bux equates to", conversion, "US dollars.")

        #exit currency exchange 
        goodbye()

    elif choice == 3:

        #exit currency exchange 
        goodbye()


main()
