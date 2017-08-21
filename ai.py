
import game, position, threat
import random

class AI(game.ConnectFourGame):

    def __init__(self):
        pass


    # returns integer for which column to move to
    def determineMove(self, board):




        # DEFENSIVE:

        threats = self.getAllThreats(board)

        # array of all suggestions from the highest priority group (lowest priority value)
        prioritySuggestions = []

        if len(threats) > 0:
            threats[0].calcPriority()
            highestPriority = threats[0].getPriority()
            leastPriority = threats[0].getPriority()

            # map of move suggestions to their frequencies across all threats
            suggestFrequency = {}

            # calculate priorities and suggestions
            for t in threats:
                # calculate threat priority
                t.calcPriority()

                # update max and min priority values
                if t.getPriority() < highestPriority:
                    highestPriority = t.getPriority()
                elif t.getPriority() > leastPriority:
                    leastPriority = t.getPriority()


                # get suggestions and suggestion frequencies
                t.determineSuggestions()
                sug = t.getSuggestions()

                # add / update suggestion frequency
                for s in sug:
                    if s.getX() in suggestFrequency:
                        suggestFrequency[s.getX()] += 1
                    else:
                        suggestFrequency[s.getX()] = 1

                # DEBUG
                print t.getInfo()

            # in case no suggestions found from highest priority group, try other groups
            while highestPriority <= leastPriority:
                prioritySuggestions = []

                for t in threats:
                    if t.getPriority() == highestPriority:

                        # DEBUG

                        print "\n" + t.getInfo(),


                        for s in t.getSuggestions():
                            if s.getX() not in prioritySuggestions:
                                prioritySuggestions.append(s.getX())


                if len(prioritySuggestions) > 0:
                    break
                else:
                    highestPriority += 1

            print "\n\n"


        if len(prioritySuggestions) > 0:
            maxFreq = prioritySuggestions[0]
            for move in prioritySuggestions:
                if suggestFrequency[move] > suggestFrequency[maxFreq]:
                    maxFreq = move

            # DEBUG
            print "\n\nHighest frequency move found: " + str(maxFreq)

            return maxFreq
        else:
            # no suggestions, make offensive move??

            print "No suggestions found\n"

    # get all threats, given a board state
    def getAllThreats(self, board):
        th = []

        h = self.getHorizontalThreats(board)
        v = self.getVerticalThreats(board)
        d = self.getDiagonalThreats(board)

        th.extend(h)
        th.extend(v)
        th.extend(d)

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

            for c in range(0, len(board)):
                # if position exists
                if r < len(board[c]):
                    row.append(board[c][r])
                else:
                    # otherwise create null position
                    row.append(position.Position("null", c, r))

            # add all threats in row to threats array
            threats.extend(self.parseForThreats(row, "HORIZONTAL"))

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

    def getDiagonalThreats(self, board):
        threats = []

        y = 0
        # rightX starts at n - 1 from last col index
        rightX = super(AI, self).getbWidth() - 4

        # leftX starts at n - 1 from first column index
        leftX = 0 + (4 - 1) # don't give me that look

        # as rightX decrements towards left and leftX increments towards right
        while rightX >= 0 and leftX < super(AI, self).getbWidth():
            # get right diagonal
            diag = self.getDiagonalFromStart(board, rightX, y, "right")
            threats.extend(self.parseForThreats(diag, "RDIAG"))
            rightX -= 1

            # get left diagonal
            diag = self.getDiagonalFromStart(board, leftX, y, "left")
            threats.extend(self.parseForThreats(diag, "LDIAG"))
            leftX += 1


        # rightX rests at first column as y ascends
        rightX = 0
        # leftX rests at last column as y ascends
        leftX = super(AI, self).getbWidth() - 1

        # y ascends to column height - n (+1 is for exclusive index in for loop)
        for y in range(1, (super(AI, self).getbHeight() - 4) + 1):
            # get right diagonal
            diag = self.getDiagonalFromStart(board, rightX, y, "right")
            threats.extend(self.parseForThreats(diag, "RDIAG"))

            # get left diagonal
            diag = self.getDiagonalFromStart(board, leftX, y, "left")
            threats.extend(self.parseForThreats(diag, "LDIAG"))

        return threats

    def getDiagonalFromStart(self, board, startX, startY, direction):
        diagonal = []

        tempX = startX
        tempY = startY
        while (tempX < super(AI, self).getbWidth() if direction == "right" else tempX >= 0) and tempY < super(AI, self).getbHeight():
            if len(board[tempX]) > tempY:
                diagonal.append(board[tempX][tempY])
            else:
                p = position.Position("null", tempX, tempY)
                diagonal.append(p)

            # increment or decrement tempX based on direction
            tempX = (tempX + 1 if direction == "right" else tempX - 1)
            tempY += 1

        return diagonal


























