

def main():

    shows = ["Daredevil", "Fargo", "Limitless", "Elementary", "Brooklyn 99", "Empire", "Supergirl"]
    
    for i in range(len(shows)):
        print(i+1, "-", shows[i])
       

    
    print("You and your friends are voting on a show to watch.\nWhich show would you like to vote for?")

    voteList = [0] * len(shows)
    vote = int(input("Enter '0' to stop voting: "))


    dd = 0
    fargo = 0
    limit = 0
    elem = 0
    brook = 0
    empire = 0
    superGirl = 0

    while vote != 0:
        if (vote >= 1) and (vote <= 7):
            if vote == 1:
                dd += 1
                voteList[0] = dd
            if vote == 2:
                fargo += 1
                voteList[1] = fargo
            if vote == 3:
                limit += 1
                voteList[2] = limit
            if vote == 4:
                elem += 1
                voteList[3] = elem
            if vote == 5:
                brook += 1
                voteList[4] = brook
            if vote == 6: 
                empire += 1
                voteList[5] = empire
            if vote == 7:
                superGirl += 1
                voteList[6] = superGirl

        vote = int(input("Enter '0' to stop voting: "))
      
    
    print("Here are the final votes:\n")

  
    for i in range(len(shows)):
        print(shows[i], "has\t", voteList[i], "votes")


main()



