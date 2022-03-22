import random
from player import *
from outcome import *

class Yahtzee():

    outcomes = [ "ONES", "TWOS" ]
    numTries = 3

    def __init__(self):
        self.currentPlayer = 0
        self.currentNums = [ [], [] ] # [ [player 1 nums], [player 2 nums] ]
        self.turnNum = 0
        self.gameContinue = True
        print(self.currentNums)
    
    def run(self):
        while (self.gameContinue):
            self.runOneIteration()
    
    def runOneIteration(self):
        print(self.currentNums)
        print(f'Current Player: {self.currentPlayer}')

        # Generate random numbers
        currentNums = self.currentNums[self.currentPlayer]
        print(f'Current Numbers: {currentNums}')
        

        # Determine the new numbers that need to be selected
        numsLeft = 5 - len(currentNums)

        newNums = random.choices(range(1,7), k = numsLeft)
        print(f'New Numbers: {newNums}')

        # Ask user which numbers to keep - for now have them type the indices
        indices = input("Enter the indices of the numbers that you want to keep: ").split(",")

        # Update the player's current numbers based on the indices
        self.currentNums[self.currentPlayer] += [newNums[int(index)] for index in indices]
        
        # End the game -- FOR DEBUGGING PURPOSES
        self.gameContinue = len(self.currentNums[self.currentPlayer]) != 5

        self.turnNum += 1

        if (self.turnNum >= self.numTries):
            # Let the player choose their outcome
            self.chooseOutcome()

            self.currentPlayer = 1 - self.currentPlayer

    def chooseOutcome(self):
        pass
    
    def createGame(self):
        pass
    
    def getGameContinue(self):
        return self.gameContinue
    
    def setGameContinue(self, newVal):
        self.gameContinue = newVal




if __name__ == '__main__':
    game = Yahtzee()
    game.run()