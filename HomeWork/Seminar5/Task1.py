# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
def kortej(s: str) -> tuple:
    *a, b = s.split("/")
    b, c = b.split(".")
    result = (a, b, c)
    return result

s = "C:/temp/wasya/GB/test.txt"
print(kortej(s))