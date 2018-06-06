import random
from enum import Enum

class SquareType(Enum):
    NORMAL = 0
    CC = 1
    CHANCE = 2
    GTJ = 3
    INJAIL = 4

class Dice:

    i = 65

    def __init__(self):
        self.name = chr(Dice.i)
        Dice.i = Dice.i + 1

    def roll(self):
        return random.randint(1, 6)


class Card:

    def __init__(self, type, typeI, description):
        self.type = type
        self.typeI = typeI
        self.description = description

class ChanceCard(Card):

    type="Chance"

    def __init__(self, typeI, description):
        #   typeI must be of type CardType
        Card.__init__(self, ChanceCard.type, typeI, description)

class CommunityChestCard(Card):
    
    type="Community Chest"

    def __init__(self, typeI, description):
        #   typeI must be of type CardType
        Card.__init__(self, CommunityChestCard.type, typeI, description)


class Board:

    descArr = [
        "Go", "Mediterranean Avenue", "Community Chest", "Baltic Avenue", "Income Tax", 
        "Reading Railroad", "Oriental Avenue", "Chance", "Vermont Avenue", "Connecticut Avenue", 
        "Just Visiting(In Jail)", "St. Charles Place", "Electric Company", "States Avenue", 
        "Virginia Avenue", "Pennsylvania Railroad", "St. James Place", "Community Chest", 
        "Tennessee Avenue", "New York Avenue", "Free Parking", "Kentucky Avenue", "Chance", 
        "Indiana Avenue", "Illinois Avenue", "B. & O. Railroad", "Atlantic Avenue", "Ventnor Avenue", 
        "Water Works Aqueduc", "Marvin Gardens", "Go to Jail", "Pacific Avenue", "North California Avenue", 
        "Community Chest", "Pennsylvania Avenue", "Short Line", "Chance", "Park Place", "Luxury Tax", "Boardwalk"
    ]

    """
        Normal: 0
        Community Chest: 1
        Chance: 2
        Go to Jail: 3
        Just Visiting(in Jail): 4
    """

    typeArr = [
        SquareType.NORMAL, SquareType.NORMAL, SquareType.CC, SquareType.NORMAL, SquareType.NORMAL, 
        SquareType.NORMAL, SquareType.NORMAL, SquareType.CHANCE, SquareType.NORMAL, SquareType.NORMAL, 
        SquareType.INJAIL, SquareType.NORMAL, SquareType.NORMAL, SquareType.NORMAL, SquareType.NORMAL, 
        SquareType.NORMAL, SquareType.NORMAL, SquareType.CC, SquareType.NORMAL, SquareType.NORMAL, 
        SquareType.NORMAL, SquareType.NORMAL, SquareType.CHANCE, SquareType.NORMAL, SquareType.NORMAL, 
        SquareType.NORMAL, SquareType.NORMAL, SquareType.NORMAL, SquareType.NORMAL, SquareType.NORMAL, 
        SquareType.GTJ, SquareType.NORMAL, SquareType.NORMAL, SquareType.CC, SquareType.NORMAL, 
        SquareType.NORMAL, SquareType.CHANCE, SquareType.NORMAL, SquareType.NORMAL, SquareType.NORMAL
    ]

    class Square:

        class Position:

            def __init__(self, x, y):
                self.x = x
                self.y = y
            
            def get(self):
                return (self.x, self.y)

        def __init__(self, x=-1, y=-1, type=-1, description="", index=-1):
            self.position = self.Position(x, y)
            self.type = type
            self.description = description
            self.index = index

        def printInfo(self):
            print(self.index, " - ", self.type, " [", self.description, "]")

        def getType(self):
            return self.type

        def getTypeValue(self):
            return self.type.value

    def __init__(self):
        self.boardSquares = self.setUp()

    def setUp(self):
        squares = []
        for i in range(len(Board.descArr)):
            square = self.Square(type=Board.typeArr[i], description=Board.descArr[i], index=i)
            squares.append(square)
        return squares

    def getBoardSquares(self):
        return self.boardSquares

    def getJailIndex(self):
        return 10
    
    def getIllinoisAvenueIndex(self):
        return 24

    def getReadingRailRoadIndex(self):
        return 5
    
    def getBoardwalkIndex(self):
        return 39

    def getGoIndex(self):
        return 0
    
    def getStCharlesPlaceIndex(self):
        return 11

    def getRailroadPositionArr(self):
        posArr = [
            5, 15, 25
        ]
        return posArr
    
    def getUilityPosArr(self):
        posArr = [
            12, 28
        ]
        return posArr


class Token:

    numSquares = 40
    i = 65

    def __init__(self):
        self.posAtIndex = 0
        self.canGOOJ = False  #   if None -> no card for getting out of jail free
        self.isJustVisitJail = True
        self.name = chr(Token.i)
        if Token.i == 91:
            Token.i = 65
        else:
            Token.i = Token.i + 1
    
    def advancePosition(self, numSteps):
        self.posAtIndex = (self.posAtIndex + numSteps) % Token.numSquares

    def moveToPosition(self, posIndex):
        self.posAtIndex = posIndex

    def getCurrentPosIndex(self):
        return self.posAtIndex

    def canGetOutOfJail(self):
        return self.canGOOJ
    
    def justVisitJail(self):
        return self.isJustVisitJail

    def setCanGetOutOfJail(self, boolValue):
        self.canGOOJ = boolValue

    def setIsJustVisitJail(self, boolValue):
        self.isJustVisitJail = boolValue







