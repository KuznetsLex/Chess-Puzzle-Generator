from ChessPuzzleGenerator import Utils


def main():
    placement = "8/8/8/8/8/8/2N5/8"
    print(Utils.getMovesToTarget(placement, 'c2', 'a1'))




if __name__ == "__main__":
    main()
