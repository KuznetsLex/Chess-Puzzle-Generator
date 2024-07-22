from ChessPuzzleGenerator import Utils


def main():
    puzzle = ['hujLD', 'r2qr1k1/pb1n2pp/1p1BpnB1/3p2N1/2Pp3Q/4P3/PP3PPP/R4RK1 b', 'h7h6 g6h7 f6h7 h4h7']
    placement = puzzle[1].split()[0]
    moves = puzzle[2].split()
    for move in moves:
        print(Utils.isPieceOnTheWay(placement, move))
        placement = Utils.makeMove(placement, move)




if __name__ == "__main__":
    main()
