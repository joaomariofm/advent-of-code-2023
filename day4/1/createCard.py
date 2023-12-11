from entities.Card import Card


def createCard(line):
    cardId = line.split(" ")[1][:-1]
    cardWinningNumbers = []
    cardPlayerNumbers = []

    splitedLine = line.split("|")
    firstLineSections = splitedLine[0].split(" ")
    secondLineSections = splitedLine[1].split(" ")

    for i, section in enumerate(firstLineSections):
        if i >= 2:
            if section == "|":
                break
            cardWinningNumbers.append(section)

    for number in cardWinningNumbers:
        if number == '':
            cardWinningNumbers.remove(number)

    for i, section in enumerate(secondLineSections):
        if section == "|":
            break
        cardPlayerNumbers.append(section)

    for number in cardPlayerNumbers:
        if number == '':
            cardPlayerNumbers.remove(number)

    cardPlayerNumbers[-1] = cardPlayerNumbers[-1][:-1]

    return Card(cardId, cardWinningNumbers, cardPlayerNumbers)
