import berserk
import chess
import chess.engine

# Инициализация API
token = 'lip_N2yQyunSWcrSzKlnSW9k'
session = berserk.TokenSession(token)
client = berserk.Client(session)
engine = chess.engine.SimpleEngine.popen_uci("D:\\chess\\stockfish\\stockfish-windows-x86-64-sse41-popcnt.exe")

def evaluate_position(board, depth=10):
    # Анализ позиции на заданную глубину
    info = engine.analyse(board, chess.engine.Limit(depth=depth))
    # Получение относительной оценки позиции
    return info['score'].relative.score(mate_score=10000)/100
print (evaluate_position('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'))