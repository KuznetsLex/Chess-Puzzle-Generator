import csv

import berserk
import chess
import chess.engine
import pandas as pd

# Инициализация API
token = 'lip_N2yQyunSWcrSzKlnSW9k'
session = berserk.TokenSession(token)
client = berserk.Client(session)
engine = chess.engine.SimpleEngine.popen_uci("D:\\chess\\stockfish\\stockfish-windows-x86-64-sse41-popcnt.exe")
engine.configure({"Threads": 4})  # Установка числа потоков (1-32)

def write_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.columns)  # Запись заголовков столбцов
        for index, row in data.iterrows():
            writer.writerow(row)
def evaluate_position(board, depth=10):
    info = engine.analyse(board, chess.engine.Limit(depth=depth))
    # Получение оценки позиции
    return info['score'].relative.score(mate_score=10000) / 100  # Преобразование
def get_best_move(board, depth=10):
    result = engine.play(board, chess.engine.Limit(depth=depth))
    return result.move
def analyze_games(usernames, max_games=10):
    data = []
    for username in usernames:
        games = client.games.export_by_player(username, max=max_games)

        for game in games:
            white_rating = game['players']['white']['rating']
            black_rating = game['players']['black']['rating']
            moves = game['moves'].split()

            player_color = 'white' if game['players']['white']['user']['name'].lower() == username.lower() else 'black'
            player_rating = white_rating if player_color == 'white' else black_rating
            board = chess.Board()

            # Переменные для хранения данных
            first_line_moves = 0
            second_line_moves = 0
            third_line_moves = 0
            bad_moves = 0
            total_moves = 0

            # Анализируем все ходы
            for move_index, move_san in enumerate(moves):
                is_users_move = (player_color == 'white' and move_index % 2 == 0) or (
                    player_color == 'black' and move_index % 2 != 0)

                if not is_users_move:
                    board.push_san(move_san)
                    continue

                try:
                    move_obj = board.parse_san(move_san)
                except ValueError:
                    continue

                legal_moves = list(board.legal_moves)

                if move_obj in legal_moves:
                    # Оценка позиции перед ходом
                    pre_move_score = evaluate_position(board)

                    # Оценка лучшего хода
                    best_move = get_best_move(board, depth=10)
                    board.push(best_move)
                    best_move_score = evaluate_position(board)
                    board.pop()

                    board.push(move_obj)
                    post_move_score = evaluate_position(board)

                    score_difference = post_move_score - best_move_score
                    if move_index < 10:
                        if score_difference <= 0.5:
                            first_line_moves += 1
                        elif 0.5 < score_difference <= 1:
                            second_line_moves += 1
                        elif 1 < score_difference <= 2:
                            third_line_moves += 1
                        else:
                            bad_moves += 1
                    else:
                        if score_difference <= 0.5:
                            first_line_moves += 1
                        elif 0.5 < score_difference <= 1:
                            second_line_moves += 1
                        elif score_difference > 1 and pre_move_score * 0.5 <= post_move_score:
                            third_line_moves += 1
                        else:
                            bad_moves += 1

                    total_moves += 1

                    board.pop()  # Отменяем ход для анализа следующего хода

                board.push_san(move_san)  # Восстанавливаем исходное состояние доски

            if total_moves > 0:
                data.append({
                    'username': username,
                    'user_rating': player_rating,
                    'first_line_percentage': format(first_line_moves / total_moves * 100, '.2f'),
                    'second_line_percentage': format(second_line_moves / total_moves * 100, '.2f'),
                    'third_line_percentage': format(third_line_moves / total_moves * 100, '.2f'),
                    'bad_moves_percentage': format(bad_moves / total_moves * 100, '.2f')
                })

    # Завершение работы движка
    engine.quit()

    return pd.DataFrame(data)

if __name__ == "__main__":
    usernames = ['Ro_ro2', 'Ali430','GelioChess', 'faceofmarlboro', 'kolosok2008']
    data = analyze_games(usernames, max_games=10)
    write_to_csv(data, 'chess_data.csv')
