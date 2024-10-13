# Chess Puzzle Generator
Программа извлекает случайную задачу выбранного уровня сложности из базы данных и генерирует на её основе массив похожих задач.
Сгенерированная задача отличается от исходной позицией и достоинство фигуры игрока.

В репозитории отркажена работа за две недели Большой Математической Мастерской 2024. Проект продолжает развиваться здесь: https://github.com/EkaterinaDerisheva/ChessPuzzleGenerator

## Demo

### How to use
https://github.com/user-attachments/assets/b872a384-4bb8-4501-8386-53a1e93ee025

### Сгенерированная задача
На скриншоте привден пример сгенерированной задачи. Красными кругами отмечены фигуры, поменявшие свое начальное положение пазла. Кругом с перекрестием отмечен первый ход игрока (шах конем). Мат ставит ладья.
<img width="1273" alt="Screenshot 2024-10-14 at 00 13 16" src="https://github.com/user-attachments/assets/c318a0f1-ac26-460a-ab1e-eacf395fa6e4">

### Презентация в PDF
[Chess_puzzle_generator.pdf](https://github.com/user-attachments/files/17356647/_.pdf)

## Build&Run
Для разработки используется Python 3.10

## External dependencies
С помощью pip необходимо установить следующие зависимости:
* библиотека pandas для работы с базой шахматных задач
* библиотека pygame для взаимодействия со сгенерированными пазлами
