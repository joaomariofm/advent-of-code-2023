from entities.Character import Character


def createCharactersMatrix(file):
    lines = file.readlines()

    charactersMatrix = []

    for i, line in enumerate(lines):
        characters = []
        for j, char in enumerate(line):
            if char == '\n':
                break
            character = Character(char, i, j)
            characters.append(character)
        charactersMatrix.append(characters)

    return charactersMatrix
