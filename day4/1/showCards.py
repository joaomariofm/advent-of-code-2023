def showCards(cards):
    for card in cards:
        print("Card ID: " + card.id)
        print("Winning numbers: " + str(card.winningNumbers))
        print("Player numbers: " + str(card.playerNumbers))
