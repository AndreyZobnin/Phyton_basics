""" Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. """

from Seminar1.modules.input import num_input_check as inp


def is_simple(num):
    current_num = num - 1

    while current_num >= 2:
        if num % current_num == 0:
            return False
        current_num -= 1

    else:
        return True


def number_type_enter():
    while True:
        number = inp('Введите положительное целое число не более 100 000')
        if 0 < number <= 100000:
            break
        continue

    if is_simple(number):
        print(f'Число {number} простое\n')
    else:
        print(f'число {number} составное\n')
