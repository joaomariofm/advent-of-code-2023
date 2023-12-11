def showCharactersMatrix(charactersMatrix):
    for line in charactersMatrix:
        for character in line:
            print("[", end='')
            print(character.value, end='')
            print("-", end='')
            print(character.i, end='')
            print("-", end='')
            print(character.j, end='')
            print("]", end='')
        print()
