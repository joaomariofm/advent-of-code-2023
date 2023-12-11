def indexesAreNotOutOfRange(gearsMatrix, i, j):
    if (0 <= i) and (0 <= j) and (i < len(gearsMatrix)) and (j < len(gearsMatrix[0])):
        return True
    return False


def isASymbol(character):
    if not character.value.isnumeric() and character.value != '.':
        return True
    return False


def hasAdjacentSymbol(gearsMatrix, i, j):
    indexi = 0
    indexj = 0

    indexi = i-1
    indexj = j-1

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj):
        if isASymbol(gearsMatrix[indexi][indexj]):
            return True

    indexi = i-1
    indexj = j

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj):
        if isASymbol(gearsMatrix[indexi][indexj]):
            return True

    indexi = i-1
    indexj = j+1

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj):
        if isASymbol(gearsMatrix[indexi][indexj]):
            return True

    indexi = i
    indexj = j-1

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj):
        if isASymbol(gearsMatrix[indexi][indexj]):
            return True

    indexi = i
    indexj = j+1

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj):
        if isASymbol(gearsMatrix[indexi][indexj]):
            return True

    indexi = i+1
    indexj = j-1

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj):
        if isASymbol(gearsMatrix[indexi][indexj]):
            return True

    indexi = i+1
    indexj = j

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj):
        if isASymbol(gearsMatrix[indexi][indexj]):
            return True

    indexi = i+1
    indexj = j+1

    if indexesAreNotOutOfRange(gearsMatrix, indexi, indexj):
        if isASymbol(gearsMatrix[indexi][indexj]):
            return True

    return False
