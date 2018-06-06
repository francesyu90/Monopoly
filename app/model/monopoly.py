from enum import Enum
from model.equipment import Dice, ChanceCard, CommunityChestCard, Card, Board, Token

class CardType(Enum):
    OTHERS = 0
    IA = 1  #   Illinois Avenue
    RR = 2  #   Reading Railroad
    BW = 3  #   Boardwalk
    GO = 4
    GOOJF = 5   #   Get Out Of Jail Free
    SCP = 6 #   St. Charles Place
    TP = 7  #   Go Back Three Spaces
    NXRR = 8    #   The Next Railroad
    NARR = 9    #   The Nearest Railroad
    GTJ = 10    #   Go To Jail
    NAU = 11    #   The Nearest Utility


class Monopoly:

    def __init__(self, tokenSize=1):

        self.setUp(tokenSize)

    def setUp(self, tokenSize):

        #   initialize dices
        self.dice1 = Dice()
        self.dice2 = Dice()

        #   initialize chance cards
        self.chanceCardArr = self.getChanceCards()

        #   initialize community chest cards
        self.ccCardArr = self.getCommunityChestCards()

        #   initialize game board
        self.gameBoard = Board()

        #   initialize token
        self.tokenArr = self.getTokens(tokenSize)


    def getChanceCards(self):
        descArr = [
            "Go to Jail", 
            "Advance to the Nearest Utility",
            "Advance to Illinois Avenue",
            "",
            "Take a trip to Reading Railroad",
            "Advance to Boardwalk",
            "Advance to Go",
            "",
            "",
            "Get Out of Jail Free",
            "Advance to St. Charles Place",
            "",
            "Go Back Three Spaces",
            "",
            "Advance to The Next Railroad",
            "Advance to The Nearest Railroad"
        ]
        typeIArr = [
            CardType.GTJ, CardType.NAU, CardType.IA, CardType.OTHERS, CardType.RR, CardType.BW,
            CardType.GO, CardType.OTHERS, CardType.OTHERS, CardType.GOOJF, CardType.SCP,
            CardType.OTHERS, CardType.TP, CardType.OTHERS, CardType.NXRR, CardType.NARR
        ]

        chanceCardArr = []
        for i in range(len(descArr)):
            chanceCard = ChanceCard(typeIArr[i], descArr[i])
            chanceCardArr.append(chanceCard)
        return chanceCardArr


    def getCommunityChestCards(self):
        descArr = [
            "",
            "",
            "Advance to Go",
            "",
            "",
            "",
            "",
            "",
            "",
            "Go to Jail",
            "",
            "",
            "",
            "",
            "",
            "Get Out of Jail Free"
        ]
        typeIArr = [
            CardType.OTHERS, CardType.OTHERS, CardType.GO, CardType.OTHERS, CardType.OTHERS,
            CardType.OTHERS, CardType.OTHERS, CardType.OTHERS, CardType.OTHERS, 
            CardType.GTJ, CardType.OTHERS, CardType.OTHERS, CardType.OTHERS, CardType.OTHERS, 
            CardType.OTHERS,CardType.GOOJF
        ]

        ccCardArr = []
        for i in range(len(descArr)):
            ccCard = CommunityChestCard(typeIArr[i], descArr[i])
            ccCardArr.append(ccCard)
        return ccCardArr

    
    def getTokens(self, size):
        tokenArr = []
        for i in range(size):
            token = Token()
            tokenArr.append(token)
        return tokenArr


    def getEquipments(self):
        equipArr = ["Dice", "Chance Card", "Community Chest Card", "Game Board", "Token"]
        equipMap = {}
        equipMap[equipArr[0]] = (self.dice1, self.dice2)
        equipMap[equipArr[1]] = self.chanceCardArr
        equipMap[equipArr[2]] = self.ccCardArr
        equipMap[equipArr[3]] = self.gameBoard
        equipMap[equipArr[4]] = self.tokenArr
        return equipMap

