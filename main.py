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

    t = threat.Threat("HORIZONTAL", chain)

    t.calcPriority()
    print "P: " + str(t.getPriority()) + "\n"

    c = t.getChain()
    for i in c:
        print i.getInfo()

    t.determineSuggestions()
    s = t.getSuggestions()

    print len(s)
    for i in s:
        print i.getInfo()

    g.printBoard()



if __name__ == "__main__":
    main()