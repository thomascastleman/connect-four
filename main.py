import threat, ai, game, position

import random

def main():

    a = ai.AI()
    g = game.ConnectFourGame()

    # make some random moves for debug
    for i in range(0, 7):
        r = random.randrange(0, 2)
        if r == 0:
            s = "user"
        else:
            s = "ai"
        g.move(random.randrange(0, 7), s)


    # # debug vertical threats
    # vert = a.getVerticalThreats(g.getBoard())
    # print str(len(vert)) + " threats found"
    #
    # print "\nThreat info: "
    # for v in vert:
    #     v.calcPriority()
    #     print v.getInfo()
    # print "\n\n"

    # # debug horizontal threats
    # horiz = a.getHorizontalThreats(g.getBoard())
    # print str(len(horiz)) + " threats found"
    #
    # print "\nThreat info: "
    # for h in horiz:
    #     h.calcPriority()
    #     print h.getInfo()
    # print "\n\n"

    # debug diagonal threats
    d = a.getDiagonalThreats(g.getBoard())
    print str(len(d)) + " threats found"

    print "\nThreat info: "
    for t in d:
        t.calcPriority()
        print t.getInfo()
    print "\n\n"


    g.printBoard()



if __name__ == "__main__":
    main()

















