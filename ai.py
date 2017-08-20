
import game, position, threat

class AI(game.ConnectFourGame):

    def __init__(self):
        print ""


    # returns integer for which column to move to
    def determineMove(self, board):




        # DEFENSIVE:

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

    # parse an array of positions for threats (can be used for horizontal and diagonals)
    def parseForThreats(self, section):
        print ""

    def getHorizontalThreats(self, board):
        print ""

    def getVerticalThreats(self, board):
        threats = []

        for col in board:

            if len(col) > 0 and col[len(col) - 1].getValue() == "user":

                lowest = 0
                # trace down column until bottom or ai position found
                for i in range(len(col) - 1, -1, -1):
                    if col[i].getValue() == "ai":
                        break
                    else:
                        lowest = i

                # if threat not going to reach top of column
                if lowest <= super(AI, self).getbHeight() - 4:
                    # get chain for threat
                    ch = []

                    for i in range(lowest, len(col)):
                        ch.append(col[i])

                    # append any necessary null positions in threat
                    for i in range(0, 4 - len(ch)):
                        prev = ch[len(ch) - 1]
                        p = position.Position("null", prev.getX(), prev.getY() + 1)
                        ch.append(p)

                    t = threat.Threat("VERTICAL", ch)
                    threats.append(t)

        return threats





    def getRDiagThreats(self, board):
        print ""

    def getLDiagThreats(self, board):
        print ""



























