
def squareToCoordsConverter(square):
    row = 8 - int(square[1])
    x = square[0]
    col = ord(x) - ord('a')
    return row, col


num_to_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

def coordsToSquareConverter(coords):
    square = num_to_letters[coords[1]]
    square += str(8 - coords[0])
    return square


# TODO рефактор
def piecePlacementToBoard(placement):
    listPlacement = placement.split('/')
    board = [[0 for _ in range(8)] for _ in range(8)]
    i = 0
    for row in listPlacement:
        j = 0
        for x in row:
            if x.isdigit():
                j -= 1
                for k in range(int(x)):
                    j += 1
                    board[i][j] = "-"
            else:
                board[i][j] = x
            j += 1
        i += 1
    return board


def boardToPiecePlacement(board):
    placement = ""
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "-":
                count += 1
            elif count != 0:
                placement += str(count)
                count = 0
                placement += board[i][j]
            else:
                placement += board[i][j]
        if count != 0:
            placement += str(count)
        count = 0
        placement += "/"
    return placement[:-1]


def getPieceBySquare(placement, square):
    listPlacement = placement.split('/')
    square = squareToCoordsConverter(square)
    pieceRow = listPlacement[square[0]]
    pieceColIndex = square[1]
    colIndex = 0

    for item in pieceRow:
        if colIndex == pieceColIndex:
            return item
        if item.isdigit():
            colIndex += int(item)
        else:
            colIndex += 1


def makeMove(placement, move):
    start_coord = squareToCoordsConverter((move[0], move[1]))
    finish_coord = squareToCoordsConverter((move[2], move[3]))

    board = piecePlacementToBoard(placement)
    figure = board[start_coord[0]][start_coord[1]]
    board[start_coord[0]][start_coord[1]] = "-"
    board[finish_coord[0]][finish_coord[1]] = figure
    newPlacement = boardToPiecePlacement(board)
    return newPlacement


def shiftPiece(placement, startSquare, finishSquare):
    return makeMove(placement, startSquare+finishSquare)


def revertMove(placement, move):
    move = move[2:4] + move[0:2]
    return makeMove(placement, move)


def getWhiteKingLocation(board):
    for i in range (8):
        for j in range(8):
            if board[i][j] == 'K':
                return (i,j)


def getBlackKingLocation(board):
    for i in range (8):
        for j in range(8):
            if board[i][j] == 'k':
                return (i,j)


