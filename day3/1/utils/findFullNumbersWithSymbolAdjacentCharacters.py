def findFullNumbersWithSymbolAdjacentCharacters(fullNumbers, symbolAdjacentCharacters):
    fullNumbersWithSymbolAdjacentCharacters = []

    for fullNumber in fullNumbers:
        for character in fullNumber:
            if character in symbolAdjacentCharacters:
                fullNumbersWithSymbolAdjacentCharacters.append(fullNumber)
                break

    return fullNumbersWithSymbolAdjacentCharacters
