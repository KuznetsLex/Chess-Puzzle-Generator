import Generator
from PuzzleManager import Puzzle


def main():
    difficulty_level = 4  # выбираем уровень сложности (1-8)
    number_of_puzzles_to_generate = 2  # выбираем количество задач

    # извлекаем случайную задачу
    puzzle_manager = Puzzle(difficulty_level)
    puzzle_orig = puzzle_manager.parse()

    # генерируем задачи
    generated_puzzles = [str(Generator.generate(puzzle_orig)) for _ in range(number_of_puzzles_to_generate)]

    #  записываем задачи в файл
    f = open('generatedPuzzles.txt', 'w')
    f.write(str(puzzle_orig) + "\n" + "\n".join(generated_puzzles))
    f.close()


if __name__ == "__main__":
    main()
