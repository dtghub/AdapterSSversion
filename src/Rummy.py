import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/AdapterSSversion')
from os import truncate
from src.PlayingCard import PlayingCard
import random
import copy


class Rummy:
    playing_card = PlayingCard()

    def initGameState(self):

        initGameState = {
            "rulesFilename": "Gamerules.txt",
            "playerNumber": 0,
            "gameRound": 0,
            "deck": [],
            "hands": [],
            "plays": [],
            "stock": [],
            "score": [],
            "scoreToWin": 1000,
            "numberOfPlayers": 4
        }
        gameState = copy.deepcopy(initGameState)
        return(gameState)



    def initListOfPlays(self):
        initListOfPlays = {
            "playerHand": [],
            "playsFound": [],
            "newPlaysFound": [],
            "playsMadeSoFar": [],
            "bestScoreSoFar": 0
        }
        listOfPlays = copy.deepcopy(initListOfPlays)
        return(listOfPlays)





    def askYorN(self, questionString):
        validResponse = False
        while (not validResponse):
            questionResponse = input(questionString)
            if ((len(questionResponse) == 1) and (questionResponse.lower() in "yn")):
                validResponse = True
            else:
                print("Please enter 'y' or 'n'")
        return(questionResponse.lower() == "y")



    def setupNewDeck(self):
        newDeck = self.playing_card.generate_deck()
        newDeck = self.playing_card.shuffle_cards(newDeck)
        return(newDeck)



    def getCardFromDeck(self, gameState):
        # have we exhauseted the deck?
        # if so, turn over the stock pile and shuffle
        if (gameState["deck"] == []):
            lenOfStock = len(gameState["stock"])
            if (lenOfStock == 1):
                print("Deck is empty. Only the stock card remains!")
                print("Drawing stock card!")
                topCard = self.playing_card.deal_a_card(gameState["stock"])
            else:
                gameState["deck"] = gameState["stock"][0:lenOfStock - 2]
                gameState["stock"] = [gameState["stock"][lenOfStock - 1]]
                self.playing_card.shuffle_cards(gameState["deck"])
                topCard = self.playing_card.deal_a_card(gameState["deck"])
        else:
            topCard = self.playing_card.deal_a_card(gameState["deck"])
        return(topCard)



    def displayRules(self, rulesFilename):
        try:
            with open(rulesFilename, "r") as f:
                emailTemplate = f.read()
        except OSError as err:
            print("Hmmm: something went wrong:")
            print("OS error: {0}".format(err))
            print("Unable to open the game rules file...")
            emailTemplate = ""
        return emailTemplate



    def getNumberFromPlayer(self, inputText, min = -1, max = -1, defaultValue = -1):
        isNotValidInput = True

        while (isNotValidInput):
            isAboveMin = True
            isBelowMax = True

            playerChoice = input(inputText)
            
            if (defaultValue != -1):
                if (playerChoice == ""):
                    playerChoice = str(defaultValue)

            if (playerChoice.isdigit()):
                playerChoice = int(playerChoice)

                rangeInfo = ""
                if (min != -1):
                    rangeInfo = ", minimum; " + str(min)
                if (max != -1):
                    rangeInfo += ", maximum; " + str(max)

                if ((playerChoice < min) and (min != -1)):
                    isAboveMin = False
                if ((playerChoice > max) and (min != -1)):
                    isBelowMax = False

                if (isAboveMin and isBelowMax):
                    isNotValidInput = False
                else:
                    print("Sorry, you need to enter a number" + rangeInfo)

        return(playerChoice)






    def welcomeThePlayer(self, rulesFilename):
        print("\nWelcome to Rummy!\n\n")
        if self.askYorN("Would you like to see the instructions? (y or n): "):
            print(self.displayRules(rulesFilename))



    def askPlayerForPrefs(self, gameState):
        print("If you want, you can just press enter to accept the default answers (shown in brackets) to the following questions.")

        playerChoice = self.getNumberFromPlayer("Please enter the target score to win (1000): ", 10, 100000, 1000)
        gameState["scoreToWin"] = playerChoice

        playerChoice = self.getNumberFromPlayer("Please enter the number of players (4):", 2, 5, 4)
        gameState["numberOfPlayers"] = playerChoice
        
        return(gameState)




    def getPlayerChoices(self, gameState):
        self.welcomeThePlayer(gameState["rulesFilename"])
        gameState = self.askPlayerForPrefs(gameState)
        return(gameState)



    def determinePlayingOrder(self, gameState):
        playerNum = random.randint(0, gameState["numberOfPlayers"] - 1)
        print("You are player number " + str(playerNum + 1))
        gameState["playerNumber"] = playerNum
        return(gameState)



    def initiateEnvironment(self, gameState):
        for i in range(gameState["numberOfPlayers"]):
            gameState["plays"].append([])
        return(gameState)








    # consider implementing 2 decks if more than 5 players (7 cards dealt to each)
    def dealTheHands(self, gameState):
        if (gameState["numberOfPlayers"] < 5):
            cardsPerHand = 10
        else:
            cardsPerHand = 6
        gameState["hands"] = self.playing_card.deal_cards(gameState["deck"], cardsPerHand, gameState["numberOfPlayers"])
        self.playing_card.sort_hands(gameState["hands"])
        return(gameState)








    def displayStock(self, gameState):
        topCard = gameState["stock"][len(gameState["stock"]) - 1]
        print("The top card on the stock pile is:", topCard)



    def initiateTheStock(self, gameState):
        gameState["stock"].append(self.playing_card.deal_a_card(gameState["deck"]))
        self.displayStock(gameState)
        return(gameState)


        
    def displayComputerPosition(self, computerHand, gameState):
        print("Player", computerHand + 1, "has", len(gameState["hands"][computerHand]), "cards left in their hand.")
        if (len(gameState["plays"][computerHand]) > 0):
            print("They have played the following:", gameState["plays"][computerHand])



    def displayPlayerPosition(self, gameState):
        playerHand = gameState["playerNumber"]
        print("You are player", playerHand+1)
        print("You have the following cards in your hand:", gameState["hands"][playerHand])
        if (len(gameState["plays"][playerHand]) > 0):
            print("You have played the following:")
            for plays in gameState["plays"][playerHand]:
                self.playing_card.convert_numbers_to_faces(plays)
                print(plays)
                self.playing_card. convert_faces_to_numbers(plays)
        





    def displayInitialPosition(self, gameState):
        print("Under construction")

        self.displayStock(gameState)

        for handToDisplay in range(gameState["numberOfPlayers"]):
            if handToDisplay == gameState["playerNumber"]:
                self.displayPlayerPosition(gameState)
            else:
                self.displayComputerPosition(handToDisplay, gameState)







    def setupNewGame(self, gameState):
        gameState["deck"] = self.setupNewDeck()
        gameState = self.getPlayerChoices(gameState)
        gameState = self.determinePlayingOrder(gameState)
        gameState = self.initiateEnvironment(gameState)
        gameState = self.dealTheHands(gameState)
        gameState = self.initiateTheStock(gameState)
        self.displayInitialPosition(gameState)
        print(gameState)
        return(gameState)








    # set up the listOfPlays structure at the start of the evaluation
    def setupListOfPlays(self, gameState, currentPlayer):
        listOfPlays = self.initListOfPlays()
        listOfPlays["playsFound"] = copy.deepcopy(gameState["plays"][currentPlayer])
        listOfPlays["playerHand"] = copy.deepcopy(gameState["hands"][currentPlayer])

        return(listOfPlays)


























    # check to see if the next x cards are sequential (x = playLength)
    def checkForRun(self, startPosition, playLength, playerHand):
        isMatch = True
        for i in range(startPosition, startPosition + playLength - 1):
            if (isMatch):
                if ((playerHand[i][0] != playerHand[i + 1][0]) or (int(playerHand[i][1:3]) != (int(playerHand[i + 1][1:3]) - 1))):
                    isMatch = False 
        if (isMatch):
            setToReturn = playerHand[startPosition:(startPosition + playLength)]
        else:
            setToReturn = []

        return(setToReturn)




    # find the first x cards with the same face value as the starting card (x = playLength)
    def checkForSet(self, startPosition, playLength, playerHand):
        cardToMatch = playerHand[startPosition]
        faceValueToMatch = cardToMatch[1:3]
        cardsMatched = 1
        setToReturn = [cardToMatch]
        for i in range(startPosition + 1, len(playerHand)):
            if (playerHand[i][1:3] == faceValueToMatch):
                cardsMatched += 1
                if (cardsMatched <= playLength):
                    setToReturn.append(playerHand[i])
        if (cardsMatched < playLength):
            setToReturn = []

        return(setToReturn)



    # start with the card in position 0 in the hand, and see if a run or set can be formed from it, then move on to the card in position 1 etc
    def findSetsOrRuns(self, listOfPlays, playLength):
        isPlaysFound = False
        for i in range(len(listOfPlays["playerHand"]) - playLength + 1):
            playsFound = self.checkForRun(i, playLength, listOfPlays["playerHand"])
            if (playsFound != []):
                listOfPlays["newPlaysFound"].append(playsFound)
                isPlaysFound = True
            playsFound = self.checkForSet(i, playLength, listOfPlays["playerHand"])
            if (playsFound != []):
                listOfPlays["newPlaysFound"].append(playsFound)
                isPlaysFound = True
        return(listOfPlays, isPlaysFound)



    # identify what run and set plays are possible from the current position
    def generateListOfRunsAndSets(self, listOfPlays):
        numberOfCardsInThePlay = 3
        isPlaysFound = True
        lengthOfTheHand = len(listOfPlays["playerHand"])
        if lengthOfTheHand == 0:
            isPlaysFound = False
        # start by identifying plays of 3 cards, then look for 4 etc
        # if there aren't any 4-length plays then there won't be any 5, 6 etc
        while(isPlaysFound and (numberOfCardsInThePlay <= lengthOfTheHand)):
            listOfPlays, isPlaysFound = self.findSetsOrRuns(listOfPlays, numberOfCardsInThePlay)
            numberOfCardsInThePlay += 1

        return(listOfPlays)












    # see if the card can be added to the start or end of a set
    def checkForMeldSet(self, handPosition, listOfPlays, setToCheck):
        replacedSet = []
        setToReplace = []
        cardToMeld = []

        cardToMatch = listOfPlays["playerHand"][handPosition]
        faceToMatch = cardToMatch[1:3]

        if (setToCheck[0][1:3] == faceToMatch):
            newSet = copy.deepcopy(setToCheck)
            newSet.append(cardToMatch)
            replacedSet = setToCheck
            setToReplace = newSet
            cardToMeld = cardToMatch
    
        if (cardToMeld != []):
            playToReturn = []
            playToReturn.append([cardToMeld])
            playToReturn.append(setToReplace)
            playToReturn.append(replacedSet)
        else:
            playToReturn = []

        return(playToReturn)



    # see if the card can be added to the start or end of a run
    def checkForMeldRun(self, startPosition, listOfPlays, runToCheck):

        replacedRun = []
        runToReplace = []
        cardToMeld = []

        print(runToCheck)
        # runToCheck = self.playing_card.convert_face_to_number(runToCheck)


        cardToMatch = listOfPlays["playerHand"][startPosition]
        suitToMatch = cardToMatch[0]
        faceToMatch = cardToMatch[1:3]

        firstCard = 0
        lastCard = len(runToCheck) - 1

        if ((runToCheck[firstCard][0] == suitToMatch) and (int(runToCheck[firstCard][1:3]) == int(faceToMatch) + 1)):
            # runToCheck = self.playing_card.convert_number_to_face(runToCheck)
            newRun = [cardToMatch]
            newRun.extend(runToCheck)
            replacedRun = runToCheck
            runToReplace = newRun
            cardToMeld = cardToMatch

        if ((runToCheck[lastCard][0] == suitToMatch) and (int(runToCheck[lastCard][1:3]) == int(faceToMatch)-1)):
            # runToCheck = self.playing_card.convert_number_to_face(runToCheck)
            newRun = copy.deepcopy(runToCheck)
            newRun.append(cardToMatch)
            replacedRun = runToCheck
            runToReplace = newRun
            cardToMeld = cardToMatch

        if (cardToMeld != []):
            playToReturn = []
            playToReturn.append([cardToMeld])
            playToReturn.append(runToReplace)
            playToReturn.append(replacedRun)
        else:
            playToReturn = []

        return(playToReturn)







    def checkForMelds(self, handPosition, listOfPlays):
        meldsFound = []
        for playToCheck in listOfPlays["playsFound"]:
            # is it a set? if not it's a run
            if (playToCheck[0][1:3] == playToCheck[1][1:3]):
                meldPlay = self.checkForMeldSet(handPosition, listOfPlays, playToCheck)
            else:
                meldPlay = self.checkForMeldRun(handPosition, listOfPlays, playToCheck)
            if (meldPlay != []):
                meldsFound.append(meldPlay)
        return(meldsFound)



    def generateListOfMeldsFound(self, listOfPlays):
        # we can only meld cards to plays already made
        if (len(listOfPlays["playsFound"]) > 0):
            for i in range(len(listOfPlays["playerHand"])):
                playsFound = self.checkForMelds(i, listOfPlays)
                if (playsFound != [] ):
                    for playFound in playsFound:
                        listOfPlays["newPlaysFound"].append(playFound)
        return(listOfPlays)








    def findPlaysInHand(self, listOfPlays):
        listOfPlays = self.generateListOfRunsAndSets(listOfPlays)
        listOfPlays = self.generateListOfMeldsFound(listOfPlays)
        return(listOfPlays)




    def calculateScore(self, listOfPlays):
        totalScore = 0
        for play in listOfPlays["playsFound"]:
            self.playing_card.convert_faces_to_numbers(play)
            for card in play:
                cardValue = int(card[1:3])
                totalScore += cardValue
            self.playing_card.convert_numbers_to_faces(play)
        listOfPlays["bestScoreSoFar"] = totalScore
        return(listOfPlays)





    def removeCardsFromHand(self, playerHand, cardsToRemove):
        for nextCard in cardsToRemove:
                playerHand.remove(nextCard)
        return(playerHand)



    def incorporateTheNewPlay(self, listOfPlays, playToEvaluate):

        # update listOfPlays to record that playToEvaluate has been applied    
        listOfPlays["newPlaysFound"] = []
        listOfPlays["playsMadeSoFar"].append(playToEvaluate)
        # is the play we're evaluating a new run or set, or just to meld one card?
        if (len(playToEvaluate[1][0]) == 1):
            # run or set
            listOfPlays["playsFound"].append(playToEvaluate)
            listOfPlays["playerHand"] = self.removeCardsFromHand(listOfPlays["playerHand"], playToEvaluate)  
        else:
            # it's a meld
            print(playToEvaluate)
            meldedCard = playToEvaluate[0]
            print(meldedCard)
            print(meldedCard[0])
            newPlay = playToEvaluate[1]
            originalPlay = playToEvaluate[2]
            listOfPlays["playerHand"].remove(meldedCard[0])
            listOfPlays["playsFound"].remove(originalPlay)
            listOfPlays["playsFound"].append(newPlay)

        return(listOfPlays)






    # called recursively until no more plays found, then calculates score and returns the highest-score-found-so-far as each call returns
    def findBestScoreForHand(self, listOfPlays):
        bestPlay = copy.deepcopy(listOfPlays)

        # identify what if any plays are possible with the hand
        listOfPlays = self.findPlaysInHand(listOfPlays)

        # if play(s) have been identified, they need evaluated, so recurse and keep the best score which is returned
        if (listOfPlays["newPlaysFound"] != []):
            for newPlayFound in listOfPlays["newPlaysFound"]:
                newPlay = copy.deepcopy(listOfPlays)
                newPlay = self.incorporateTheNewPlay(newPlay, newPlayFound)
                newPlay = self.findBestScoreForHand(newPlay)
                newPlay = self.calculateScore(newPlay)
                if (newPlay["bestScoreSoFar"] >= bestPlay["bestScoreSoFar"]):
                    bestPlay = copy.deepcopy(newPlay)

        return(bestPlay)






    # here we call the evaluate best hand routine, firstly just with the hand and then with the top card on the discard pile - if including the top discard card improves the score we go with that, otherwise we draw a card from the pile and play based on that
    def decideDiscardOrStockAndThenPlay(self, gameState, listOfPlays):

        # what is the best score we can have without drawing a card?
        justHand = copy.deepcopy(listOfPlays)
        justHand = self.findBestScoreForHand(justHand)
        

        # add the top card from the stock and try again
        topCard = gameState["stock"][len(gameState["stock"]) - 1]
        topCard = self.playing_card. convert_face_to_number(topCard)
        withTopCard = copy.deepcopy(listOfPlays)
        withTopCard["playerHand"].append(topCard)
        withTopCard["playerHand"].sort()
        withTopCard = self.findBestScoreForHand(withTopCard)


        if (withTopCard["bestScoreSoFar"] > justHand["bestScoreSoFar"]):
            listOfPlays = withTopCard
            topCard = self.playing_card. convert_number_to_face(topCard)
            print("Player draws the", topCard, "from the stock pile.")
            gameState["stock"].pop()
        else:
            # the stock card didn't help, so take the chance with the stock card
            cardFromDeck = self.getCardFromDeck(gameState)
            cardFromDeck = self.playing_card. convert_face_to_number(cardFromDeck)
            print("Player takes a card from the deck.")
            listOfPlays["playerHand"].append(cardFromDeck)
            listOfPlays["playerHand"].sort()
            listOfPlays = self.findBestScoreForHand(listOfPlays)

        return(gameState, listOfPlays)



    def pickACardToDiscard(self, gameState, listOfPlays):
        numberOfCardsLeftInHand = len(listOfPlays["playerHand"])
        if (numberOfCardsLeftInHand > 0):
            positionOfCardToDiscard = random.randint(1, numberOfCardsLeftInHand) - 1
            cardToDiscard = listOfPlays["playerHand"][positionOfCardToDiscard]
            listOfPlays["playerHand"].pop(positionOfCardToDiscard)

            print("Player discards", cardToDiscard)
            gameState["stock"].append(cardToDiscard)
        return(gameState, listOfPlays)



    def reportWhatWasPlayed(self, listOfPlays):
        for playMade in listOfPlays["playsMadeSoFar"]:
            if (len(playMade[1][0]) == 1):
                # run or set
                facesList = copy.deepcopy(playMade)
                self.playing_card.convert_numbers_to_faces(facesList)
                print("Player played:", facesList)
            else:
                # it's a meld
                meldedCard = playMade[0]
                self.playing_card.convert_numbers_to_faces(meldedCard)
                newPlay = playMade[1]
                self.playing_card.convert_numbers_to_faces(newPlay)
                originalPlay = playMade[2]
                self.playing_card.convert_numbers_to_faces(originalPlay)
                
                print(
                    "Player melded the", meldedCard,
                    "card to", originalPlay,
                    "to make the new play:", newPlay
                )
                



    def incorporateThePlaysMade(self, gameState, listOfPlays, currentPlayer):
        gameState["hands"][currentPlayer] = listOfPlays["playerHand"]
        gameState["plays"][currentPlayer] = listOfPlays["playsFound"]
        return(gameState)



    def playComputerTurn(self, gameState, currentPlayer):
        # currentPlayer = 0 #dummy value for just now
        print("\n\nPlayer number", currentPlayer + 1, "plays.")

        listOfPlays = self.setupListOfPlays(gameState, currentPlayer)
        self.playing_card. convert_faces_to_numbers(listOfPlays["playerHand"])
        listOfPlays["playerHand"].sort()

        gameState, listOfPlays = self.decideDiscardOrStockAndThenPlay(gameState, listOfPlays)

        self.playing_card.convert_numbers_to_faces(listOfPlays["playerHand"])

        gameState, listOfPlays = self.pickACardToDiscard(gameState, listOfPlays)
        self.reportWhatWasPlayed(listOfPlays)
        gameState = self.incorporateThePlaysMade(gameState, listOfPlays, currentPlayer)
        return(gameState)











    def playerChoiceDeckOrStock(self, gameState, listOfPlays):
        isToDrawStockCard = self.askYorN("Do you want to take the top stock card? (y/n): ")
        if (isToDrawStockCard):
            cardDrawn = gameState["stock"].pop()
            cardDrawn = self.playing_card. convert_face_to_number(cardDrawn)
        else:
            cardDrawn = self.getCardFromDeck(gameState)
            print("You have drawn", cardDrawn, "from the deck.")
            cardDrawn = self.playing_card. convert_face_to_number(cardDrawn)
            
        self.playing_card. convert_faces_to_numbers(listOfPlays["playerHand"])
        listOfPlays["playerHand"].append(cardDrawn)
        listOfPlays["playerHand"].sort()
        self.playing_card.convert_numbers_to_faces(listOfPlays["playerHand"])

        return(listOfPlays)












    def listPlaysAndGetPlayerChoice(self, listOfPlays):
        isKeepGoing = True
        print("Please choose from the following options:")
        playerChoices = listOfPlays["newPlaysFound"]
        for i, playerOption in enumerate(playerChoices):

            if (len(playerOption[1][0]) == 1):
                self.playing_card.convert_numbers_to_faces(playerOption)
                print(i,")", playerOption)
                self.playing_card. convert_faces_to_numbers(playerOption)
            else:
                meldedCard = playerOption[0]
                self.playing_card.convert_numbers_to_faces(meldedCard)
                newPlay = playerOption[1]
                self.playing_card.convert_numbers_to_faces(newPlay)
                originalPlay = playerOption[2]
                self.playing_card.convert_numbers_to_faces(originalPlay)
                
                print(
                    i, ")",
                    "Meld the", meldedCard,
                    "card to", originalPlay,
                    "to make the new play:", newPlay
                )

        print(len(playerChoices), ") No play")

        playNumberChosenByPlayer = self.getNumberFromPlayer("\nPlease select:", 0, len(playerChoices))
        if (playNumberChosenByPlayer < len(playerChoices)):
            playerChoice = playerChoices[playNumberChosenByPlayer]
            self.playing_card. convert_faces_to_numbers(listOfPlays["playerHand"])
            listOfPlays = self.incorporateTheNewPlay(listOfPlays, playerChoice)
            self.playing_card.convert_numbers_to_faces(listOfPlays["playerHand"])
        else:
            isKeepGoing = False

        return(listOfPlays, isKeepGoing)













    def getPlayersChoiceOfPlays(self, listOfPlays):
        isKeepGoing = True
        while (isKeepGoing):
            self.playing_card. convert_faces_to_numbers(listOfPlays["playerHand"])
            listOfPlays["playerHand"].sort()
            listOfPlays = self.findPlaysInHand(listOfPlays)
            self.playing_card.convert_numbers_to_faces(listOfPlays["playerHand"])
            print("Looking for a play option...")

            if (listOfPlays["newPlaysFound"] != []):
                listOfPlays, isKeepGoing = self.listPlaysAndGetPlayerChoice(listOfPlays)
            else:
                print("You have no valid plays available")
                isKeepGoing = False
        return(listOfPlays)




    def getPlayersChoiceOfCardToReturnToStock(self, gameState, listOfPlays):
        numberOfCardsLeft = len(listOfPlays["playerHand"])
        if (numberOfCardsLeft == 0):
            print("You have played all of your cards")
        elif (numberOfCardsLeft == 1):
            print("You must return your remaining card", listOfPlays["playerHand"], "to the stock pile")
            gameState["stock"].append(listOfPlays["playerHand"])
            listOfPlays["playerHand"] = ""
        else:
            print("Please choose a card from your hand to return to stock:")
            playerChoices = listOfPlays["playerHand"]
            for i, playerOption in enumerate(playerChoices):
                print(i,")", playerOption)
            cardNumberChosenByPlayer = self.getNumberFromPlayer("\nPlease select:", 0, len(playerChoices))
            gameState["stock"].append(listOfPlays["playerHand"][cardNumberChosenByPlayer])
            listOfPlays["playerHand"].pop(cardNumberChosenByPlayer)

        return(gameState, listOfPlays)










    def playersTurn(self, gameState):
        self.displayPlayerPosition(gameState)
        self.displayStock(gameState)

        listOfPlays = self.setupListOfPlays(gameState, gameState["playerNumber"])

        #insert listofplays convert faces to numbers here

        listOfPlays = self.playerChoiceDeckOrStock(gameState, listOfPlays)

        
        listOfPlays = self.getPlayersChoiceOfPlays(listOfPlays)
    
        gameState, listOfPlays = self.getPlayersChoiceOfCardToReturnToStock(gameState, listOfPlays)

        gameState = self.incorporateThePlaysMade(gameState, listOfPlays, gameState["playerNumber"])




















    def hasLastCardBeenPlayed(self, gameState, currentPlayer):
        isGameToContinue = True
        if (len(gameState["hands"][currentPlayer]) == 0):
            isGameToContinue = False
        return(isGameToContinue)



    def playGame(self, gameState):
        isGameInProgress = True
        gameNumber = 1

        while (isGameInProgress):
            currentPlayer = (gameNumber - 1) % (gameState["numberOfPlayers"])
            if (currentPlayer == gameState["playerNumber"]):
                self.playersTurn(gameState)
            else:
                self.playComputerTurn(gameState, currentPlayer)

            isGameInProgress = self.hasLastCardBeenPlayed(gameState, currentPlayer)

            gameNumber += 1
        return(gameState)
















    def main(self):
        gameState = self.initGameState()

        gameState = self.setupNewGame(gameState)


        isGameInProgress = True



        # the game control logic should probably be broken out to a function
        # loop and then if playermyber = hand number then do player turn else compuerturn
        while isGameInProgress:

            gameState = self.playGame(gameState)

            # currentPlayer = 0

            # gameState = self.playComputerTurn(gameState, currentPlayer) # currentPlayer logic needs added

            # gameState = self.playersTurn(gameState)
            
            # gameState = playComputerHandsSecondStage(gameState)

            # for testing purposes
            # isGameInProgress = False





        print(gameState)
        print()
        print(gameState["deck"])





if __name__ == "__main__":
    rummy = Rummy()
    rummy.main()