import threat, ai, game, position

import random

def main():

    th = threat.Threat("VERTICAL", [])
    a = ai.AI()
    g = game.ConnectFourGame()
    pos = position.Position("null", 3, 2)

    print ""

    board = g.getBoard()
    for x in range(0, 7):
        rand = random.randrange(0, 3)
        if rand == 0:
            s = "ai"
        elif rand == 1:
            s = "user"
        else:
            s = "null"

        if (s != "null"):
            p = position.Position(s, x, 0)
            board[x].append(p)


    chain = []
    for x in range(0, 4):
        if len(board[x]) > 0:
            chain.append(g.getBoard()[x][0])
        else:
            chain.append(position.Position("null", x, 0))

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