import pytest

from source import Matrix


@pytest.fixture
def matrix1():
    return [[1, 2], [1, 2]]


@pytest.fixture
def matrix2():
    return [[]]


@pytest.fixture
def matrix3():
    return [[1, 2], [1, 2]]


@pytest.fixture
def matrix4():
    return [[1, 2, 3], [4, 5, 6]]


@pytest.fixture
def matrix5():
    return [[1, 2], [3, 4], [5, 6]]


# def test_all_items(dict1, dict2):
#     assert all_items(dict1) == ['item_a', 'item_b', 'item_c', 'item_d', 'item_e']
#     assert all_items(dict2) == []
def test_sum_matrix_elements(matrix1, matrix2):
    assert Matrix(matrix1).sum_elements() == 6
    assert Matrix(matrix2).sum_elements() == 0


def test_equals_of_matrix(matrix1, matrix2, matrix3):
    assert Matrix(matrix1) != Matrix(matrix2)
    assert Matrix(matrix1) == Matrix(matrix3)
    assert Matrix(matrix2) != Matrix(matrix3)


def test_not_equals_matrix(matrix1, matrix2, matrix3):
    assert Matrix(matrix1) > Matrix(matrix2)
    assert Matrix(matrix1) >= Matrix(matrix3)
    assert Matrix(matrix2) < Matrix(matrix3)
    assert Matrix(matrix1) <= Matrix(matrix3)


def test_matrix_sum(matrix1, matrix2, matrix3, matrix4):
    assert Matrix(matrix1) + Matrix(matrix3) == Matrix([[2, 4], [2, 4]])
    assert Matrix(matrix1) + Matrix(matrix4) == 'Нельзя складывать матрицы разных размерностей!'
    assert Matrix(matrix1) + Matrix(matrix2) == 'Нельзя складывать матрицы разных размерностей!'


def test_matrix_mult(matrix1, matrix2, matrix3, matrix4, matrix5):
    assert Matrix(matrix1) * Matrix(matrix3) == Matrix([[3, 6], [3, 6]])
    assert Matrix(matrix4) * Matrix(matrix5) == Matrix([[22, 28], [49, 64]])
    assert Matrix(matrix1) * Matrix(matrix5) == 'Произведение двух матриц возможно только в том случае,' \
                                                'когда число столбцов матрицы 1 совпадает с числом строк матрицы 2'
    assert Matrix(matrix1) * Matrix(matrix2) == 'Произведение двух матриц возможно только в том случае,' \
                                                'когда число столбцов матрицы 1 совпадает с числом строк матрицы 2'


if __name__ == '__main__':
    pytest.main(['-vv'])
