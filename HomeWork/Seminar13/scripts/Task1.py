from Seminar13.scripts.Exept import DiffLenException, NotIntException, ZeroLenException, NotListException, \
    NotFloatException, NotPercentSignException, NegativeNumberException, ZeroLenStr


class StaffInfo:
    """Класс, хранящий три списка одинаковой длины: имена str, ставка int,
    премия str с указанием процентов вида «10.20%»."""
    def __init__(self, names, salaries, percents):
        if not len(names) == len(salaries) == len(percents):
            raise DiffLenException(names, salaries, percents)
        for s in names:
            if len(s) == 0:
                raise ZeroLenStr('Имя')

        if not isinstance(names, list):
            raise NotListException('names')
        if not isinstance(salaries, list):
            raise NotListException('salaries')
        if not isinstance(percents, list):
            raise NotListException('percents')

        for item in salaries:
            if not isinstance(item, int):
                raise NotIntException(item)
            if item < 0:
                raise NegativeNumberException('Зарплата', item)

        for item in percents:
            if '%' not in item:
                raise NotPercentSignException(item)
            if not self._is_str_float(item[:-1]):
                raise NotFloatException(item)
            if float(item[:-1]) < 0:
                raise NegativeNumberException('Бонус', item)

        if len(names) == 0:
            raise ZeroLenException()

        self._names = names
        self._salaries = salaries
        self._percents = percents

    def calc_bonuses(self):
        """Генератор словаря, который возвращает словарь с именем в качестве ключа
        и суммой премии в качестве значения."""
        return {self._names[i]: round(self._salaries[i] * (float(self._percents[i][:-1:]) / 100), 2)
                for i in range(len(self._salaries))}

    @staticmethod
    def _is_str_float(s: str) -> bool:
        """Проверка возможности преобразования строки в число с плавающей точкой"""
        try:
            float(s)
            return True
        except ValueError:
            return False