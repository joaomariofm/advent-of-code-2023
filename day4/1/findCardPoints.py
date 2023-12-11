def findCardPoints(card):
    points = 0
    for playerNumber in card.playerNumbers:
        if playerNumber in card.winningNumbers:
            if points == 0:
                points = 1
            else:
                points = points * 2

    return points
