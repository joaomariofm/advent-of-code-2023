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


def findSymbolAdjacentNumbers(gearsMatrix):
    numbersAjacentstoSymbols = []

    for i, line in enumerate(gearsMatrix):
        for j, character in enumerate(line):
            if character.isnumeric():
                if hasAdjacentSymbol(gearsMatrix, i, j):
                    numbersAjacentstoSymbols.append(character)

    return numbersAjacentstoSymbols


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

    numbers = findSymbolAdjacentNumbers(gearsMatrix)
    print(numbers)