# TODO должен получать square на вход. Не row,col
def squareUnderAttack(placement, row, col):
    board = piecePlacementToBoard(placement)
    if board[row][col].islower():
        # проверяем на атаку пешкой слева
        if row < 7 and col > 1 and board[row + 1][col - 1] == 'P':
            return True
        # проверяем на атаку пешкой справа
        if row < 7 and col < 7 and board[row + 1][col + 1] == 'P':
            return True
        # проверяем на атаку по вертикали и горизонтали
        for row_ in range(row + 1, 8):
            if board[row_][col] == 'R' or board[row_][col] == 'Q':
                return True
            elif board[row_][col] != '-':
                break
        for row_ in range(row - 1, -1, -1):
            if board[row_][col] == 'R' or board[row_][col] == 'Q':
                return True
            elif board[row_][col] != '-':
                break
        for col_ in range(col + 1, 8):
            if board[row][col_] == 'R' or board[row][col_] == 'Q':
                return True
            elif board[row][col_] != '-':
                break
        for col_ in range(col - 1, -1, -1):
            if board[row][col_] == 'R' or board[row][col_] == 'Q':
                return True
            elif board[row][col_] != '-':
                break
        # проверяем на атаку по диагоналям
        col_ = col + 1
        for row_ in range(row + 1, 8):
            if col_ < 8 and (board[row_][col_] == 'B' or board[row_][col_] == 'Q'):
                return True
            elif col_ < 8 and board[row_][col_] != '-':
                break
            col_ += 1
        col_ = col - 1
        for row_ in range(row - 1, -1, -1):
            if col_ >= 0 and (board[row_][col_] == 'B' or board[row_][col_] == 'Q'):
                return True
            elif col_ >= 0 and board[row_][col_] != '-':
                break
            col_ -= 1
        col_ = col - 1
        for row_ in range(row + 1, 8):
            if col_ >= 0 and (board[row_][col_] == 'B' or board[row_][col_] == 'Q'):
                return True
            elif col_ >= 0 and board[row_][col_] != '-':
                break
            col_ -= 1
        col_ = col + 1
        for row_ in range(row - 1, -1, -1):
            if col_ < 8 and (board[row_][col_] == 'B' or board[row_][col_] == 'Q'):
                return True
            elif col_ < 8 and board[row_][col_] != '-':
                break
            col_ += 1
        # проверяем на атаку конём
        if row <= 6 and col <= 5 and board[row + 1][col + 2] == 'N':
            return True
        if row <= 6 and col >= 2 and board[row + 1][col - 2] == 'N':
            return True
        if row <= 5 and col >= 1 and board[row + 2][col - 1] == 'N':
            return True
        if row <= 5 and col <= 6 and board[row + 2][col + 1] == 'N':
            return True
        if row >= 2 and col <= 6 and board[row - 2][col + 1] == 'N':
            return True
        if row >= 2 and col >= 1 and board[row - 2][col - 1] == 'N':
            return True
        if row >= 1 and col >= 2 and board[row - 1][col - 2] == 'N':
            return True
        if row >= 1 and col <= 5 and board[row - 1][col + 2] == 'N':
            return True
        return False
    if board[row][col].isupper():
        # проверяем на атаку пешкой слева
        if row > 1 and col > 1 and board[row - 1][col - 1] == 'p':
            return True
        # проверяем на атаку пешкой справа
        if row > 1 and col < 7 and board[row - 1][col + 1] == 'p':
            return True
        # проверяем на атаку по вертикали и горизонтали
        for row_ in range(row + 1, 8):
            if board[row_][col] == 'r' or board[row_][col] == 'q':
                return True
            elif board[row_][col] != '-':
                break
        for row_ in range(row - 1, -1, -1):
            if board[row_][col] == 'r' or board[row_][col] == 'q':
                return True
            elif board[row_][col] != '-':
                break
        for col_ in range(col + 1, 8):
            if board[row][col_] == 'r' or board[row][col_] == 'q':
                return True
            elif board[row][col_] != '-':
                break
        for col_ in range(col - 1, -1, -1):
            if board[row][col_] == 'r' or board[row][col_] == 'q':
                return True
            elif board[row][col_] != '-':
                break
        # проверяем на атаку по диагоналям
        col_ = col + 1
        for row_ in range(row + 1, 8):
            if col_ < 8 and (board[row_][col_] == 'b' or board[row_][col_] == 'q'):
                return True
            elif col_ < 8 and board[row_][col_] != '-':
                break
            col_ += 1
        col_ = col - 1
        for row_ in range(row - 1, -1, -1):
            if col_ >= 0 and (board[row_][col_] == 'b' or board[row_][col_] == 'q'):
                return True
            elif col_ >= 0 and board[row_][col_] != '-':
                break
            col_ -= 1
        col_ = col - 1
        for row_ in range(row + 1, 8):
            if col_ >= 0 and (board[row_][col_] == 'b' or board[row_][col_] == 'q'):
                return True
            elif col_ >= 0 and board[row_][col_] != '-':
                break
            col_ -= 1
        col_ = col + 1
        for row_ in range(row - 1, -1, -1):
            if col_ < 8 and (board[row_][col_] == 'b' or board[row_][col_] == 'q'):
                return True
            elif col_ < 8 and board[row_][col_] != '-':
                break
            col_ += 1
        # проверяем на атаку конём
        if row <= 6 and col <= 5 and board[row + 1][col + 2] == 'n':
            return True
        if row <= 6 and col >= 2 and board[row + 1][col - 2] == 'n':
            return True
        if row <= 5 and col >= 1 and board[row + 2][col - 1] == 'n':
            return True
        if row <= 5 and col <= 6 and board[row + 2][col + 1] == 'n':
            return True
        if row >= 2 and col <= 6 and board[row - 2][col + 1] == 'n':
            return True
        if row >= 2 and col >= 1 and board[row - 2][col - 1] == 'n':
            return True
        if row >= 1 and col >= 2 and board[row - 1][col - 2] == 'n':
            return True
        if row >= 1 and col <= 5 and board[row - 1][col + 2] == 'n':
            return True
        return False


def isKingChecked(placement, color):
    if color == "w":
        return squareUnderAttack(placement, getWhiteKingLocation(piecePlacementToBoard(placement))[0], getWhiteKingLocation(piecePlacementToBoard(placement))[1])
    else:
        return squareUnderAttack(placement, getBlackKingLocation(piecePlacementToBoard(placement))[0], getBlackKingLocation(piecePlacementToBoard(placement))[1])


