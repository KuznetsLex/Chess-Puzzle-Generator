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
    moveSet = " ".join(moveSet)
    id = origId
    newPuzzle = [id, placement + " " + origFen.split()[1], moveSet]
    return newPuzzle


def main():
    puzzleOrig = ["WTZrK", "r3r1k1/p4ppp/2p2n2/1p6/3P1qb1/2NQR3/PPB2PP1/R1B3K1 w - - 5 18", "f8g8 f4h4 h6g7 d2h6"]
    generate(puzzleOrig)


if __name__ == "__main__":
    main()
