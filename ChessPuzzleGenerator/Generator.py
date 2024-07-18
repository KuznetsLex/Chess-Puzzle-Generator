from ChessPuzzleGenerator import Utils
import random


def getMovesWithDifferStartPos(placement, moves):
    return ['h3h4']


def generate(puzzleOrig):
    origId = puzzleOrig[0]
    origFen = puzzleOrig[1]
    origMoveSet = puzzleOrig[2]
    origPlacement = origFen.split()[0]
    moveSet = origMoveSet
    placement = origPlacement
    origMoveSet = origMoveSet.split()
    moveSet = moveSet.split()

    # humanMoves1 = getMovesWithDifferStartPos(placement, origMoveSet[1])
    humanMoves1 = Utils.getMovesToTarget(placement, origMoveSet[1][0:2], origMoveSet[1][2:4])
    print(humanMoves1)
    humanMove1 = random.choice(humanMoves1)
    moveSet[1] = humanMove1
    placement = Utils.shiftPiece(placement, origMoveSet[1][0:2], moveSet[1][0:2])
    moveSet = " ".join(moveSet)
    id = origId + '1'
    newPuzzle = [id, placement + " " + origFen.split()[1], moveSet]
    print(newPuzzle)
    return newPuzzle


def main():
    puzzleOrig = ["WTZrK", "2br1r2/p4p2/5b1k/1p2qP2/2ppPR1p/P2P1B2/1PPQ3P/R6K b - - 0 31", "f8g8 f4h4 h6g7 d2h6"]
    generate(puzzleOrig)


if __name__ == "__main__":
    main()
