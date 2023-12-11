def sumFullNumbers(fullNumbers):
    sum = 0
    for fullNumber in fullNumbers:
        fullNumberAsString = ""
        for character in fullNumber:
            fullNumberAsString += character.value
        sum += int(fullNumberAsString)

    return sum
