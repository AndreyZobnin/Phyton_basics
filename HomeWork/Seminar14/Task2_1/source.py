"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третьей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

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
    if count_num % BONUS_COUNT == 0:
        tmp_cash = total_cash
        total_cash *= EXTRA_PERCENT
        print(f'За каждую третью операцию начисляется 3%. '
              f'Вам дополнительно начислено {total_cash - tmp_cash} на остаток по счёту.')

    return total_cash


def operation_add_to_total(money, count_num, total):
    if is_multiplicity(money):
        count_num += 1
        total += money

        print(f'Сумма {money} успешно внесена на счёт')

    else:
        print('Сумма должна быть кратна 50!')

    return [total, count_num]


def take_cash(cash):
    take_off_sum = cash * (1 - PERCENT)

    if take_off_sum > MAX_CASH:
        cash -= MAX_CASH

    elif take_off_sum < MIN_CASH:
        cash -= MIN_CASH

    else:
        cash *= PERCENT

    return cash


def operation_take_from_total(money, count_num, total):
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
    return True if cash % 50 == 0 and cash != 0 else False


def is_overrun(cash_with_percents, total_cash):
    return True if cash_with_percents > total_cash else False


def rich_tax(total_cash):
    if total_cash >= MAX_SCORE:
        print(f'Вы очень богаты, надо поделиться!\n'
              f'С Вашего счёта снято 10% - {total_cash * (1 - RICH_PERCENT)}')
        total_cash *= RICH_PERCENT
        print_total_cash(total_cash)

    return total_cash


def print_total_cash(total_cash):
    print(f'На Вашем счету {total_cash}...\n')
