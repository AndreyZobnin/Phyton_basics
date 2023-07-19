"""Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса"""

from Seminar9.old_hw.hw1 import guessing_game, random_int_number
from old_hw.hw9 import guessing_numbers
from old_hw.ex6 import guesses_dict

if __name__ == '__main__':
    game = input('Выберите 1 игру:\n'
                 '1 - Угадай число версия из домашки 1 \n'
                 '2 - Угадайка чисел версия с декоратором \n'
                 '3 - Угадайка загадок из семинара № 6)')
    match game:
        case('1'):
            guessing_game(random_int_number())

        case('2'):
            print(guessing_numbers.__name__)
            print(guessing_numbers(40, 5))

        case ('3'):
            guesses = {'Зимой и летом одним цветом': ['елка', 'ёлка', 'ель', 'елочка' 'ёлочка', 'сосна'],
                       'Не лает, не кусает, а в дом не пускает': ['замок', 'замочек'],
                       'Сидит дед, во сто шуб одет': ['лук', 'луковица'],
                       'Висит груша нельзя скушать': ['лампа', 'лампочка']}
            guesses_dict(guesses)