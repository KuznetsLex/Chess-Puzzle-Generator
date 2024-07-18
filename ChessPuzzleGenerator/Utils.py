
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


def coordsToSquareConverter(coords):
    square = ""
    match coords[0]:
        case 0: square += "a"
        case 1: square += "b"
        case 2: square += "c"
        case 3: square += "d"
        case 4: square += "e"
        case 5: square += "f"
        case 6: square += "g"
        case 7: square += "h"
    square += 8 - coords[1]
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


def getMovesToTarget(placement, square):
    #дописать проверку на шах и ход конем
    moves = []
    figure = getPieceBySquare(placement, square)
    board = piecePlacementToBoard(placement)
    figure_coords = squareToCoordsConverter(square)
    match figure.lowercase():
        case 'r':
            for row in range(figure_coords[0] + 1, 8):
                if board[row][figure_coords[1]] == '-':
                    moves.append(square + coordsToSquareConverter((row, figure_coords[1])))
                else:
                    break
            for row in range(figure_coords[0] - 1, 0, -1):
                if board[row][figure_coords[1]] == '-':
                    moves.append(square + coordsToSquareConverter((row, figure_coords[1])))
                else:
                    break
            for col in range(figure_coords[1] + 1, 8):
                if board[figure_coords[0]][col] == '-':
                    moves.append(square + coordsToSquareConverter((figure_coords[0], col)))
                else:
                    break
            for col in range(figure_coords[1] - 1, 0, -1):
                if board[figure_coords[0]][col] == '-':
                    moves.append(square + coordsToSquareConverter((figure_coords[0], col)))
                else:
                    break
        case 'b':
            col = figure_coords[1] + 1
            for row in range(figure_coords[0] + 1, 8):
                if board[row][col] == '-':
                    moves.append(square + coordsToSquareConverter((row, col)))
                    col += 1
                else:
                    break
            col = figure_coords[1] - 1
            for row in range(figure_coords[0] - 1, 0, -1):
                if board[row][col] == '-':
                    moves.append(square + coordsToSquareConverter((row, col)))
                    col -= 1
                else:
                    break
            col = figure_coords[1] - 1
            for row in range(figure_coords[0] + 1, 8):
                if board[row][col] == '-':
                    moves.append(square + coordsToSquareConverter((row, col)))
                    col -= 1
                else:
                    break
            col = figure_coords[1] + 1
            for row in range(figure_coords[0] - 1, 0, -1):
                if board[row][col] == '-':
                    moves.append(square + coordsToSquareConverter((row, col)))
                    col += 1
                else:
                    break
        case 'q':
            for row in range(figure_coords[0] + 1, 8):
                if board[row][figure_coords[1]] == '-':
                    moves.append(square + coordsToSquareConverter((row, figure_coords[1])))
                else:
                    break
            for row in range(figure_coords[0] - 1, 0, -1):
                if board[row][figure_coords[1]] == '-':
                    moves.append(square + coordsToSquareConverter((row, figure_coords[1])))
                else:
                    break
            for col in range(figure_coords[1] + 1, 8):
                if board[figure_coords[0]][col] == '-':
                    moves.append(square + coordsToSquareConverter((figure_coords[0], col)))
                else:
                    break
            for col in range(figure_coords[1] - 1, 0, -1):
                if board[figure_coords[0]][col] == '-':
                    moves.append(square + coordsToSquareConverter((figure_coords[0], col)))
                else:
                    break
            col = figure_coords[1] + 1
            for row in range(figure_coords[0] + 1, 8):
                if board[row][col] == '-':
                    moves.append(square + coordsToSquareConverter((row, col)))
                    col += 1
                else:
                    break
            col = figure_coords[1] - 1
            for row in range(figure_coords[0] - 1, 0, -1):
                if board[row][col] == '-':
                    moves.append(square + coordsToSquareConverter((row, col)))
                    col -= 1
                else:
                    break
            col = figure_coords[1] - 1
            for row in range(figure_coords[0] + 1, 8):
                if board[row][col] == '-':
                    moves.append(square + coordsToSquareConverter((row, col)))
                    col -= 1
                else:
                    break
            col = figure_coords[1] + 1
            for row in range(figure_coords[0] - 1, 0, -1):
                if board[row][col] == '-':
                    moves.append(square + coordsToSquareConverter((row, col)))
                    col += 1
                else:
                    break
    return moves

