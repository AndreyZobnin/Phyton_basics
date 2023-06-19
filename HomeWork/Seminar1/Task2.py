num = int(input('Введите число от 0 до 100000: '))
if num > 100000 or num < 1:
    print ('Введите верное число!')
    quit()
k = 0
for i in range (2, num // 2 + 1):
    if (num % i == 0):
        k = k + 1
if (k <= 0):
    print('Простое число!')
else:
    print('Число не является простым!')