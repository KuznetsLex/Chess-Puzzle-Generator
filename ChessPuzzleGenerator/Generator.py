from Utils import Utils

class Generator:
    def __int__(self, puzzleOrig):
        self.puzzleOrig = puzzleOrig

    def generate(self, puzzleOrig):
        origId = puzzleOrig[0]
        origFen = puzzleOrig[1]
        origMoveSet = puzzleOrig[2]


    def makeMove(self, fen, move):
        newFen = ""
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





