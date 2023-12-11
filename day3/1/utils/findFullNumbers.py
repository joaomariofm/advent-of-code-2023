def findFullNumbers(charactersmatrix):
    fullNumbers = []
    charactesUnderAnalysis = []

    for line in charactersmatrix:
        charactesUnderAnalysis = []
        for character in line:
            if character.value.isnumeric():
                charactesUnderAnalysis.append(character)

            if not character.value.isnumeric() or character == line[-1]:
                fullNumbers.append(charactesUnderAnalysis)
                charactesUnderAnalysis = []

    return fullNumbers
