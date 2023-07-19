""" Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. """

from random import randint
from Seminar9.old_hw.modules.start import num_input_check as inp


LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 10


def random_int_number():
    return randint(LOWER_LIMIT, UPPER_LIMIT)


def guessing_game(hidden_num):
    current_attempts = ATTEMPTS

    while current_attempts > 0:
        user_num = inp('Введите целое число от 1 до 1000')

        if user_num == hidden_num:
            print(f'Вы угадали! Загаданное число - {hidden_num}')
            break

        if user_num > hidden_num:
            print(f'Число {user_num} больше загаданного...')

        if user_num < hidden_num:
            print(f'Число {user_num} меньше загаданного...')

        current_attempts -= 1
        print(f'Осталось {current_attempts} попыток')

    else:
        print(f'Попытки закончились, Вы не угадали загаданное число {hidden_num}')