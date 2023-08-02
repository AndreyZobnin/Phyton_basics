class Exceptions(Exception):
    pass


class NotListException(Exceptions):
    def __init__(self, data: str):
        self.data = data

    def __str__(self):
        return f'\nТип поданного на вход списка {self.data} должен быть list!\n'


class ZeroLenStr(Exceptions):
    def __init__(self, field: str):
        self._field = field

    def __str__(self):
        return f'\nЗначения списка "{self._field}" не может быть пустым!\n'


class DiffLenException(Exceptions):
    def __init__(self, names: list[str], salaries: list[int], percents: list[str]):
        self._names = names
        self._salaries = salaries
        self._percents = percents

    def __str__(self):
        return f'\nДлины списков данных не совпадают:\n' \
               f'- {len(self._names)} имён,\n' \
               f'- {len(self._salaries)} зарплат,\n' \
               f'- {len(self._percents)} процентов бонусов\n'


class NotIntException(Exceptions):
    def __init__(self, salary: int | str):
        self._salary = salary

    def __str__(self):
        return f'\nЗначение {self._salary} должно быть целым числом!\n'


class NotFloatException(Exceptions):
    def __init__(self, bonus):
        self._bonus = bonus[:-1]

    def __str__(self):
        return f'\nЗначение бонуса {self._bonus} должно быть целым или дробным числом!\n'


class NotPercentSignException(Exceptions):
    def __init__(self, bonus):
        self._bonus = bonus

    def __str__(self):
        return f'\nЗначение бонуса ({self._bonus}) должно быть со знаком процента (%)!\n'


class NegativeNumberException(Exceptions):
    def __init__(self, lst_name: str, num: float | int):
        self._lst_name = lst_name
        self._num = num

    def __str__(self):
        return f'\nЗначение в списке "{self._lst_name}" = {self._num} должно быть положительным!\n'


class ZeroLenException(Exceptions):
    def __init__(self):
        pass

    def __str__(self):
        return f'\nСписки данных не могут быть пустыми!\n'