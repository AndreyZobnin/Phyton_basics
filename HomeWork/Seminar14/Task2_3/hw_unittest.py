import unittest

from source import Matrix


class TestMatrixActions(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix1 = [[1, 2], [1, 2]]
        self.matrix2 = [[]]
        self.matrix3 = [[1, 2], [1, 2]]
        self.matrix4 = [[1, 2, 3], [4, 5, 6]]
        self.matrix5 = [[1, 2], [3, 4], [5, 6]]

    def test_sum_matrix_elements(self):
        self.assertEquals(Matrix(self.matrix1).sum_elements(), 6)
        self.assertEquals(Matrix(self.matrix2).sum_elements(), 0)

    def test_equals_of_matrix(self):
        self.assertNotEquals(Matrix(self.matrix1), Matrix(self.matrix2))
        self.assertEquals(Matrix(self.matrix1), Matrix(self.matrix3))
        self.assertNotEquals(Matrix(self.matrix2), Matrix(self.matrix3))

    def test_not_equals_matrix(self):
        self.assertGreater(Matrix(self.matrix1), Matrix(self.matrix2))
        self.assertGreaterEqual(Matrix(self.matrix1), Matrix(self.matrix3))
        self.assertLess(Matrix(self.matrix2), Matrix(self.matrix3))
        self.assertLessEqual(Matrix(self.matrix1), Matrix(self.matrix3))

    def test_matrix_sum(self):
        self.assertEquals(Matrix(self.matrix1) + Matrix(self.matrix3), Matrix([[2, 4], [2, 4]]))
        self.assertEquals(Matrix(self.matrix1) + Matrix(self.matrix4), 'Нельзя складывать матрицы разных размерностей!')
        self.assertEquals(Matrix(self.matrix1) + Matrix(self.matrix2), 'Нельзя складывать матрицы разных размерностей!')

    def test_matrix_mult(self):
        self.assertEquals(Matrix(self.matrix1) * Matrix(self.matrix3), Matrix([[3, 6], [3, 6]]))
        self.assertEquals(Matrix(self.matrix4) * Matrix(self.matrix5), Matrix([[22, 28], [49, 64]]))
        self.assertEquals(Matrix(self.matrix1) * Matrix(self.matrix5),
                          'Произведение двух матриц возможно только в том случае,когда '
                          'число столбцов матрицы 1 совпадает с числом строк матрицы 2')
        self.assertEquals(Matrix(self.matrix1) * Matrix(self.matrix2),
                          'Произведение двух матриц возможно только в том случае,когда '
                          'число столбцов матрицы 1 совпадает с числом строк матрицы 2')


if __name__ == '__main__':
    unittest.main(verbosity=2)
