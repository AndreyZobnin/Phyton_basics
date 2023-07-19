""" Задание №1 (№8 семинара)
Нарисовать в консоли ёлку спросив у пользователя количество рядов."""

from Seminar1.modules.input import num_input_check as num_input
from Seminar1.modules.input import is_natural_num as is_natural


MIN_ROWS = 1
MAX_ROWS = 100


def print_tree(rows):
    for row in range(rows):
        print(f"{' ' * (rows - 1)}{'*' * (row + 1)}{'*' * row}")
        rows -= 1
    print()


def draw_tree(text):
    tree_rows = num_input(text)

    if is_natural(tree_rows) and tree_rows <= MAX_ROWS:
        print_tree(tree_rows)

    elif tree_rows > MAX_ROWS:
        draw_tree(f'Число слишком большое, введите число от {MIN_ROWS} до {MAX_ROWS}')

    else:
        draw_tree(f'Вы ввели число меньше {MIN_ROWS}, введите положительное число')
