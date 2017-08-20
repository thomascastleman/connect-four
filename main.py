import threat, ai, game, position

import random

def main():

    th = threat.Threat("VERTICAL", [])
    a = ai.AI()
    g = game.ConnectFourGame()
    pos = position.Position("null", 3, 2)

    print ""


    # make some random moves
    for i in range(0, 7):
        r = random.randrange(0, 2)
        if r == 0:
            s = "user"
        else:
            s = "ai"
        g.move(random.randrange(0, 7), s)


    # debug vertical threats
    vert = a.getVerticalThreats(g.getBoard())
    print str(len(vert)) + " threats found"

    print "\nThreat info: "
    for v in vert:
        v.calcPriority()
        print v.getInfo()
    print "\n\n"


    g.printBoard()



if __name__ == "__main__":
    main()

















