import threat, ai, game, position

def main():

    th = threat.Threat("VERTICAL")
    a = ai.AI()
    g = game.ConnectFourGame()
    pos = position.Position("null", 3, 2)

    print ""
    print g.getBoard()

    for x in range(0, 7):
        p = position.Position("user", x, 0)
        board = g.getBoard()
        board[x].append(p)

    g.printBoard()



if __name__ == "__main__":
    main()