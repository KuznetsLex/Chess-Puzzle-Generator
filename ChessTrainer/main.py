import pygame
import chess
import chess.engine
import sys

from PIL import ImageTk, Image
from sklearn.datasets import images

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 800
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


# Загрузка изображений
def load_images():
    pieces = {
        'b': 'bB.png', 'k': 'bK.png', 'n': 'bN.png', 'p': 'bP.png', 'q': 'bQ.png', 'r': 'bR.png',
        'B': 'wB.png', 'K': 'wK.png', 'N': 'wN.png', 'P': 'wP.png', 'Q': 'wQ.png', 'R': 'wR.png'
    }
    for piece, filename in pieces.items():
        images[piece] = ImageTk.PhotoImage(
            Image.open(f"C:/Users/vovab/ChessTrainerNEW/ChessAI/images_GUI/{filename}"))


# Рисование доски
def draw_board(screen):
    colors = [pygame.Color('white'), pygame.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


# Рисование фигур
def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board.piece_at(r * DIMENSION + c)
            if piece:
                screen.blit(IMAGES[piece.symbol()], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


# Оценка позиции
def evaluate_position(board, engine, depth=10):
    info = engine.analyse(board, chess.engine.Limit(depth=depth))
    return info['score'].relative.score(mate_score=10000) / 100


# Получение лучшего хода
def get_best_move(board, engine, depth=10):
    result = engine.play(board, chess.engine.Limit(depth=depth))
    return result.move


# Анализ хода
def analyze_move(board, move, engine, depth=10):
    pre_move_score = evaluate_position(board, engine, depth)
    best_move = get_best_move(board, engine, depth)

    board.push(best_move)
    best_move_score = evaluate_position(board, engine, depth)
    board.pop()

    board.push(move)
    post_move_score = evaluate_position(board, engine, depth)
    board.pop()

    score_difference = post_move_score - best_move_score
    user_winning = (pre_move_score >= 2.5)

    if user_winning:
        if score_difference <= 0.4:
            return "Сильнейший ход"
        elif 0.4 < score_difference <= 1:
            return "Ход по второй линии"
        elif 1 < score_difference <= 1.5:
            return "Ход по третьей линии"
        else:
            return "Плохой ход"
    else:
        if score_difference <= 0.5:
            return "Сильнейший ход"
        elif 0.5 < score_difference <= 1:
            return "Ход по второй линии"
        elif score_difference > 1 and pre_move_score * 0.5 <= post_move_score:
            return "Ход по третьей линии"
        else:
            return "Плохой ход"


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('white'))
    board = chess.Board()
    load_images()
    engine = chess.engine.SimpleEngine.popen_uci("D:\\chess\\stockfish\\stockfish-windows-x86-64-sse41-popcnt.exe")

    running = True
    square_selected = ()
    player_clicks = []

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if square_selected == (row, col):
                    square_selected = ()
                    player_clicks = []
                else:
                    square_selected = (row, col)
                    player_clicks.append(square_selected)
                if len(player_clicks) == 2:
                    move = chess.Move.from_uci(
                        f"{chess.square_name(chess.square(*player_clicks[0][::-1]))}"
                        f"{chess.square_name(chess.square(*player_clicks[1][::-1]))}"
                    )
                    if move in board.legal_moves:
                        board.push(move)
                        evaluation = analyze_move(board, move, engine)
                        print(f"Ход: {board.san(move)}, Оценка: {evaluation}")

                        opponent_move = get_best_move(board, engine)
                        board.push(opponent_move)
                        print(f"Ход Stockfish: {board.san(opponent_move)}")

                    square_selected = ()
                    player_clicks = []

        draw_board(screen)
        draw_pieces(screen, board)
        pygame.display.flip()
        clock.tick(MAX_FPS)

    engine.quit()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
