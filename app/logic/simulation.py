from logic.gameLogic import GameLogic
from model.monopoly import Monopoly

class Simulation:

    def runSimulation():

        #   get equipments
        monopoly = Monopoly()
        equipMap = monopoly.getEquipments()
        equipArr = ["Dice", "Chance Card", "Community Chest Card", "Game Board", "Token"]
        dice1, dice2 = equipMap[equipArr[0]]
        tokenArr = equipMap[equipArr[4]]
        token = tokenArr[0]
        gameBoard = equipMap[equipArr[3]]
        chanceCardArr = equipMap[equipArr[1]]
        ccCardArr = equipMap[equipArr[2]]

        numMoves = 100

        for i in range(numMoves):

            print("***********************")

            #   roll dices
            num1, num2, num3, resSum = GameLogic.rollDices(dice1, dice2)
            print(num1, num2, num3, resSum)

            #   move token
            if resSum == 0:
                token = GameLogic.moveTokenToJail(token, gameBoard)
            elif token.getCurrentPosIndex() != gameBoard.getJailIndex() or token.justVisitJail() == True:
                token = GameLogic.moveTokenByNumSteps(token, resSum)
            elif token.getCurrentPosIndex() == gameBoard.getJailIndex() and num2 == 0:
                token = GameLogic.moveTokenOutOfJail(token, resSum)

            print(token.getCurrentPosIndex())
            print(token.justVisitJail())

            #   perform action based on square type
            token = GameLogic.performActionGivenSquareType(gameBoard, token, chanceCardArr, ccCardArr)
            print(token.getCurrentPosIndex())

            print("#######################")


