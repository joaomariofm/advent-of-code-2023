def checkForNumberInsideSubString(subString):
    if subString[0] == 'o':
        if "one" in subString:
            return "1"

    if subString[0] == 't':
        if "two" in subString:
            return "2"
        if "three" in subString:
            return "3"

    if subString[0] == 'f':
        if "four" in subString:
            return "4"
        if "five" in subString:
            return "5"

    if subString[0] == 's':
        if "six" in subString:
            return "6"
        if "seven" in subString:
            return "7"

    if subString[0] == 'e':
        if "eight" in subString:
            return "8"

    if subString[0] == 'n':
        if "nine" in subString:
            return "9"

    return ''


def checkForNumberInsideReverseSubString(subString):
    if subString[0] == 'e':
        if "eno" in subString:
            return "1"
        if "eerht" in subString:
            return "3"
        if "evif" in subString:
            return "5"
        if "enin" in subString:
            return "9"

    if subString[0] == 'o':
        if "owt" in subString:
            return "2"

    if subString[0] == 'r':
        if "ruof" in subString:
            return "4"

    if subString[0] == 'x':
        if "xis" in subString:
            return "6"

    if subString[0] == 'n':
        if "neves" in subString:
            return "7"

    if subString[0] == 't':
        if "thgie" in subString:
            return "8"

    return ''


def seacrhForFirstNumberGoingForward(line):
    numbersFirstLetters = ['o', 't', 'f', 's', 'e', 'n']

    for i, c in enumerate(line):
        if c.isdigit():
            return c

        if c in numbersFirstLetters:
            subString = line[i:i+5]
            number = checkForNumberInsideSubString(subString)

            if number != '':
                return number


def searchForFirstNumberGoingBackward(line):
    numbersLastLetters = ['o', 'e', 'r', 'x', 't', 'n']

    reversedLine = line[::-1]

    for i, c in enumerate(reversedLine):
        if c.isdigit():
            return c

        if c in numbersLastLetters:
            subString = reversedLine[i:i+5]
            number = checkForNumberInsideReverseSubString(subString)

            if number != '':
                return number


def trebuchet(line):
    firstNumber = seacrhForFirstNumberGoingForward(line)
    secondNumber = searchForFirstNumberGoingBackward(line)

    print(firstNumber, secondNumber)

    if firstNumber == '' or firstNumber == None:
        firstNumber = '0'

    if secondNumber == '' or secondNumber == None:
        secondNumber = '0'

    return int(firstNumber + secondNumber)


with open('./input.txt') as f:
    lines = f.readlines()

    totalSum = 0

    for line in lines:
        cleanLine = line.strip()

        sum = trebuchet(cleanLine)

        totalSum += sum

    print(totalSum)
