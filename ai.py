
import game

class AI(game.ConnectFourGame):

    def __init__(self):
        print "new ai"


    def determineMove(self, board):
        threats = self.getAllThreats(board)

    # get all threats, given a board state
    def getAllThreats(self, board):
        th = []

        h = self.getHorizontalThreats(board)
        v = self.getVerticalThreats(board)
        r = self.getRDiagThreats(board)
        l = self.getLDiagThreats(board)

        th.extend(h)
        th.extend(v)
        th.extend(r)
        th.extend(l)

        return th

    def getHorizontalThreats(self, board):
        print ""

    def getVerticalThreats(self, board):
        print ""

    def getRDiagThreats(self, board):
        print ""

    def getLDiagThreats(self, board):
        print ""