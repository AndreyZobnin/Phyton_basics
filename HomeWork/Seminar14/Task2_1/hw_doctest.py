import doctest

MULT = 50
PERCENT = 0.985
EXTRA_PERCENT = 1.03
RICH_PERCENT = 0.9
MIN_CASH = 30
MAX_CASH = 600
BONUS_COUNT = 3
MAX_SCORE = 5_000_000
count = 0
total_score = 0


def bonus_cash(total_cash, count_num):
    """
    >>> bonus_cash(500, 1)
    500
    >>> bonus_cash(500, 3)
    За каждую третью операцию начисляется 3%. Вам дополнительно начислено 15.0 на остаток по счёту.
    515.0
    """
    if count_num % BONUS_COUNT == 0:
        tmp_cash = total_cash
        total_cash *= EXTRA_PERCENT
        print(f'За каждую третью операцию начисляется 3%. '
              f'Вам дополнительно начислено {total_cash - tmp_cash} на остаток по счёту.')

    return total_cash


def operation_add_to_total(money, count_num, total):
    """
    >>> operation_add_to_total(695, 1, 5_000)
    Сумма должна быть кратна 50!
    [5000, 1]
    >>> operation_add_to_total(0, 1, 5_000)
    Сумма должна быть кратна 50!
    [5000, 1]
    >>> operation_add_to_total(500, 1, 5_000)
    Сумма 500 успешно внесена на счёт
    [5500, 2]
    """
    if is_multiplicity(money):
        count_num += 1
        total += money

        print(f'Сумма {money} успешно внесена на счёт')

    else:
        print('Сумма должна быть кратна 50!')

    return [total, count_num]


def take_cash(cash):
    """
    >>> take_cash(5_000)
    4925.0
    >>> take_cash(100_000)
    99400
    >>> take_cash(300)
    270
    >>> take_cash(0)
    -30
    """
    take_off_sum = cash * (1 - PERCENT)

    if take_off_sum > MAX_CASH:
        cash -= MAX_CASH

    elif take_off_sum < MIN_CASH:
        cash -= MIN_CASH

    else:
        cash *= PERCENT

    return cash


def operation_take_from_total(money, count_num, total):
    """
    >>> operation_take_from_total(300, 1, 10_000)
    Выдано 270, списано процентов 30
    [9700, 2]
    >>> operation_take_from_total(300, 1, 200)
    Превышен лимит. Вы можете снять сумму не более 200!
    [200, 1]
    >>> operation_take_from_total(280, 1, 10_000)
    Сумма должна быть кратна 50!
    [10000, 1]
    """
    cash_to_take = take_cash(money)

    if is_multiplicity(money) and not is_overrun(money, total):
        percents = money - cash_to_take
        count_num += 1

        print(f'Выдано {cash_to_take}, списано процентов {percents}')
        total -= money

    elif is_overrun(money, total):
        print(f'Превышен лимит. Вы можете снять сумму не более {total}!')

    else:
        print('Сумма должна быть кратна 50!')

    return [total, count_num]


def is_multiplicity(cash):
    """
    >>> is_multiplicity(100)
    True
    >>> is_multiplicity(100.0)
    True
    >>> is_multiplicity(-100)
    True
    >>> is_multiplicity(70)
    False
    >>> is_multiplicity(0)
    False
    """
    return True if cash % 50 == 0 and cash != 0 else False


def is_overrun(cash_with_percents, total_cash):
    """
    >>> is_overrun(200, 100)
    True
    >>> is_overrun(100, 200)
    False
    >>> is_overrun(100, 100)
    False
    """
    return True if cash_with_percents > total_cash else False


def rich_tax(total_cash):
    """
    >>> rich_tax(5_000_000)
    Вы очень богаты, Ура, поделитесь?
    С Вашего счёта снято 10% - 499999.9999999999
    На Вашем счету 4500000.0...
    <BLANKLINE>
    4500000.0
    >>> rich_tax(6_000_000)
    Вы очень богаты, надо поделиться!
    С Вашего счёта снято 10% - 599999.9999999999
    На Вашем счету 5400000.0...
    <BLANKLINE>
    5400000.0
    >>> rich_tax(500)
    500
    """
    if total_cash >= MAX_SCORE:
        print(f'Вы очень богаты, надо поделиться!\n'
              f'С Вашего счёта снято 10% - {total_cash * (1 - RICH_PERCENT)}')
        total_cash *= RICH_PERCENT
        print_total_cash(total_cash)

    return total_cash


def print_total_cash(total_cash):
    """
    >>> print_total_cash(500)
    На Вашем счету 500...
    <BLANKLINE>
    """
    print(f'На Вашем счету {total_cash}...\n')


if __name__ == '__main__':
    doctest.testmod(verbose=True)
