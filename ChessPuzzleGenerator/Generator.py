import copy

import Utils
import random
import pandas as pd
from PuzzleManager import Puzzle

def generate(puzzleOrig):
    df = pd.DataFrame(columns=['PuzzleId', 'FEN', 'Moves', 'Level'])

    origId = puzzleOrig[0]
    origFen = puzzleOrig[1]
    origMoveSet = puzzleOrig[2].split()
    origLevel = puzzleOrig[3]
    origPlacement = origFen.split()[0]
    moveSet = list(origMoveSet)
    placement = str(origPlacement)
    savedPlacement = str(placement)
    # origMoveSet = origMoveSet
    # moveSet = moveSet
    enemyKing = 'k' if origFen.split()[1] == 'b' else 'K'
    enemyKingColor = 'b' if enemyKing == 'k' else 'w'
    playerKingColor = 'w' if enemyKing == 'b' else 'b'
    indexPos1 = 0
    indexPiece1 = 0
    indexPos2 = 0

    # генерация первого хода игрока
    humanPoses1 = Utils.getMovesToTarget(placement, moveSet[1][0:2], moveSet[1][2:4])
    for move in humanPoses1[:]:
        moveSet = list(origMoveSet)
        placement = str(origPlacement)
        savedPlacement1 = str(savedPlacement)
        savedPlacement1 = Utils.shiftPiece(savedPlacement1, origMoveSet[1][0:2], move[0:2])
        if move[0:2] == moveSet[0][2:4] or move[0:2] == moveSet[2][2:4]:
            humanPoses1.remove(move)
            continue
        if Utils.isKingChecked(savedPlacement1, playerKingColor):
            humanPoses1.remove(move)
            continue
        savedPlacement1 = Utils.makeMove(savedPlacement1, moveSet[0])
        if Utils.isKingChecked(savedPlacement1, enemyKingColor):
            humanPoses1.remove(move)
            continue
    for humanPose1 in humanPoses1:
        indexPos1 += 1
        moveSet[1] = humanPose1
        placement = str(origPlacement)
        placement = Utils.shiftPiece(placement, origMoveSet[1][0:2], moveSet[1][0:2])
        possiblePieces1 = Utils.getPossiblePieces(placement, moveSet[1][0:2])
        for piece in possiblePieces1[:]:
            savedPlacement1 = str(savedPlacement)
            savedPlacement1 = Utils.shiftPiece(savedPlacement1, origMoveSet[1][0:2], moveSet[1][0:2])
            savedPlacement1 = Utils.spawnPiece(savedPlacement1, moveSet[1][0:2], piece)
            savedPlacement1 = Utils.makeMove(savedPlacement1, moveSet[0])
            if Utils.isKingChecked(savedPlacement1, enemyKingColor):
                possiblePieces1.remove(piece)
                continue
        for humanPiece1 in possiblePieces1:
            indexPiece1 += 1
            placement = Utils.spawnPiece(placement, moveSet[1][0:2], humanPiece1)

        # генерация второго хода игрока
        if origMoveSet[1][2:4] != origMoveSet[3][0:2]:
            humanPoses2 = Utils.getMovesToTarget(placement, moveSet[3][0:2], moveSet[3][2:4])
            # print(humanPoses2)
            # if Utils.getPieceBySquare(placement, moveSet[2][0:2]) == enemyKing:
            for move in humanPoses2[:]:
                savedPlacement2 = str(savedPlacement)
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
            for humanPose2 in humanPoses2:
                indexPos2 += 1
                moveSet[3] = humanPose2
                placement = Utils.shiftPiece(placement, origMoveSet[3][0:2], moveSet[3][0:2])
                correctFlag = True
                for move in moveSet:
                    savedPlacement = str(placement)
                    if Utils.isPieceOnTheWay(savedPlacement, move) == True:
                        correctFlag = False
                    placement = Utils.makeMove(savedPlacement, move)
                newMoveSet = " ".join(moveSet)
                id = str(origId) + '_' + str(indexPos1) + '_' + str(indexPiece1) + '_' + str(indexPos2)
                newPuzzle = [id, placement + " " + origFen.split()[1], newMoveSet, origLevel]
                if correctFlag:
                    df = pd.concat([df, pd.DataFrame([newPuzzle])], ignore_index=True)
                    print(newPuzzle)
    return df


def main():
    df_MateIn2_Generated = pd.DataFrame(columns=['PuzzleId', 'FEN', 'Moves', 'Level'])
    for i in range(1):
        puzzle_manager = Puzzle(4)
        puzzle = puzzle_manager.parse()
        df_MateIn2_Generated = pd.concat([df_MateIn2_Generated, generate(puzzle)])
    df_MateIn2_Generated.to_csv('mateIn2Generated')
if __name__ == "__main__":
    main()
