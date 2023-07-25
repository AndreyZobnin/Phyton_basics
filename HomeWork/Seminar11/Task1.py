"""Добавьте ко всем задачам с семинара строки документации и методы вывода
информации на печать"""

from time import time


class MyString(str):
    """MyString - класс, которому доступны все возможности str.
    В экземплярах класса дополнительно хранятся:\n
    - имя автора строки (author_name)\n
    - время создания (time_created)"""

    def __init__(self, value: str, author_name: str):
        self.value = value

    def __new__(cls, value: str, author_name: str):
        """Переопределение класса str"""
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.time_created = time()
        print(f'Класс {cls} создан')
        return instance

    def __str__(self):
        return f'Имя автора: {self.author_name}, время создания: {self.time_created}'

    def __repr__(self) -> str:
        return f'MyString(\'{self.value}\', \'{self.author_name}\')'


class Archive:
    """Archive - класс, хранящий пару свойств (число (num) и строку (text)).\n
    При создании нового экземпляра класса, старые данные из ранее созданных
    экземпляров сохраняются в пару списков-архивов, которые также являются свойствами экземпляра
    """

    __instance = None

    def __init__(self, num: int, text: str):
        """Инициализация параметров num и text экземпляра класса"""
        self.num = num
        self.text = text

    def __new__(cls, *args, **kwargs):
        """Переопределение класса Object"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance

    def __str__(self):
        return f'Текст: {self.text}, число: {self.num}, ' \
               f'архив текста: {self.text_list}, архив чисел: {self.num_list}'

    def __repr__(self) -> str:
        return f'Archive({self.num}, \'{self.text}\')'


class Rectangle:
    """Класс создания прямоугольников и работы с ними"""
    def __init__(self, width: float, height: float = None):
        """Инициализация параметров width и height экземпляра класса"""
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def calc_perimeter(self):
        """Вычисление периметра прямоугольника"""
        return 2 * (self.width + self.height)

    def calc_area(self):
        """Вычисление площади прямоугольника"""
        return self.width * self.height

    def __add__(self, other):
        """Сложение двух прямоугольников"""
        perimeter = self.calc_perimeter() + other.calc_perimeter()
        width = self.width + other._width
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """Вычитание двух прямоугольников"""
        width = abs(self.width - other._width)
        perimeter = abs(self.calc_perimeter() - other.calc_perimeter())
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __str__(self):
        return f'Периметр = {self.calc_perimeter()}, ширина = {self.width}, длина = {self.height}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __eq__(self, other):
        """Сравнение площадей двух прямоугольников на равенство"""
        return self.calc_area() == other.calc_area()

    def __lt__(self, other):
        """Сравнение площадей двух прямоугольников на строго меньше"""
        return self.calc_area() < other.calc_area()

    def __le__(self, other):
        """Сравнение площадей двух прямоугольников на меньше или равно"""
        return self.calc_area() <= other.calc_area()


if __name__ == '__main__':
    my_str = MyString('Everybody, hello!', 'It`s me')
    print(my_str)
    print(f'{my_str = }')
    print()

    arch1 = Archive(1, 'what?')
    arch2 = Archive(2, 'something...')
    print(arch2)
    print(f'{arch2 = }')
    print()

    rect = Rectangle(5, 7)
    print(rect)
    print(f'{rect = }')
    print()

    # print(help(MyString))
    print(MyString.__doc__ + '\n')
    # print(help(Archive))
    print(Archive.__doc__ + '\n')
    print(Rectangle.calc_perimeter.__doc__ + '\n')
    print(help(Rectangle))