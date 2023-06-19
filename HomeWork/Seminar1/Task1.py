a = int(input('Введите длину стороны А '))
b = int(input('Введите длину стороны B '))
c = int(input('Введите сторону длины С '))
if c + a > b and b + c > a and a + b > c:
    print('Это треугольник')
    if a != b and b != c and c != a:
        print('Треугольник разносторонний')
    if a == b or b == c or c == a:
        print('треугольник  равнобедренным')
    if a == b == c:
        print('треугольник равносторонним')
else:
    print('Это не треугольник')