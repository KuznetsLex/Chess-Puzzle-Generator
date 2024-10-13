import Utils
import random

def generate(puzzleOrig):
    origId = puzzleOrig[0]
    origFen = puzzleOrig[1]
    origMoveSet = puzzleOrig[2]
    origPlacement = origFen.split()[0]
    moveSet = origMoveSet
    placement = origPlacement
    savedPlacement = placement
    origMoveSet = origMoveSet.split()
    moveSet = moveSet.split()
    enemyKing = 'k' if origFen.split()[1] == 'b' else 'K'
    enemyKingColor = 'b' if enemyKing == 'k' else 'w'
    playerKingColor = 'w' if enemyKing == 'b' else 'b'

    # генерация первого хода игрока
    humanPoses1 = Utils.getMovesToTarget(placement, moveSet[1][0:2], moveSet[1][2:4])
    for move in humanPoses1[:]:
        savedPlacement1 = savedPlacement
        savedPlacement1 = Utils.shiftPiece(savedPlacement1, origMoveSet[1][0:2], move[0:2])
        if Utils.isKingChecked(savedPlacement1, playerKingColor):
            humanPoses1.remove(move)
            continue
        savedPlacement1 = Utils.makeMove(savedPlacement1, moveSet[0])
        if Utils.isKingChecked(savedPlacement1, enemyKingColor):
            humanPoses1.remove(move)
            continue

    humanPose1 = random.choice(humanPoses1)
    moveSet[1] = humanPose1
    placement = Utils.shiftPiece(placement, origMoveSet[1][0:2], moveSet[1][0:2])

    possiblePieces1 = Utils.getPossiblePieces(placement, moveSet[1][0:2])
    # print(possiblePieces1)
    for piece in possiblePieces1[:]:
        savedPlacement1 = savedPlacement
        savedPlacement1 = Utils.shiftPiece(savedPlacement1, origMoveSet[1][0:2], moveSet[1][0:2])
        savedPlacement1 = Utils.spawnPiece(savedPlacement1, moveSet[1][0:2], piece)
        savedPlacement1 = Utils.makeMove(savedPlacement1, moveSet[0])
        if Utils.isKingChecked(savedPlacement1, enemyKingColor):
            possiblePieces1.remove(piece)
            continue
    humanPiece1 = random.choice(possiblePieces1)
    placement = Utils.spawnPiece(placement, moveSet[1][0:2], humanPiece1)

    # генерация второго хода игрока
    if origMoveSet[1][2:4] != origMoveSet[3][0:2]:
        humanPoses2 = Utils.getMovesToTarget(placement, moveSet[3][0:2], moveSet[3][2:4])
        # print(humanPoses2)
        # if Utils.getPieceBySquare(placement, moveSet[2][0:2]) == enemyKing:
        for move in humanPoses2[:]:
            savedPlacement2 = savedPlacement
            savedPlacement2 = Utils.shiftPiece(savedPlacement2, origMoveSet[1][0:2], moveSet[1][0:2])
            savedPlacement2 = Utils.shiftPiece(savedPlacement2, origMoveSet[3][0:2], move[0:2])
            if move[0:2] == moveSet[0][2:4] or move[0:2] == moveSet[2][2:4]:
                humanPoses2.remove(move)
                continue
            if Utils.isKingChecked(savedPlacement2, playerKingColor):
                humanPoses2.remove(move)
                continue
            savedPlacement2 = Utils.makeMove(savedPlacement2, moveSet[0])
            if Utils.isKingChecked(savedPlacement2, enemyKingColor):
                humanPoses2.remove(move)
                continue
            Utils.makeMove(savedPlacement2, moveSet[1])
            if Utils.isKingChecked(savedPlacement2, playerKingColor):
                humanPoses2.remove(move)
                continue
            Utils.makeMove(savedPlacement2, move)
            if Utils.isKingChecked(savedPlacement2, enemyKingColor):
                humanPoses2.remove(move)
                continue
        humanPose2 = random.choice(humanPoses2)
        moveSet[3] = humanPose2
        placement = Utils.shiftPiece(placement, origMoveSet[3][0:2], moveSet[3][0:2])

    moveSet = " ".join(moveSet)
    id = origId
    newPuzzle = [id, placement + " " + origFen.split()[1], moveSet]
    return newPuzzle

def main():
    puzzleOrig = ['ZI07y', 'Q7/3qppkp/3p1np1/2pP4/3nP2P/1rN1B1P1/4BPK1/8 b - - 2 27', 'b3c3 e3h6 g7h6 a8f8']
    generate(puzzleOrig)


if __name__ == "__main__":
    main()