def isPieceOnTheWay(placement, move):
    board = piecePlacementToBoard(placement)
    start_coord = squareToCoordsConverter((move[0], move[1]))
    finish_coord = squareToCoordsConverter((move[2], move[3]))
    if start_coord[0] == finish_coord[0]:
        frm = start_coord[1] + 1
        to = finish_coord[1]
        if start_coord[1] > finish_coord[1]:
            frm, to = to, frm
        for i in range(frm, to):
            if board[start_coord[0]][i] != '-':
                return True
    elif start_coord[1] == finish_coord[1]:
        frm = start_coord[0] + 1
        to = finish_coord[0]
        if start_coord[0] > finish_coord[0]:
            frm, to = to, frm
        for i in range(frm, to):
            if board[i][start_coord[1]] != '-':
                return True
    elif start_coord[0] - finish_coord[0] == start_coord[1] - finish_coord[1]:
        dif = abs(start_coord[0] - finish_coord[0])
        if start_coord[0] > finish_coord[0]:
            for i in range(1, dif):
                if board[start_coord[0] - i][start_coord[1] - i] != '-':
                    return True
        else:
            for i in range(1, dif):
                if board[start_coord[0] + i][start_coord[1] + i] != '-':
                    return True
    elif start_coord[0] - finish_coord[0] == -(start_coord[1] - finish_coord[1]):
        dif = abs(start_coord[0] - finish_coord[0])
        if start_coord[0] > finish_coord[0]:
            for i in range(1, dif):
                if board[start_coord[0] - i][start_coord[1] + i] != '-':
                    return True
        else:
            for i in range(1, dif):
                if board[start_coord[0] + i][start_coord[1] - i] != '-':
                    return True
    return False






