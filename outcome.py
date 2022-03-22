from constants import *

class YahtzeeOutcome():

    def __init__(self):
        self.numYahtzees = 0
        self.outcome = ''
    
    def selectOutcome(self):
        print('Possible outcomes: ', '.'.join(OUTCOMES))
        outcome = input('Choose an outcome: ')

        while outcome not in OUTCOMES:
            print('Possible outcomes: ', '.'.join(OUTCOMES))
            outcome = input('That was not a valid outcome')
        
        self.outcome = outcome

    
    def getScore(self, outcome, nums):
        
        if (outcome == 'ONES'):

            score = nums.count(1)
        
        elif (outcome == 'TWOS'):

            score = nums.count(2)
        
        elif (outcome == 'YAHTZEE'):
            
            if (nums.count(nums[0]) == 5):
                score = 100 * (self.numYahtzees + 1)
                self.numYahtzees += 1
            else:
                score = 0

        return score
    
    def selectBestOutcome(self, nums):

        bestScore = -1
        bestOutcome = ''
        for outcome in OUTCOMES:
            score = self.getScore(outcome, nums)
            if (score > bestScore):
                bestScore = score
                bestOutcome = outcome
        
        return bestOutcome, bestScore
   