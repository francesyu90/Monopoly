import random
from model.monopoly import CardType
from model.equipment import SquareType

class GameLogic:

    def rollDices(dice1, dice2):

        num1 = dice1.roll()
        num2 = dice2.roll()
        if num1 != num2:
            return (num1, num2, 0, num1+num2)
        num3 = dice2.roll()
        if num3 != num2:
            return (num1, 0, num3, num1+num3)
        return (num1, num2, num3, 0)

    def drawCard(cardArr):
        randNum = random.randint(0, len(cardArr)-1)
        return cardArr[randNum]

    def drawCardAndGetIndex(cardArr):
        return random.randint(0, len(cardArr)-1)

    def moveTokenByNumSteps(token, numSteps):
        token.advancePosition(numSteps)
        return token
    
    def moveTokenByPosIndex(token, posIndex):
        token.moveToPosition(posIndex)
        return token

    def moveTokenToJail(token, board):
        return GameLogic.handleGivencardGTJ(board, token)

    def moveTokenOutOfJail(token, numSteps):
        token.setIsJustVisitJail(True)
        return GameLogic.moveTokenByNumSteps(token, numSteps)

    def determineNextPosIndexGivenCard(card, board):
        if card.typeI == CardType.OTHERS:
            return -1
        elif card.typeI == CardType.IA:
            return board.getIllinoisAvenueIndex()
        elif card.typeI == CardType.RR:
            return board.getReadingRailRoadIndex()
        elif card.typeI == CardType.BW:
            return board.getBoardwalkIndex()
        elif card.typeI == CardType.GO:
            return board.getGoIndex()
        elif card.typeI == CardType.GOOJF:
            return -CardType.GOOJF.value
        elif card.typeI == CardType.SCP:
            return board.getStCharlesPlaceIndex()
        elif card.typeI == CardType.TP:
            return -3
        elif card.typeI == CardType.NXRR:
            return -CardType.NXRR.value
        elif card.typeI == CardType.NARR:
            return -CardType.NARR.value
        elif card.typeI == CardType.GTJ:
            return -CardType.GTJ.value
        else:
            return -CardType.NAU.value

    def handleGivenCardGOOJF(board, token):

        curPosIndex = token.getCurrentPosIndex()
        jailIndex = board.getJailIndex()

        #   if current not in jail
        if curPosIndex != jailIndex:
            token.setCanGetOutOfJail(True)
        else:   #   if current in jail
            token = GameLogic.moveTokenByPosIndex(token, jailIndex+1)
            token.setCanGetOutOfJail(False)

        token.setIsJustVisitJail(True)
        return token

    def handleGivenCardNXRR(board, token):

        railroadPosArr = board.getRailroadPositionArr()
        curPosIndex = token.getCurrentPosIndex()

        posIndex = curPosIndex
        if curPosIndex >= railroadPosArr[len(railroadPosArr)-1]:
            posIndex = railroadPosArr[0]
        else:
            for i in range(len(railroadPosArr)):
                index = railroadPosArr[i]
                if index > posIndex:
                    posIndex = index
                    break
        
        return GameLogic.moveTokenByPosIndex(token, posIndex)


    def handleGivenCardNARR(board, token):
        diffArr = []
        railroadPosArr = board.getRailroadPositionArr()
        curPosIndex = token.getCurrentPosIndex()

        for i in range(len(railroadPosArr)):
            diff = abs(curPosIndex - railroadPosArr[i])
            diffArr.append(diff)

        minDiff = min(diffArr)
        minDiffIndex = diffArr.index(minDiff)
        posIndex = railroadPosArr[minDiffIndex]
        return GameLogic.moveTokenByPosIndex(token, posIndex)

    
    def handleGivencardGTJ(board, token):
        
        if token.canGetOutOfJail() == True:
        #   if have card Get Out Of Jail Free
            token.setCanGetOutOfJail(False)
        else:
        #   if not have the card
            posIndex = board.getJailIndex()
            token = GameLogic.moveTokenByPosIndex(token, posIndex)
            token.setIsJustVisitJail(False)
        return token

    def handleGivenCardNAU(board, token):

        diffArr = []
        utilityPosArr = board.getUilityPosArr()
        curPosIndex = token.getCurrentPosIndex()

        for i in range(len(utilityPosArr)):
            diff = abs(curPosIndex - utilityPosArr[i])
            diffArr.append(diff)
        
        minDiff = min(diffArr)
        minDiffIndex = diffArr.index(minDiff)
        posIndex = utilityPosArr[minDiffIndex]

        return GameLogic.moveTokenByPosIndex(token, posIndex)


    def moveTokenByPosIndexGivenCard(board, token, posIndex):
        if posIndex == -1:
            return token

        curPosIndex = token.getCurrentPosIndex()
        jailIndex = board.getJailIndex()
        if curPosIndex == jailIndex and posIndex != -CardType.GOOJF.value:
            return token
        elif posIndex >= 0:
            return GameLogic.moveTokenByPosIndex(token, posIndex)
        elif posIndex == -3:
            curPosIndex = token.getCurrentPosIndex()
            updatedPosIndex = (curPosIndex + 40 + posIndex) % 40
            return GameLogic.moveTokenByPosIndex(token, updatedPosIndex)
        elif posIndex == -CardType.GOOJF.value:
            return GameLogic.handleGivenCardGOOJF(board, token)
        elif posIndex == -CardType.NXRR.value:
            return GameLogic.handleGivenCardNXRR(board, token) 
        elif posIndex == -CardType.NARR.value:
            return GameLogic.handleGivenCardNARR(board, token)  
        elif posIndex == -CardType.GTJ.value:
            return GameLogic.handleGivencardGTJ(board, token)    
        else:
            return GameLogic.handleGivenCardNAU(board, token)

    def performActionGivenSquareType(board, token, chanceCardArr, ccCardArr):
        boardSquares = board.getBoardSquares()
        curPosIndex = token.getCurrentPosIndex()
        square = boardSquares[curPosIndex]
        print(square.type)

        '''
            Do nothing if square type is the following:
                NORMAL, INJAIL
        '''
        if square.type == SquareType.NORMAL or square.type == SquareType.INJAIL:
            return token
        elif square.type == SquareType.CHANCE:
            card = GameLogic.drawCard(chanceCardArr)
            print(card.typeI)
            posIndex = GameLogic.determineNextPosIndexGivenCard(card, board)
            return GameLogic.moveTokenByPosIndexGivenCard(board, token, posIndex)
        elif square.type == SquareType.CC:
            card = GameLogic.drawCard(ccCardArr)
            print(card.typeI)
            posIndex = GameLogic.determineNextPosIndexGivenCard(card, board)
            return GameLogic.moveTokenByPosIndexGivenCard(board, token, posIndex)
        else:
            return GameLogic.moveTokenToJail(token, board)