def getMovesToTarget(placement, startSquare, targetSquare):
    startSquares = []
    placementSaved = placement
    placement = makeMove(placement, startSquare+targetSquare)
    piece = getPieceBySquare(placement, targetSquare)
    board = piecePlacementToBoard(placement)
    piece_coords = squareToCoordsConverter(targetSquare)
    enemyKingColor = "w" if piece.islower() else "b"
    match piece.lower():
        case 'r':
            for row in range(piece_coords[0] + 1, 8):
                if board[row][piece_coords[1]] == '-':
                    startSquares.append(coordsToSquareConverter((row, piece_coords[1])))
                else:
                    break
            for row in range(piece_coords[0] - 1, -1, -1):
                if board[row][piece_coords[1]] == '-':
                    startSquares.append(coordsToSquareConverter((row, piece_coords[1])))
                else:
                    break
            for col in range(piece_coords[1] + 1, 8):
                if board[piece_coords[0]][col] == '-':
                    startSquares.append(coordsToSquareConverter((piece_coords[0], col)))
                else:
                    break
            for col in range(piece_coords[1] - 1, -1, -1):
                if board[piece_coords[0]][col] == '-':
                    startSquares.append(coordsToSquareConverter((piece_coords[0], col)))
                else:
                    break
        case 'b':
            col = piece_coords[1] + 1
            for row in range(piece_coords[0] + 1, 8):
                if col < 8 and board[row][col] == '-':
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col += 1
                else:
                    break
            col = piece_coords[1] - 1
            for row in range(piece_coords[0] - 1, -1, -1):
                if col >= 0 and board[row][col] == '-':
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col -= 1
                else:
                    break
            col = piece_coords[1] - 1
            for row in range(piece_coords[0] + 1, 8):
                if col >= 0 and board[row][col] == '-':
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col -= 1
                else:
                    break
            col = piece_coords[1] + 1
            for row in range(piece_coords[0] - 1, -1, -1):
                if col < 8 and board[row][col] == '-':
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col += 1
                else:
                    break
        case 'q':
            for row in range(piece_coords[0] + 1, 8):
                if board[row][piece_coords[1]] == '-':
                    startSquares.append(coordsToSquareConverter((row, piece_coords[1])))
                else:
                    break
            for row in range(piece_coords[0] - 1, -1, -1):
                if board[row][piece_coords[1]] == '-':
                    startSquares.append(coordsToSquareConverter((row, piece_coords[1])))
                else:
                    break
            for col in range(piece_coords[1] + 1, 8):
                if board[piece_coords[0]][col] == '-':
                    startSquares.append(coordsToSquareConverter((piece_coords[0], col)))
                else:
                    break
            for col in range(piece_coords[1] - 1, -1, -1):
                if board[piece_coords[0]][col] == '-':
                    startSquares.append(coordsToSquareConverter((piece_coords[0], col)))
                else:
                    break
            col = piece_coords[1] + 1
            for row in range(piece_coords[0] + 1, 8):
                if col < 8 and board[row][col] == '-':
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col += 1
                else:
                    break
            col = piece_coords[1] - 1
            for row in range(piece_coords[0] - 1, -1, -1):
                if col >= 0 and board[row][col] == '-':
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col -= 1
                else:
                    break
            col = piece_coords[1] - 1
            for row in range(piece_coords[0] + 1, 8):
                if col >= 0 and board[row][col] == '-':
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col -= 1
                else:
                    break
            col = piece_coords[1] + 1
            for row in range(piece_coords[0] - 1, -1, -1):
                if col < 8 and board[row][col] == '-':
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col += 1
                else:
                    break
        case 'p':
            startSquares.append(startSquare)
        case 'n':
            row = piece_coords[0] + 1
            col = piece_coords[1] + 2
            if row < 8 and col < 8 and board[row][col] == '-':
                startSquares.append(coordsToSquareConverter((row, col)))
            row = piece_coords[0] + 2
            col = piece_coords[1] + 1
            if row < 8 and col < 8 and board[row][col] == '-':
                startSquares.append(coordsToSquareConverter((row, col)))
            row = piece_coords[0] - 1
            col = piece_coords[1] + 2
            if row > 0 and col < 8 and board[row][col] == '-':
                startSquares.append(coordsToSquareConverter((row, col)))
            row = piece_coords[0] - 2
            col = piece_coords[1] + 1
            if row > 0 and col < 8 and board[row][col] == '-':
                startSquares.append(coordsToSquareConverter((row, col)))
            row = piece_coords[0] + 1
            col = piece_coords[1] - 2
            if row < 8 and col > 0 and board[row][col] == '-':
                startSquares.append(coordsToSquareConverter((row, col)))
            row = piece_coords[0] + 2
            col = piece_coords[1] - 1
            if row < 8 and col > 0 and board[row][col] == '-':
                startSquares.append(coordsToSquareConverter((row, col)))
            row = piece_coords[0] - 1
            col = piece_coords[1] - 2
            if row > 0 and col > 0 and board[row][col] == '-':
                startSquares.append(coordsToSquareConverter((row, col)))
            row = piece_coords[0] - 2
            col = piece_coords[1] - 1
            if row > 0 and col > 0 and board[row][col] == '-':
                startSquares.append(coordsToSquareConverter((row, col)))
    # for i in range(len(startSquares)):
    #     placement = placementSaved
    #     placement = shiftPiece(placement, startSquares[i], targetSquare)
    #     if isKingChecked(placement, enemyKingColor):
    #         startSquares.pop(i)
    #         i-=1

    # for square in startSquares:
    #     placement = placementSaved
    #     placement = shiftPiece(placement, square, targetSquare)
    #     if isKingChecked(placement, enemyKingColor):
    #         startSquares.remove(square)

    moves = []
    for i in range(len(startSquares)):
        moves.append(startSquares[i] + targetSquare)
    return moves


def getPossiblePieces(placement, square):
    piece = getPieceBySquare(placement, square)
    savedPlacement = placement
    possiblePieces = [piece]
    enemyKingColor = "w" if piece.islower() else "b"
    piece.lower()
    if piece == 'b' or piece == 'r':
        newPiece = 'q' if enemyKingColor == 'w' else 'Q'
        placement = spawnPiece(placement, square, newPiece)
        if isKingChecked(savedPlacement, enemyKingColor) and isKingChecked(placement,
                                                                           enemyKingColor) or not isKingChecked(
                savedPlacement, enemyKingColor) and not isKingChecked(placement, enemyKingColor):
            possiblePieces.append(newPiece)
    return possiblePieces


def spawnPiece(placement, square, piece):
    coords = squareToCoordsConverter(square)
    board = piecePlacementToBoard(placement)
    board[coords[0]][coords[1]] = piece
    placement = boardToPiecePlacement(board)
    return placement


def getKingLocation(placement, kingColor):
    board = piecePlacementToBoard(placement)
    king = 'k' if kingColor == 'b' else 'K'
    for i in range (8):
        for j in range(8):
            if board[i][j] == king:
                return (i,j)
