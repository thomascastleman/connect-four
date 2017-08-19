
# an element in the board, is either null, user, or ai
class Position():

    __x = 0
    __y = 0
    __value = ""

    def __init__(self, val, x, y):
        self.__x = x
        self.__y = y
        self.__value = val

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getValue(self):
        return self.__value