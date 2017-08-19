import game, position

# keeps track of chains of
class Threat(game.ConnectFourGame):

    __chain = []            # array of positions involved in threat
    __type = ""             # either VERTICAL, HORIZONTAL, LDIAG, or RDIAG
    __priority = 0          # number of opponenent moves away from completion
    __suggestions = []      # array of positions as suggested moves

    def __init__(self, type, chain):
        self.__type = type
        self.__chain = chain
        print self.__type


    # calculate priority of threat
    def calcPriority(self):
        board = super(Threat, self).getBoard()

        for pos in self.__chain:
            if pos.getValue() == "null":
                # if vertical, sum null positions
                if self.__type == "VERTICAL":
                    self.__priority += 1

                # for all other types, sum number of moves to completed threat (opponent win)
                else:
                    self.__priority += (pos.getY() - (len(board[pos.getX()]) - 1))

    # get suggestions for neutralization moves
    def determineSuggestions(self):
        # if priority 1, take only null position as suggestion
        if self.__priority == 1:
            for p in self.__chain:
                if p.getValue() == "null":
                    self.__suggestions.append(p)
        # otherwise, get all null positions that are accessible in one move
        else:
            for p in self.__chain:
                # if empty position
                if p.getValue() == "null":

                    if self.__type == "VERTICAL":
                        return p
                    else:
                        # if valid move
                        if p.getY() == len(super(Threat, self).getBoard()[p.getX()]):
                            # add to suggestions
                            self.__suggestions.append(p)



    # getters and setters:

    def getChain(self):
        return self.__chain

    def getType(self):
        return self.__type

    def getPriority(self):
        return self.__priority

    def getSuggestions(self):
        return self.__suggestions
