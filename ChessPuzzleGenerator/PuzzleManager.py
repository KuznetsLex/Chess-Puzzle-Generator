import pandas as pd

class Puzzle:
    df_mateIn2 = pd.read_csv('mateIn2WithLevel.csv', index_col=0)

    def __init__(self, n):
        self.n = n
        
    def parse(self):
        puzzle = self.df_mateIn2[self.df_mateIn2['Level'] == self.n].sample().iloc[0]
        puzzle = [puzzle['PuzzleId'], puzzle['FEN'], puzzle['Moves'], puzzle['Level']]
        return puzzle
