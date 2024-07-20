
def squareToCoordsConverter(square):
    row = 8 - int(square[1])
    x = square[0]
    match x:
        case 'a': col = 0
        case 'b': col = 1
        case 'c': col = 2
        case 'd': col = 3
        case 'e': col = 4
        case 'f': col = 5
        case 'g': col = 6
        case 'h': col = 7
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


def isKingChecked(placement):
    pass

def getMovesToTarget(placement, startSquare, targetSquare):
    # TODO дописать проверку на шах и ход конем
    startSquares = []
    placementSaved = placement
    placement = makeMove(placement, startSquare+targetSquare)
    figure = getPieceBySquare(placement, targetSquare)
    board = piecePlacementToBoard(placement)
    figure_coords = squareToCoordsConverter(targetSquare)
    match figure.lower():
        case 'r':
            for row in range(figure_coords[0] + 1, 8):
                if board[row][figure_coords[1]] == '-':
                    startSquares.append(coordsToSquareConverter((row, figure_coords[1])))
                else:
                    break
            for row in range(figure_coords[0] - 1, 0, -1):
                if board[row][figure_coords[1]] == '-':
                    startSquares.append(coordsToSquareConverter((row, figure_coords[1])))
                else:
                    break
            for col in range(figure_coords[1] + 1, 8):
                if board[figure_coords[0]][col] == '-':
                    startSquares.append(coordsToSquareConverter((figure_coords[0], col)))
                else:
                    break
            for col in range(figure_coords[1] - 1, 0, -1):
                if board[figure_coords[0]][col] == '-':
                    startSquares.append(coordsToSquareConverter((figure_coords[0], col)))
                else:
                    break
        case 'b':
            col = figure_coords[1] + 1
            for row in range(figure_coords[0] + 1, 8):
                if board[row][col] == '-' and col < 8:
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col += 1
                else:
                    break
            col = figure_coords[1] - 1
            for row in range(figure_coords[0] - 1, 0, -1):
                if board[row][col] == '-' and col >= 0:
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col -= 1
                else:
                    break
            col = figure_coords[1] - 1
            for row in range(figure_coords[0] + 1, 8):
                if board[row][col] == '-' and col >= 0:
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col -= 1
                else:
                    break
            col = figure_coords[1] + 1
            for row in range(figure_coords[0] - 1, 0, -1):
                if board[row][col] == '-' and col < 8:
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col += 1
                else:
                    break
        case 'q':
            for row in range(figure_coords[0] + 1, 8):
                if board[row][figure_coords[1]] == '-':
                    startSquares.append(coordsToSquareConverter((row, figure_coords[1])))
                else:
                    break
            for row in range(figure_coords[0] - 1, 0, -1):
                if board[row][figure_coords[1]] == '-':
                    startSquares.append(coordsToSquareConverter((row, figure_coords[1])))
                else:
                    break
            for col in range(figure_coords[1] + 1, 8):
                if board[figure_coords[0]][col] == '-':
                    startSquares.append(coordsToSquareConverter((figure_coords[0], col)))
                else:
                    break
            for col in range(figure_coords[1] - 1, 0, -1):
                if board[figure_coords[0]][col] == '-':
                    startSquares.append(coordsToSquareConverter((figure_coords[0], col)))
                else:
                    break
            col = figure_coords[1] + 1
            for row in range(figure_coords[0] + 1, 8):
                if board[row][col] == '-' and col < 8:
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col += 1
                else:
                    break
            col = figure_coords[1] - 1
            for row in range(figure_coords[0] - 1, 0, -1):
                if board[row][col] == '-' and col >= 0:
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col -= 1
                else:
                    break
            col = figure_coords[1] - 1
            for row in range(figure_coords[0] + 1, 8):
                if board[row][col] == '-' and col >= 0:
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col -= 1
                else:
                    break
            col = figure_coords[1] + 1
            for row in range(figure_coords[0] - 1, 0, -1):
                if board[row][col] == '-' and col < 8:
                    startSquares.append(coordsToSquareConverter((row, col)))
                    col += 1
                else:
                    break
    for i in range(len(startSquares)):
        placement = placementSaved
        placement = shiftPiece(placement, startSquares[i], targetSquare)
        if isKingChecked(placement):
            startSquares.pop(i)

    moves = []
    for i in range(len(startSquares)):
        moves.append(startSquares[i] + targetSquare)
    return moves

