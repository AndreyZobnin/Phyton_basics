""" Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним."""

from Seminar1.modules.input import num_input_check as num_input


def triangle_check(side_a, side_b, side_c):
    if side_a > 0 and side_b > 0 and side_c >0:
        if side_a > (side_b + side_c) or side_b > (side_a + side_c) or side_c > (side_a + side_b):
            print('Такой треугольник не существует')
        elif side_a == side_b == side_c:
            print('Этот треугольник равносторонний')
        elif side_a == side_b or side_a == side_c or side_b == side_c:
            print('Этот треугольник равнобедренный')
        else:
            print('Этот треугольник разносторонний')

    else:
        print('Введена отрицательная сторона треугольника')

    print()


def enter_triangle():
    a = num_input('Введите сторону a', 'float')
    b = num_input('Введите сторону b', 'float')
    c = num_input('Введите сторону c', 'float')

    triangle_check(a, b, c)
