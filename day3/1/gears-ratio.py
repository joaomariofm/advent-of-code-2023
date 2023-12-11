from utils.createCharactersMatrix import createCharactersMatrix

from utils.showCharactersMatrix import showCharactersMatrix
from utils.showCharactersArray import showCharactersArray
from utils.showFullNumbers import showFullNumbers

from utils.findSymbolAdjacentCharacters import findSymbolAdjacentCharacters
from utils.findFullNumbers import findFullNumbers
from utils.findFullNumbersWithSymbolAdjacentCharacters import findFullNumbersWithSymbolAdjacentCharacters

from utils.sumFullNumbers import sumFullNumbers


with open('inputs/input.txt') as file:
    charactersMatrix = createCharactersMatrix(file)
    showCharactersMatrix(charactersMatrix)

    print()

    symbolAdjacentCharacters = findSymbolAdjacentCharacters(charactersMatrix)
    showCharactersArray(symbolAdjacentCharacters)

    print()

    fullNumbers = findFullNumbers(charactersMatrix)
    showFullNumbers(fullNumbers)

    print()

    fullNumbersWithSymbolAdjacentCharacters = findFullNumbersWithSymbolAdjacentCharacters(fullNumbers, symbolAdjacentCharacters)
    showFullNumbers(fullNumbersWithSymbolAdjacentCharacters)

    print()

    sum = sumFullNumbers(fullNumbersWithSymbolAdjacentCharacters)
    print(sum)
