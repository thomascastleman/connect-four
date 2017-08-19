

class ConnectFourGame(object):

    __board = []

    # initialize board as 2d array
    for i in range(0, 7):
        __board.append([])

    def __init__(self):
        print "new game"

    def getBoard(self):
        return self.__board

    def printBoard(self):
        i = 0
        for x in self.__board:
            print "Col " + str(i) + ": ",
            i += 1

            for y in x:
                print y,
            print ""