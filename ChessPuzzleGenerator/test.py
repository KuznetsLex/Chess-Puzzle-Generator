from ChessPuzzleGenerator import Utils


def main():
    puzzleOrig = ['ZI07y', 'Q7/3qppkp/3p1np1/2pP4/3nP2P/1rN1B1P1/4BPK1/8 b - - 2 27', 'b3c3 e3h6 g7h6 a8f8']
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
    humanPoses1 = Utils.getMovesToTarget(placement, moveSet[1][0:2], moveSet[1][2:4])

    # validHumanPoses1 = []

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

    print(humanPoses1)

    # placement = "8/8/8/8/8/8/2N5/8"
    # print(Utils.getMovesToTarget(placement, 'c2', 'a1'))




if __name__ == "__main__":
    main()
