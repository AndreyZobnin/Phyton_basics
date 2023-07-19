def num_input_check(message, param='integer'):
    while True:
        try:
            mess = input(f'{message}: ')

            if param == 'integer':
                return int(mess)
            elif param == 'float':
                return float(mess)

        except ValueError:
            if param == 'integer':
                message = 'Ошибка ввода, введите целое число...'
            elif param == 'float':
                message = 'Ошибка ввода, введите число...'
            continue


def is_natural_num(number):
    if number >= 1 and number % 1 == 0:
        return True
    return False
