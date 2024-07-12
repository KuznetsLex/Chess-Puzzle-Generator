import pandas as pd
import random as rnd
class Puzzle:
    def __init__(self, n):
        self.n = n
    def parse(self):
      df_mateIn2 = pd.read_csv('mateIn2.csv', index_col=0)
      from_ind = 0
      to_ind = 0
      match int(self.n):
        case 1:
          from_ind = 0
          to_ind = df_mateIn2.loc[df_mateIn2['Rating'] <= 499].index[-1]
        case 2:
          from_ind = df_mateIn2.loc[df_mateIn2['Rating'] >= 500].index[0]
          to_ind = df_mateIn2.loc[df_mateIn2['Rating'] <= 799].index[-1]
        case 3:
          from_ind = df_mateIn2.loc[df_mateIn2['Rating'] >=800].index[0]
          to_ind = df_mateIn2.loc[df_mateIn2['Rating'] <= 999].index[-1]
        case 4:
          from_ind = df_mateIn2.loc[df_mateIn2['Rating'] >= 1000].index[0]
          to_ind = df_mateIn2.loc[df_mateIn2['Rating'] <= 1399].index[-1]
        case 5:
          from_ind = df_mateIn2.loc[df_mateIn2['Rating'] >= 1400].index[0]
          to_ind = df_mateIn2.loc[df_mateIn2['Rating'] <= 1599].index[-1]
        case 6:
          from_ind = df_mateIn2.loc[df_mateIn2['Rating'] >= 1600].index[0]
          to_ind = df_mateIn2.loc[df_mateIn2['Rating'] <= 1799].index[-1]
        case 7:
          from_ind = df_mateIn2.loc[df_mateIn2['Rating'] >= 1800].index[0]
          to_ind = df_mateIn2.loc[df_mateIn2['Rating'] <= 1999].index[-1]
        case 8:
          from_ind = df_mateIn2.loc[df_mateIn2['Rating'] >= 2000].index[0]
          to_ind = df_mateIn2.loc[df_mateIn2['Rating'] <= 3500].index[-1]

      ind = rnd.randint(from_ind, to_ind)
      puzzle = []
      puzzle.append(df_mateIn2.iloc[ind]['PuzzleId'])
      puzzle.append(df_mateIn2.iloc[ind]['FEN'])
      puzzle.append(df_mateIn2.iloc[ind]['Moves'])
      return puzzle
