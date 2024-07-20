import configparser as conf
import tkinter as tk

import chess
import chess.engine
import joblib
import pandas as pd
from PIL import Image, ImageTk

# Загрузка модели и scaler
best_model = joblib.load('chess_rating_model.pkl')
scaler = joblib.load('scaler.pkl')

# Загрузка конфигурации
config = conf.RawConfigParser()
config.read('./config.properties')
engine_path = config.get("Main", "EngineStr")

# Инициализация движка
engine = chess.engine.SimpleEngine.popen_uci(engine_path)

def predict_user_rating(first_line_percentage, second_line_percentage, third_line_percentage, bad_moves_percentage):
    input_data = pd.DataFrame({
        'first_line_percentage': [first_line_percentage],
        'second_line_percentage': [second_line_percentage],
        'third_line_percentage': [third_line_percentage],
        'bad_moves_percentage': [bad_moves_percentage]
    })
    input_data_scaled = scaler.transform(input_data)
    predicted_rating = best_model.predict(input_data_scaled)
    return predicted_rating[0]

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ChessTrainer GMW")
        self.root.configure(bg='#f0f0f0')  # Установка фона окна
        self.board = chess.Board()
        self.images = {}
        self.load_images()

        self.canvas = tk.Canvas(root, width=480, height=480)
        self.canvas.pack(pady=10)

        self.status_label = tk.Label(root, text="Your turn", font='arial 12 bold', bg='#d9d9d9', fg='#333333')
        self.status_label.pack(pady=5)

        self.rating_label = tk.Label(root, text="Predicted Rating: N/A | Engine ELO: N/A", font='arial 12 bold', bg='#d9d9d9', fg='#333333')
        self.rating_label.pack(pady=5)

        self.surrender_button = tk.Button(root, text="Сдаться", command=self.surrender, font='arial 12 bold', bg='#ffcccc', fg='#333333')
        self.surrender_button.pack(pady=10)

        self.canvas.bind("<Button-1>", self.click)

        self.draw_board()

        # Статистика ходов
        self.firstLine = 0
        self.secondLine = 0
        self.thirdLine = 0
        self.badMoves = 0
        self.totalMoves = 0

        # Уровень движка
        self.current_engine_elo = 500
        self.update_engine_level()

    def load_images(self):
        pieces = {
            'b': 'bB.png', 'k': 'bK.png', 'n': 'bN.png', 'p': 'bP.png', 'q': 'bQ.png', 'r': 'bR.png',
            'B': 'wB.png', 'K': 'wK.png', 'N': 'wN.png', 'P': 'wP.png', 'Q': 'wQ.png', 'R': 'wR.png'
        }
        for piece, filename in pieces.items():
            self.images[piece] = ImageTk.PhotoImage(
                Image.open(f"C:/Users/vovab/ChessTrainerNEW/ChessAI/images_GUI/{filename}") #Change path depend on yours
            )

    def draw_board(self):
        self.canvas.delete("all")
        color = True
        for rank in range(8):
            for file in range(8):
                x1 = file * 60
                y1 = rank * 60
                x2 = x1 + 60
                y2 = y1 + 60
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white" if color else "blue")
                color = not color
            color = not color

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                x = (square % 8) * 60
                y = (7 - square // 8) * 60
                piece_image = self.images.get(piece.symbol())
                if piece_image:
                    self.canvas.create_image(x, y, image=piece_image, anchor=tk.NW)

    def click(self, event):
        x = event.x // 60
        y = 7 - (event.y // 60)
        square = chess.square(x, y)
        piece = self.board.piece_at(square)
        if piece and piece.color == self.board.turn:
            self.selected_square = square
        elif hasattr(self, 'selected_square'):
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                best_move_info = engine.analyse(self.board, chess.engine.Limit(time=0.5))
                best_move = best_move_info['pv'][0]
                self.board.push(best_move)
                best_move_eval = engine.analyse(self.board, chess.engine.Limit(time=0.5))['score'].relative.score(
                    mate_score=10000) / 100.0
                self.board.pop()

                # Выполняем ход пользователя
                self.board.push(move)
                user_move_info = engine.analyse(self.board, chess.engine.Limit(time=0.5))
                user_move_eval = user_move_info['score'].relative.score(mate_score=10000) / 100.0

                # Подсчет статистики
                difference = abs(best_move_eval - user_move_eval)
                if difference < 0.4:
                    self.firstLine += 1
                elif 0.4 <= difference < 0.7:
                    self.secondLine += 1
                elif 0.7 <= difference < 1.0:
                    self.thirdLine += 1
                else:
                    self.badMoves += 1
                self.totalMoves += 1

                self.after_user_move()
                self.draw_board()
                del self.selected_square

    def after_user_move(self):
        if self.board.is_checkmate():
            self.status_label.config(text="Checkmate")
            self.print_statistics()
            return
        engine_move = engine.play(self.board, chess.engine.Limit(time=1.0)).move
        self.board.push(engine_move)
        self.draw_board()

        if self.board.is_checkmate():
            self.status_label.config(text="Checkmate")
            self.print_statistics()
            return

        # Оценка после каждого хода
        self.evaluate_game()

    def evaluate_game(self):
        if self.totalMoves == 0:
            return

        first_line_percentage = (self.firstLine / self.totalMoves) * 100
        second_line_percentage = (self.secondLine / self.totalMoves) * 100
        third_line_percentage = (self.thirdLine / self.totalMoves) * 100
        bad_moves_percentage = (self.badMoves / self.totalMoves) * 100

        predicted_rating = predict_user_rating(first_line_percentage, second_line_percentage, third_line_percentage,
                                               bad_moves_percentage)
        self.update_engine_level(predicted_rating)
        self.rating_label.config(
            text=f"Predicted Rating: {int(predicted_rating)} | Engine ELO: {self.current_engine_elo}")

    # Изменение рейтинга движка после каждого хода
    def update_engine_level(self, predicted_rating=500):
        if predicted_rating < 800:
            self.current_engine_elo = 500
        elif 800 <= predicted_rating < 1200:
            self.current_engine_elo = 1000
        elif 1200 <= predicted_rating < 1600:
            self.current_engine_elo = 1400
        elif 1600 <= predicted_rating < 2000:
            self.current_engine_elo = 1800
        elif 2000 <= predicted_rating < 2400:
            self.current_engine_elo = 2200
        else:
            self.current_engine_elo = 2500

        skill_level = (self.current_engine_elo - 500) // 100
        engine.configure({"Skill Level": skill_level})

    # функция, заканчивающая игру
    def surrender(self):
        self.status_label.config(text="You surrendered")
        self.print_statistics()

    def print_statistics(self):
        print(f"Total Moves: {self.totalMoves}")
        print(f"First Line Moves: {self.firstLine}")
        print(f"Second Line Moves: {self.secondLine}")
        print(f"Third Line Moves: {self.thirdLine}")
        print(f"Bad Moves: {self.badMoves}")

    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessApp(root)
    app.mainloop()

    engine.quit()