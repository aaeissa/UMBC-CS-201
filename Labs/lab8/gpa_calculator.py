GRADE_AMOUNT = 3 

def convertLetter(letter):

    if letter == "A":
        return 4
    elif letter == "B":
        return 3
    elif letter == "C":
        return 2
    elif letter == "D":
        return 1
    else:
        return 0

def main():

    gradeFile = open("grades.txt", "r")
    results = open("results.txt", "w")
    average = 0
    grade1 = 0
    grade2 = 0
    grade3 = 0

    for line in gradeFile:
        line = line.strip()
        first, last, letter1, letter2, letter3 = line.split(";")
        
        grade1 = convertLetter(letter1)
        grade2 = convertLetter(letter2)
        grade3 = convertLetter(letter3)

        average = (grade1 + grade2 + grade3) / GRADE_AMOUNT

        print(first + " " + last+ "'s GPA is " + str(average))
        results.write(first + " " + last+ "'s GPA is " + str(average) + "\n")

        grade = 0
        average = 0

    gradeFile.close()
    results.close()

main()
