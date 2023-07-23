'''Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра.'''

from random import randint


class Matrix:
    def __init__(self, matrix: list(list())):
        self.matrix = matrix

    def get_matrix(self):
        return self.matrix

    def trans_matrix(self):
        transposed_matrix = []
        matrix_cols_count = len(self.matrix)
        matrix_rows_count = len(self.matrix[0])

        for i in range(matrix_rows_count):
            transposed_matrix.append([])
            for j in range(matrix_cols_count):
                transposed_matrix[i].append(self.matrix[j][i])

        return transposed_matrix


class Variables:
    def __init__(self, *args):
        self.args = args

    def variables_without_s(self):
        ending_s_variables = dict()

        for key, value in globals().items():
            if value in self.args and key[-1] == 's' and len(key) > 1:
                ending_s_variables[key] = value
                globals()[key] = None

        return ending_s_variables.keys()


class Game:
    def __init__(self, lower_limit: int, upper_limit: int, attemps: int):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.rand_number = randint(lower_limit, upper_limit)
        self.attemps = attemps

    def guessing_game(self):
        current_attempts = self.attemps

        while current_attempts > 0:
            user_num = int(input(f'Введите целое число от {self.lower_limit} до {self.upper_limit}:  '))

            if user_num == self.rand_number:
                print(f'Вы угадали! Загаданное число - {self.rand_number}')
                return True

            if user_num > self.rand_number:
                print(f'Число {user_num} больше загаданного...')

            if user_num < self.rand_number:
                print(f'Число {user_num} меньше загаданного...')

            current_attempts -= 1
            print(f'Осталось {current_attempts} попыток')

        else:
            print(f'Попытки закончились, Вы не угадали загаданное число {self.rand_number}')
            return False


if __name__ == '__main__':
    matr = Matrix([[1, 2, 3, 4, 5],
                   [11, 22, 33, 44, 55],
                   [111, 222, 333, 444, 555],
                   [1111, 2222, 3333, 4444, 5555]])
    transp_matr = matr.trans_matrix()
    print('Исходная матрица:')
    for col in matr.get_matrix():
        print(*col)
    print('\nМатрица после транспонирования:')
    for col in transp_matr:
        print(*col)

    print()
    mercury = 'Mercury'
    venus = 'Venus'
    earth = 'Earth'
    mars = 'Mars'
    jupiter = 'Jupiter'
    saturn = 'Saturn'
    uranus = 'Uranus'
    s = 6
    vars = Variables(mercury, venus, earth, mars, jupiter, saturn, uranus, s)
    print('Переменные, имена которых более одного символа и оканчиваются на "s":')
    for item in vars.variables_without_s():
        print(item)

    print()
    number_to_guess = Game(0, 100, 7)
    number_to_guess.guessing_game()