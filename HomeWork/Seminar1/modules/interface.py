from Seminar1.tasks import task1, task2, task3, task4, task5


def selection():
    while True:
        print(f'Выберите задачу:\n'
              '1. Ёлка\n'
              '2. Таблица умножения\n'
              '3. Существование треугольника\n'
              '4. Проверка, является ли число простым\n'
              '5. Угадывание числа\n'
              'Любая другая клавиша: выход из программы')

        exercises = input()

        match exercises:

            case '1':
                task1.draw_tree('Эта программа может нарисовать в консоли ёлку. Напишите количество рядов')
                menu_return()
                continue

            case '2':
                task2.mult_table()
                menu_return()
                continue

            case '3':
                task3.enter_triangle()
                menu_return()
                continue

            case '4':
                print('Эта программа определяет, является ли число простым или составным\n')
                task4.number_type_enter()
                menu_return()
                continue

            case '5':
                print('Ваша задача в этой программе - угадать число с 10 попыток\n')
                task5.guessing_game(task5.random_int_number())
                menu_return()
                continue

            case _:
                break


def menu_return():
    input('Для возврата в главное меню нажмите любую кнопку...')