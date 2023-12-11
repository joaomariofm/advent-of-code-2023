def showCharactersArray(charactersArray):
    for character in charactersArray:
        print("[", end='')
        print(character.value, end='')
        print("-", end='')
        print(character.i, end='')
        print("-", end='')
        print(character.j, end='')
        print("]", end='')
    print()
