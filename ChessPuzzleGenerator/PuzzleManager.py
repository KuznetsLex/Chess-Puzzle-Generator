import pandas as pd
import random as rnd


class Puzzle:
    df_mateIn2 = pd.read_csv('mateIn2.csv', index_col=0)
    from_ind = 0
    to_ind = 0

    def __init__(self, n):
        self.n = n
        self.setRange(n)

    def setRange(self, n):
        match int(n):
            case 1:
                self.from_ind = 0
                self.to_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] <= 499].index[-1]
            case 2:
                self.from_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] >= 500].index[0]
                self.to_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] <= 799].index[-1]
            case 3:
                self.from_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] >= 800].index[0]
                self.to_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] <= 999].index[-1]
            case 4:
                self.from_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] >= 1000].index[0]
                self.to_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] <= 1399].index[-1]
            case 5:
                self.from_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] >= 1400].index[0]
                self.to_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] <= 1599].index[-1]
            case 6:
                self.from_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] >= 1600].index[0]
                self.to_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] <= 1799].index[-1]
            case 7:
                self.from_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] >= 1800].index[0]
                self.to_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] <= 1999].index[-1]
            case 8:
                self.from_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] >= 2000].index[0]
                self.to_ind = self.df_mateIn2.loc[self.df_mateIn2['Rating'] <= 3500].index[-1]

    def parse(self):
        ind = rnd.randint(self.from_ind, self.to_ind)
        puzzle = [self.df_mateIn2.iloc[ind]['PuzzleId'], self.df_mateIn2.iloc[ind]['FEN'],
                  self.df_mateIn2.iloc[ind]['Moves']]
        return puzzle
