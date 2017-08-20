import position

class ConnectFourGame(object):

    __board = []
    __bWidth = 7
    __bHeight = 6

    # initialize board as 2d array
    for i in range(0, 7):
        __board.append([])

    def __init__(self):
        print ""

    # push position object of a given type to a given column in board
    def move(self, column, type):
        # check if index in range
        if column < len(self.__board) and len(self.__board[column]) < 6:
            p = position.Position(type, column, len(self.__board[column]))
            self.__board[column].append(p)
        else:
            print "Unable to make move"





    def getBoard(self):
        return self.__board

    def printBoard(self):
        i = 0
        for x in self.__board:
            print "Col " + str(i) + ": ",
            i += 1

            for y in x:
                print "[" + y.getInfo() + "]",
            print ""

    def getbWidth(self):
        return self.__bWidth

    def getbHeight(self):
        return self.__bHeight