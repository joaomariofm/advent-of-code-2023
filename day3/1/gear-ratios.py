class Digit:
    def __init__(self, number, i, j):
        self.number = number    
        self.i = i
        self.j = j


class FullNumber:
    def __init__(self, *numbers):
        self.numbers = numbers


def isASymbol(character):
    if not character.isnumeric() and character != '.':
        return True
    return False

def indexesAreNotOutOfRange(gearsMatrix, i, j):
    if (0 <= i) and (0 <= j) and (i < len(gearsMatrix)) and (j < len(gearsMatrix[0])):
        return True
    return False

def hasAdjacentSymbol(gearsMatrix, i, j):
    indexi = 0
    indexj = 0

    indexi = i-1
    indexj = j-1
    
    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj) and isASymbol(gearsMatrix[indexi][indexj]):
        return True

    indexi = i-1
    indexj = j

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj) and isASymbol(gearsMatrix[indexi][indexj]):
        return True

    indexi = i-1
    indexj = j+1

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj) and isASymbol(gearsMatrix[indexi][indexj]):
        return True

    indexi = i
    indexj = j-1

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj) and isASymbol(gearsMatrix[indexi][indexj]):
        return True

    indexi = i
    indexj = j+1

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj) and isASymbol(gearsMatrix[indexi][indexj]):
        return True

    indexi = i+1
    indexj = j-1

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj) and isASymbol(gearsMatrix[indexi][indexj]):
        return True

    indexi = i+1
    indexj = j

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj) and isASymbol(gearsMatrix[indexi][indexj]):
        return True

    indexi = i+1
    indexj = j+1

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj) and isASymbol(gearsMatrix[indexi][indexj]):
        return True

    return False


def findSymbolAdjacentDigits(gearsMatrix):
    digitsAjacentsToSymbols = []

    for i, line in enumerate(gearsMatrix):
        for j, digit in enumerate(line):
            if digit.isnumeric():
                if hasAdjacentSymbol(gearsMatrix, i, j):
                    adjacentDigit = Digit(digit, i, j)
                    digitsAjacentsToSymbols.append(adjacentDigit)

    return digitsAjacentsToSymbols


def findFullNumbers(gearsMatrix):
    fullNumbers = []
    digitsInAnalysis = []

    for i, line in enumerate(gearsMatrix):
        for j, digit in enumerate(line):
            if digit.isnumeric():
                digitsInAnalysis.append(Digit(digit, i, j))
            elif digitsInAnalysis:
                fullNumbers.append(FullNumber(digitsInAnalysis))
                digitsInAnalysis = []

    return fullNumbers


def verifyFullNumberAdjacentDigits(fullNumbers, symbolAdjacentDigits):
    adjacentFullNumbers = []

    for fullNumber in fullNumbers:
        for number in fullNumber.numbers:
            for digit in number:
                for symbolAdjacentDigit in symbolAdjacentDigits:
                    if digit.i == symbolAdjacentDigit.i and digit.j == symbolAdjacentDigit.j:
                        print('fullNumber analized:', end="")
                        showFullNumber(fullNumber) 
                        print(fu
    return adjacentFullNumbers


def showAdjacentDigits(adjacentDigits):
    for adjacentDigit in adjacentDigits:
        print('number:', adjacentDigit.number) 
        print('index i:', adjacentDigit.i)
        print('index j:', adjacentDigit.j) 
        print("-----")


def showFullNumbers(fullNumbers):
    for fullNumber in fullNumbers:
        for number in fullNumber.numbers:
            for digit in number:
                print(digit.number, end="")
            print()


def showFullNumber(fullNumber):
    for number in fullNumber.numbers:
        for digit in number:
            print(digit.number, end="")
        print()

def createLineArray(line):
    lineArray = []
    
    for character in line:
        if character == '\n':
            return lineArray
        

        lineArray.extend(character)

    return None


with open('example.txt') as file:
    lines = file.readlines()

    gearsMatrix = []

    for line in lines:
        lineArray = createLineArray(line)
        gearsMatrix.append(lineArray)

    adjacentDigits = findSymbolAdjacentDigits(gearsMatrix)
    fullNumbers = findFullNumbers(gearsMatrix)

    adjacentFullNumbers = verifyFullNumberAdjacentDigits(fullNumbers, adjacentDigits)

    showFullNumbers(adjacentFullNumbers)
