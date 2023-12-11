from utils.hasAdjacentSymbol import hasAdjacentSymbol


def findSymbolAdjacentCharacters(charactersMatrix):
    symbolAdjacentCharacters = []

    for line in charactersMatrix:
        for character in line:
            if character.value.isnumeric():
                if hasAdjacentSymbol(charactersMatrix, character.i, character.j):
                    symbolAdjacentCharacters.append(character)

    return symbolAdjacentCharacters
