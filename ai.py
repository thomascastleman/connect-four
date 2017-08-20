
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
    def parseForThreats(self, section, type):
        threats = []                # array of all threats found in section
        startingPositions = []      # array of starting positions of threats, to prevent duplicates

        for pos in section:
            # if null position found, check for threats
            if pos.getValue() == "null":

                # for every possible surrounding threat
                for x in range(pos.getX() - 3, pos.getX() + 1):

                    # ensure index in range
                    if x >= 0 and x <= len(section) - 4:

                        # check if threat already been evaluated to prevent duplicates
                        if x not in startingPositions:
                            # get subsection
                            chain = section[x: x + 4]

                            # check if threat legitimate (no ai positions, and contains at least one user position)
                            isThreat = True
                            numUser = 0
                            for p in chain:
                                if p.getValue() == "ai":
                                    isThreat = False
                                elif p.getValue() == "user":
                                    numUser += 1

                            if isThreat and numUser > 0:
                                t = threat.Threat(type, chain)
                                threats.append(t)
                                startingPositions.append(x)

        return threats

    def getHorizontalThreats(self, board):
        max = 0
        # get max column size
        for col in board:
            if len(col) > max:
                max = len(col)

        threats = []

        for r in range(0, max):
            # get every non empty row
            row = []
            for col in board:
                # if position exists
                if r < len(col):
                    row.append(col[r])
                # otherwise create null position
                else:
                    row.append(position.Position("null", board.index(col), r))

            # add all threats in row to threats array
            t = self.parseForThreats(row, "HORIZONTAL")
            threats.extend(t)

        return threats

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



























