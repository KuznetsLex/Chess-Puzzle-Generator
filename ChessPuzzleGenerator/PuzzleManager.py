import pandas as pd
import random as rnd

class Puzzle:
    df_mateIn2 = pd.read_csv('mateIn2.csv', index_col=0)
    ranges = [None] * 9
    ranges[1] = [0, df_mateIn2.loc[df_mateIn2['Rating'] <= 499].index[-1]]
    ranges[2] = [df_mateIn2.loc[df_mateIn2['Rating'] >= 500].index[0], df_mateIn2.loc[df_mateIn2['Rating'] <= 799].index[-1]]
    ranges[3] = [df_mateIn2.loc[df_mateIn2['Rating'] >= 800].index[0], df_mateIn2.loc[df_mateIn2['Rating'] <= 999].index[-1]]
    ranges[4] = [df_mateIn2.loc[df_mateIn2['Rating'] >= 1000].index[0], df_mateIn2.loc[df_mateIn2['Rating'] <= 1399].index[-1]]
    ranges[5] = [df_mateIn2.loc[df_mateIn2['Rating'] >= 1400].index[0], df_mateIn2.loc[df_mateIn2['Rating'] <= 1599].index[-1]]
    ranges[6] = [df_mateIn2.loc[df_mateIn2['Rating'] >= 1600].index[0], df_mateIn2.loc[df_mateIn2['Rating'] <= 1799].index[-1]]
    ranges[7] = [df_mateIn2.loc[df_mateIn2['Rating'] >= 1800].index[0], df_mateIn2.loc[df_mateIn2['Rating'] <= 1999].index[-1]]
    ranges[8] = [df_mateIn2.loc[df_mateIn2['Rating'] >= 2000].index[0], df_mateIn2.loc[df_mateIn2['Rating'] <= 3500].index[-1]]

    def __init__(self, n):
        self.n = n
        
    def parse(self):
        ind = rnd.randint(self.ranges[self.n][0], self.ranges[self.n][1])
        puzzle = [self.df_mateIn2.iloc[ind]['PuzzleId'], self.df_mateIn2.iloc[ind]['FEN'],
                  self.df_mateIn2.iloc[ind]['Moves']]
        return puzzle
