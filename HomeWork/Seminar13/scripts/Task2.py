from Seminar13.scripts.Exept import NotIntException

result = ''
NUM_ONE = 1
NUM_TEN = 10
NUM_HUNDRED = 100
NUM_THOUSAND = 1000
SQUARE = 2


def checking_digits_count() -> str:
    while True:
        num = input('Введите число от 1 до 999... ')
        if not is_str_int(num):
            raise NotIntException(num)
        num = int(num)

        if NUM_ONE <= num < NUM_TEN:
            return f'Это цифра, её значение в квадрате = {num ** SQUARE}'
        elif NUM_TEN <= num < NUM_HUNDRED:
            tmp1 = num // NUM_TEN
            tmp2 = num % NUM_TEN
            return f'Это двузначное число, произведение его цифр = {tmp1 * tmp2}'
        elif NUM_HUNDRED <= num < NUM_THOUSAND:
            tmp1 = num // NUM_HUNDRED
            tmp2 = num // NUM_TEN % NUM_TEN
            tmp3 = num % NUM_TEN
            return f'Это трёхзначное число, зеркальное ему число: {tmp3 * NUM_HUNDRED + tmp2 * NUM_TEN + tmp1}'
        else:
            print('Ошибка, введено  число не из диапазона')
            continue


def is_str_int(s: str) -> bool:
    """Проверка возможности преобразования строки в целое число"""
    try:
        int(s)
        return True
    except ValueError:
        return False