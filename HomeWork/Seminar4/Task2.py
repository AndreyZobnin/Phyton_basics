#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.
def hash_dictions(**kwargs):
    frends = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        frends[v] = k
    return frends


print(hash_dictions(Work='first', home={'vasiliy': 2, 'Ivan': 3}, frends=['andrey', 'stas', 'fedor'],
                     market={'sveta', 'roma'}))
