"""Создайте класс Матрица. Добавьте методы для:
- вывода на печать,
- сравнения,
- сложения,
- *умножения матриц"""


class Matrix:
    """Класс, принимающий на вход матрицу для печати, сравнения, сложения и умножения"""

    def __init__(self, matrix_: list[list[int]]):
        """Принимает матрицу как параметр (matrix_: list[list[int]]) и определяет её размерности"""
        self.__matrix = matrix_
        self.__matrix_cols = len(matrix_)
        self.__matrix_rows = len(matrix_[0])

    def printing(self):
        for col in self.__matrix:
            for i in range(self.__matrix_cols):
                if i < self.__matrix_cols - 1:
                    print(col[i], end=' ')
                elif i >= self.__matrix_cols - 1 and i != 0:
                    print(col[i], end='')
            print()

    def sum_elements(self):
        """Функция, определяющая сумму всех элементов матрицы"""
        sum_el = 0
        for i in range(self.__matrix_cols):
            for j in range(self.__matrix_rows):
                sum_el += self.__matrix[i][j]
        return sum_el

    def __eq__(self, other):
        """Сравнение двух матриц на равенство всех элементов и размерностей"""
        if self.__matrix_cols != other.__matrix_cols or self.__matrix_rows != other.__matrix_rows:
            return False

        for i in range(self.__matrix_cols):
            for j in range(self.__matrix_rows):
                if self.__matrix[i][j] != other.__matrix[i][j]:
                    return False
        return True

    def __lt__(self, other):
        """Сравнение сумм элементов двух матриц на строго меньше"""
        return self.sum_elements() < other.sum_elements()

    def __le__(self, other):
        """Сравнение сумм элементов двух матриц на меньше или равно"""
        return self.sum_elements() <= other.sum_elements()

    def __add__(self, other):
        """Сложение двух матриц. Возможно только для матриц одинаковых размерностей"""
        if self.__matrix_cols != other.__matrix_cols or self.__matrix_rows != other.__matrix_rows:
            return 'Нельзя складывать матрицы разных размерностей!'

        result_matrix = []

        for i in range(self.__matrix_cols):
            result_matrix.append([])
            for j in range(self.__matrix_rows):
                result_matrix[i].append(self.__matrix[i][j] + other.__matrix[i][j])

        return Matrix(result_matrix)

    def __mul__(self, other):
        """Умножение двух матриц. Возможно, когда число столбцов первой матрицы равно числу строк второй матрицы"""
        if self.__matrix_rows != other.__matrix_cols:
            return f'Произведение двух матриц возможно только в том случае,' \
                   f'когда число столбцов матрицы 1 совпадает с числом строк матрицы 2'

        result_matrix = []

        for i in range(self.__matrix_cols):
            result_matrix.append([])
            for j in range(other.__matrix_rows):
                temp_sum = 0
                for k in range(self.__matrix_rows):
                    temp_sum += self.__matrix[i][k] * other.__matrix[k][j]
                result_matrix[i].append(temp_sum)

        return Matrix(result_matrix)

    def __str__(self):
        return f'Параметры матрицы:\n' \
               f'- количество строк: {self.__matrix_cols}\n' \
               f'- количество столбцов: {self.__matrix_rows}\n'

    def __repr__(self):
        return f'Matrix({self.__matrix})'


if __name__ == '__main__':
    matrix_first = Matrix([[1, 2, 3, 4, 5],
                           [3, 8, 4, 0, 2],
                           [8, 3, 7, 1, 2],
                           [4, 6, 8, 8, 3]])

    matrix_second = Matrix([[1, 2, 3, 4, 5],
                            [3, 8, 4, 0, 2],
                            [8, 3, 7, 1, 2],
                            [4, 6, 8, 8, 3]])

    matrix_third = Matrix([[7, 9, 8, 7, 9, 4],
                           [9, 7, 3, 7, 6, 4],
                           [9, 5, 7, 6, 2, 0],
                           [1, 3, 7, 6, 3, 8],
                           [9, 6, 8, 4, 7, 3]])

    matrix_fourth = Matrix([[0, 8],
                            [1, 9],
                            [5, 6],
                            [4, 6],
                            [4, 4]])

    matrix_first.printing()
    print()
    print(matrix_first)
    print(f'{matrix_first = }')
    print()

    print(f'{matrix_first == matrix_second = }')
    print(f'{matrix_first == matrix_third = }')
    print(f'{matrix_first != matrix_fourth = }')

    print(f'{matrix_first <= matrix_second = }')
    print(f'{matrix_first > matrix_third = }')
    print(f'{matrix_first >= matrix_fourth = }')

    print(f'{matrix_first + matrix_second = }')
    print(f'{matrix_first + matrix_fourth = }')

    print(f'{matrix_first * matrix_second = }')
    print(f'{matrix_first * matrix_third = }')
    print(f'{matrix_first * matrix_fourth = }')

    print(help(Matrix))
