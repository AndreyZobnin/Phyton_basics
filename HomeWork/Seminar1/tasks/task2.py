""" Задание №1 (№9 семинара)
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке."""


FIRST_TABLE_START = 2
SECOND_TABLE_START = 6
START_NUM = 2


def is_digit(num):
    if 1 <= num <= 9:
        return True
    return False


def draw_table(row, col, start):

    for row_num in range(start, row + 1):
        col_num = col

        while col_num <= col + 3:
            result = col_num * row_num

            if is_digit(result) and is_digit(row_num) and is_digit(col_num):
                print(f'{col_num} X {row_num}  =  {result}', end='    ')
            if not is_digit(result) and is_digit(row_num) and is_digit(col_num):
                print(f'{col_num} X {row_num}  = {result}', end='    ')
            if not is_digit(result) and not is_digit(row_num) and is_digit(col_num):
                print(f'{col_num} X {row_num} = {result}', end='    ')

            col_num += 1

        print()
    print()


def mult_table():
    print('\n', ' ' * 20, 'ТАБЛИЦА УМНОЖЕНИЯ\n')

    rows = 10

    draw_table(rows, FIRST_TABLE_START, START_NUM)
    draw_table(rows, SECOND_TABLE_START, START_NUM)
