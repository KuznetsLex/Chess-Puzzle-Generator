class Utils:
    @staticmethod
    def squareCoordsCoverter(coords):
        row = 8 - int(coords[1])
        x = coords[0]
        match x:
            case 'a': col = 0
            case 'b': col = 1
            case 'c': col = 2
            case 'd': col = 3
            case 'e': col = 4
            case 'f': col = 5
            case 'g': col = 6
            case 'h': col = 7
        return (row,col)

    @staticmethod
    def fenToBoard(fen):
        listFen = fen.split();
        boardFen = listFen[0].split('/')
        board = [[0 for _ in range(8)] for _ in range(8)]
        i = 0
        for row in boardFen:
            j = 0
            for x in row:
                if x == 'p':
                    board[i][j] = "bp"
                elif x == 'P':
                    board[i][j] = "wp"
                elif x.isdigit():
                    j -= 1
                    for k in range(int(x)):
                        j += 1
                        board[i][j] = "--"
                elif x.islower():
                    board[i][j] = 'b'+x.upper()
                elif x.isupper():
                    board[i][j] = 'w' + x
                j += 1
            i += 1
        return board