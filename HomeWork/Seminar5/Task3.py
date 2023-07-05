# Создайте функцию генератор чисел Фибоначчи (см. Википедию).
def fibonaci(a):
    a1, a2 = 1, 1
    print(a1, a2, end=" " )
    for i in range(a + 1):
        yield a1+a2
        a1, a2 = a2, a1+a2

print(*fibonaci(10))