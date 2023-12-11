def showFullNumbers(fullNumbers):
    for fullNumber in fullNumbers:
        print("[", end='')
        for character in fullNumber:
            print("[", end='')
            print(character.value, end='')
            print("-", end='')
            print(character.i, end='')
            print("-", end='')
            print(character.j, end='')
            print("]", end='')
        print("]", end='')
        print()
