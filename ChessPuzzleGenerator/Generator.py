from ChessPuzzleGenerator import Utils


def generate(puzzleOrig):
    # origId = puzzleOrig[0]
    origFen = puzzleOrig[1]
    origMoveSet = puzzleOrig[2]
    origPiecePlacement = origFen.split()[0]

    newPuzzle = []
    firstBotMove = origMoveSet[0:5]
    placementAfter1 = Utils.makeMove(origPiecePlacement, firstBotMove)

    print(origPiecePlacement)
    print(firstBotMove)
    print(placementAfter1)
    return newPuzzle


def main():
    puzzleOrig = ["WTZrK", "2br1r2/p4p2/5b1k/1p2qP2/2ppPR1p/P2P1B2/1PPQ3P/R6K b - - 0 31", "f8g8 f4h4 h6g7 d2h6"]
    generate(puzzleOrig)


if __name__ == "__main__":
    main()
