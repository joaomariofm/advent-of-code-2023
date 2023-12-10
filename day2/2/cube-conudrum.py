class CubeDemonstration:
    def __init__(self, blueCubes, redCubes, greenCubes):
        self.blueCubes = blueCubes
        self.redCubes = redCubes
        self.greenCubes = greenCubes


class Game:
    def __init__(self, gameId):
        self.gameId = gameId
        self.cubeDemonstrations = []

    def getGameId(self):
        return self.gameId

    def addCubeDemonstration(self, cubeDemonstration):
        self.cubeDemonstrations.append(cubeDemonstration)

    def showCubeDemonstrations(self):
        print('Game ID: ' + self.gameId)

        for cubeDemonstration in self.cubeDemonstrations:
            print('Cube Demonstration')
            print('blueCubes: ', cubeDemonstration.blueCubes)
            print('redCubes: ', cubeDemonstration.redCubes)
            print('greenCubes: ', cubeDemonstration.greenCubes)


def formatGameContent(content):
    gameId = content[content.index(' ') + 1:content.index(':')]

    game = Game(gameId)

    subsets = content[content.index(':') + 1:].split(';')

    for subset in subsets:
        blueCubes = '0'
        redCubes = '0'
        greenCubes = '0'

        parts = subset.split(' ')

        for i, part in enumerate(parts):
            if 'blue' in part:
                blueCubes = parts[i - 1]
            elif 'red' in part:
                redCubes = parts[i - 1]
            elif 'green' in part:
                greenCubes = parts[i - 1]

        cubeDemonstration = CubeDemonstration(
            int(blueCubes),
            int(redCubes),
            int(greenCubes),
        )

        game.addCubeDemonstration(cubeDemonstration)

    return game


def findMinimumPowerOfCubes(game):
    redMinimum = 1
    blueMinimum = 1
    greenMinimum = 1

    for cubeDemonstration in game.cubeDemonstrations:
        if cubeDemonstration.redCubes > redMinimum:
            redMinimum = cubeDemonstration.redCubes
        if cubeDemonstration.blueCubes > blueMinimum:
            blueMinimum = cubeDemonstration.blueCubes
        if cubeDemonstration.greenCubes > greenMinimum:
            greenMinimum = cubeDemonstration.greenCubes

    return redMinimum * blueMinimum * greenMinimum


with open('input.txt') as f:
    content = f.readlines()

    totalSum = 0

    for line in content:
        game = formatGameContent(line)

        cubesPower = findMinimumPowerOfCubes(game)

        totalSum += cubesPower

    print(totalSum)
