import Utils
import random

def generate(puzzleOrig):
    origId = puzzleOrig[0]
    origFen = puzzleOrig[1]
    origMoveSet = puzzleOrig[2]
    origPlacement = origFen.split()[0]
    moveSet = origMoveSet
    placement = origPlacement
    origMoveSet = origMoveSet.split()
    moveSet = moveSet.split()

    humanMoves1 = Utils.getMovesToTarget(placement, origMoveSet[1][0:2], origMoveSet[1][2:4])
    humanMove1 = random.choice(humanMoves1)
    moveSet[1] = humanMove1
    placement = Utils.shiftPiece(placement, origMoveSet[1][0:2], moveSet[1][0:2])

    possiblePieces1 = Utils.getPossiblePieces(placement, moveSet[1][0:2])
    # print(possiblePieces1)
    humanPiece1 = random.choice(possiblePieces1)
    placement = Utils.spawnPiece(placement, moveSet[1][0:2], humanPiece1)

    moveSet = " ".join(moveSet)
    id = origId
    newPuzzle = [id, placement + " " + origFen.split()[1], moveSet]
    return newPuzzle


def main():
    puzzleOrig = ["WTZrK", "2br1r2/p4p2/5b1k/1p2qP2/2ppPR1p/P2P1B2/1PPQ3P/R6K b - - 0 31", "f8g8 f4h4 h6g7 d2h6"]
    generate(puzzleOrig)


if __name__ == "__main__":
    main()
