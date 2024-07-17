from Utils import Utils

class Generator:
    def __int__(self, puzzleOrig):
        self.puzzleOrig = puzzleOrig

    def generate(self, puzzleOrig):
        origId = puzzleOrig[0]
        origFen = puzzleOrig[1]
        origMoveSet = puzzleOrig[2]


    def makeMove(self, fen, move):
        fen = fen.split(" ")
        fenBoard = fen[0].split("/")

        start_coord = Utils.squareCoordsCoverter((move[0], move[1]))
        finish_coord = Utils.squareCoordsCoverter((move[2], move[3]))

        board = Utils.fenToBoard(fenBoard)

        figure = board[start_coord[0]][start_coord[1]]
        board[start_coord[0]][start_coord[1]] = "-"
        board[finish_coord[0]][finish_coord[1]] = figure

        fen[0] = Utils.boardToFen(board)
        fen[-1] = str(int(fen[-1]) + 1)
        newFen = fen.join()
        return newFen

    def getPieceByCoords(self, fen, coords):
        fen = fen.split()
        fenBoard = fen[0].split('/')
        coords = Utils.squareCoordsCoverter(coords)
        pieceRow = fenBoard[coords[0]]
        pieceColIndex = coords[1]
        colIndex = 0

        for item in pieceRow:
            if colIndex == pieceColIndex:
                return item
            if item.isdigit():
                colIndex+=int(item)
            else:
                colIndex+=1






