class Utils:
    @staticmethod
    def squareCoordsCoverter(coords):
        row = 8 - int(coords[1])
        x = coords[0]
        match x:
            case 'a': col = 0
            case 'b': col = 1
            case 'c': col = 2
            case 'd': col = 3
            case 'e': col = 4
            case 'f': col = 5
            case 'g': col = 6
            case 'h': col = 7
        return (row,col)

