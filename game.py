import position

class ConnectFourGame(object):

    __board = []

    # initialize board as 2d array
    for i in range(0, 7):
        __board.append([])

    def __init__(self):
        print "new game"

    # push position object of a given type to a given column in board
    def move(self, column, type):
        # check if index in range
        if column < len(self.__board):
            p = position.Position(type, column, len(self.__board[column]) - 1)
            self.__board[column].append(p)
        else:
            print "Column out of range. Unable to make move"





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