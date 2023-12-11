from createCard import createCard
from showCards import showCards
from findCardPoints import findCardPoints

with open('inputs/input.txt') as file:
    lines = file.readlines()

    cards = []
    totalPoints = 0

    for line in lines:
        cards.append(createCard(line))

    for card in cards:
        cardPoints = findCardPoints(card)
        showCards([card])
        print("Points: " + str(cardPoints))
        totalPoints += cardPoints

    print("Total points: " + str(totalPoints))
