import threat, ai, game, position

import random

def main():

    a = ai.AI()
    g = game.ConnectFourGame()

    # make some random moves for debug
    # for i in range(0, 7):
    #     r = random.randrange(0, 2)
    #     if r == 0:
    #         s = "user"
    #     else:
    #         s = "ai"
    #     g.move(random.randrange(0, 7), s)

    # g.move(4, "user")
    # g.move(3, "ai")
    # g.move(4, "user")
    # g.move(4, "ai")
    # g.move(3, "user")
    # g.move(3, "ai")
    # g.move(2, "user")
    # g.move(2, "ai")
    # g.move(5, "user")
    # g.move(5, "ai")
    # g.move(2, "user")
    # g.move(2, "ai")
    # g.move(1, "user")
    # g.move(1, "ai")
    # g.move(4, "user")
    # g.move(5, "ai")
    # g.move(3, "user")
    # g.move(4, "ai")
    # g.move(5, "user")
    # g.move(3, "ai")
    # g.move(6, "user")
    # g.move(6, "ai")
    # g.move(0, "user")
    # g.move(0, "ai")
    # g.move(1, "user")
    # g.move(1, "ai")
    # g.move(5, "user")
    # g.move(2, "ai")
    # g.move(1, "user")
    # g.move(0, "ai")
    # g.move(3, "user")
    # g.move(2, "ai")
    # g.move(6, "user")
    # g.move(6, "ai")
    # g.move(6, "user")
    # g.move(4, "ai")
    # g.move(0, "user")


    # make defensive move
    a.determineMove(g.getBoard())


    g.printBoard()



if __name__ == "__main__":
    main()

















