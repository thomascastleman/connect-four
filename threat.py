import game, position

# keeps track of chains of
class Threat(game.ConnectFourGame):

    __chain = []   # array of positions involved in threat
    __type = ""     # either VERTICAL, HORIZONTAL, LDIAG, or RDIAG
    __priority = 0  # number of opponenent moves away from completion

    def __init__(self, type):
        self.__type = type
        print self.__type


    # calculate priority of threat
    def calcPriority(self):
        print ""

    # get suggestions for neutralization moves
    def getSuggestions(self):
        print ""



    # getters and setters:

    def getChain(self):
        return self.__chain

    def getType(self):
        return self.__type

    def getPriority(self):
        return self.__priority
