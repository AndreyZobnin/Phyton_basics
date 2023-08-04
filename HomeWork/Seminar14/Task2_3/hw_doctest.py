import doctest


matrix1 = [[1, 2], [1, 2]]
matrix2 = [[]]
matrix3 = [[1, 2], [1, 2]]
matrix4 = [[1, 2, 3], [4, 5, 6]]
matrix5 = [[1, 2], [3, 4], [5, 6]]


class Matrix:
    def __init__(self, matrix_: list[list[int]]):
        """
        >>> Matrix(matrix1)
        Matrix([[1, 2], [1, 2]])
        >>> Matrix(matrix2)
        Matrix([[]])
        """
        self.__matrix = matrix_
        self.__matrix_cols = len(matrix_)
        self.__matrix_rows = len(matrix_[0])

    def printing(self):
        """
        >>> Matrix(matrix1).printing()
        1 2
        1 2
        >>> Matrix(matrix2).printing()
        <BLANKLINE>
        """
        for col in self.__matrix:
            for i in range(self.__matrix_cols):
                if i < self.__matrix_cols - 1:
                    print(col[i], end=' ')
                elif i >= self.__matrix_cols - 1 and i != 0:
                    print(col[i], end='')
            print()

    def sum_elements(self):
        """
        >>> Matrix(matrix1).sum_elements()
        6
        >>> Matrix(matrix2).sum_elements()
        0
        """
        sum_el = 0
        for i in range(self.__matrix_cols):
            for j in range(self.__matrix_rows):
                sum_el += self.__matrix[i][j]
        return sum_el

    def __eq__(self, other):
        """
        >>> Matrix(matrix1) == Matrix(matrix2)
        False
        >>> Matrix(matrix1) == Matrix(matrix3)
        True
        >>> Matrix(matrix2) != Matrix(matrix3)
        True
        """
        if self.__matrix_cols != other.__matrix_cols or self.__matrix_rows != other.__matrix_rows:
            return False

        for i in range(self.__matrix_cols):
            for j in range(self.__matrix_rows):
                if self.__matrix[i][j] != other.__matrix[i][j]:
                    return False
        return True

    def __lt__(self, other):
        """
        >>> Matrix(matrix1) < Matrix(matrix2)
        False
        >>> Matrix(matrix1) >= Matrix(matrix3)
        True
        >>> Matrix(matrix2) < Matrix(matrix3)
        True
        """
        return self.sum_elements() < other.sum_elements()

    def __le__(self, other):
        """
        >>> Matrix(matrix1) > Matrix(matrix2)
        True
        >>> Matrix(matrix1) <= Matrix(matrix3)
        True
        >>> Matrix(matrix2) > Matrix(matrix3)
        False
        """
        return self.sum_elements() <= other.sum_elements()

    def __add__(self, other):
        """
        >>> (Matrix(matrix1) + Matrix(matrix3)).printing()
        2 4
        2 4
        >>> Matrix(matrix1) + Matrix(matrix4)
        'Нельзя складывать матрицы разных размерностей!'
        >>> Matrix(matrix1) + Matrix(matrix2)
        'Нельзя складывать матрицы разных размерностей!'
        """
        if self.__matrix_cols != other.__matrix_cols or self.__matrix_rows != other.__matrix_rows:
            return 'Нельзя складывать матрицы разных размерностей!'

        result_matrix = []

        for i in range(self.__matrix_cols):
            result_matrix.append([])
            for j in range(self.__matrix_rows):
                result_matrix[i].append(self.__matrix[i][j] + other.__matrix[i][j])

        return Matrix(result_matrix)

    def __mul__(self, other):
        """
        >>> (Matrix(matrix1) * Matrix(matrix3)).printing()
        3 6
        3 6
        >>> (Matrix(matrix4) * Matrix(matrix5)).printing()
        22 28
        49 64
        >>> Matrix(matrix1) * Matrix(matrix5)
        'Произведение двух матриц возможно только в том случае,когда число столбцов матрицы 1 совпадает с числом строк матрицы 2'
        >>> Matrix(matrix1) * Matrix(matrix2)
        'Произведение двух матриц возможно только в том случае,когда число столбцов матрицы 1 совпадает с числом строк матрицы 2'
        """
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
        """
        >>> print(Matrix(matrix1))
        Параметры матрицы:
        - количество строк: 2
        - количество столбцов: 2
        <BLANKLINE>
        >>> print(Matrix(matrix2))
        Параметры матрицы:
        - количество строк: 1
        - количество столбцов: 0
        <BLANKLINE>
        """
        return f'Параметры матрицы:\n' \
               f'- количество строк: {self.__matrix_cols}\n' \
               f'- количество столбцов: {self.__matrix_rows}\n'

    def __repr__(self):
        """
        >>> print(repr(Matrix(matrix1)))
        Matrix([[1, 2], [1, 2]])
        >>> print(repr(Matrix(matrix2)))
        Matrix([[]])
        """
        return f'Matrix({self.__matrix})'


if __name__ == '__main__':
    doctest.testmod(verbose=True)
