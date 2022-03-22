
class Player():

    def __init__(self, playerID = ''):
        self.playerID = playerID
        self.currentNums = []
        self.score = 0
    
    def setScore(self, score):
        self.score = score
    
    def updateCurrentNums(self, nums):
        self.currentNums = nums
    
    