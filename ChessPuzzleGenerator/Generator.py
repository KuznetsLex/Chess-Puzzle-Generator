from Utils import Utils

class Generator:
    def __int__(self, puzzleOrig):
        self.puzzleOrig = puzzleOrig

    def makeMove(self, placement, move):
        # fen = fen.split(" ")
        # fenBoard = fen[0].split("/")

        start_coord = Utils.squareCoordsCoverter((move[0], move[1]))
        finish_coord = Utils.squareCoordsCoverter((move[2], move[3]))

        # board = Utils.fenToBoard(fenBoard)
        board = Utils.piecePlacementToBoard(placement)
        figure = board[start_coord[0]][start_coord[1]]
        board[start_coord[0]][start_coord[1]] = "-"
        board[finish_coord[0]][finish_coord[1]] = figure
        newPlacement = Utils.boardToPiecePlacement(board)
        return newPlacement

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

    def generate(self, puzzleOrig):
        origId = puzzleOrig[0]
        origFen = puzzleOrig[1]
        origMoveSet = puzzleOrig[2]
        origPiecePlacement = origFen.split()[0]

        newPuzzle = []
        firstBotMove = origMoveSet[0:5]
        placementAfter1 = self.makeMove(origPiecePlacement, firstBotMove)
        return newPuzzle

def main():
    puzzleOrig = ["WTZrK", "2br1r2/p4p2/5b1k/1p2qP2/2ppPR1p/P2P1B2/1PPQ3P/R6K b - - 0 31", "f8g8 f4h4 h6g7 d2h6"]
    gen = Generator()
    gen.generate(puzzleOrig)

if __name__ == "__main__":
    main()


