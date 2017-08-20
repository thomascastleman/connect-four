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



    # debug threats
    threats = a.getAllThreats(g.getBoard())
    print str(len(threats)) + " threats found"

    print "\nThreat info: "
    for t in threats:
        t.calcPriority()
        t.determineSuggestions()
        print t.getInfo()
        print ""

    print "\n\n"


    g.printBoard()



if __name__ == "__main__":
    main()

















