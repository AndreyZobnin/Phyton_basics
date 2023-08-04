"""
Задание №8 с семинара
Погружение в Python | Коллекции
✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

friends_items = {'Андрей': ('рюкзак', 'спички', 'туалетная бумага', 'котелок', 'сосиски', 'хлеб', 'вода'),
                 'Дмитрий': ('рюкзак', 'очки', 'сосиски', 'спички', 'уголь', 'палатка', 'карта'),
                 'Олег': ('очки', 'мяч', 'рюкзак', 'планшет', 'плавки', 'пиво', 'вода')}


def all_items(friend_items: dict[str, tuple]) -> list:
    all_items_set = set()
    for _, value in friend_items.items():
        all_items_set |= set(value)
    print(f'Вещи, которые взяли все три друга вместе:\n{sorted(all_items_set)}\n')
    return sorted(all_items_set)


def unique_friend_items(friend_items: dict[str, tuple]) -> dict[str]:
    unique_items_dict = dict()
    for key, value in friend_items.items():
        result = set(value)
        for key_tmp, value_tmp in friend_items.items():
            if key != key_tmp:
                result -= set(value_tmp)
        unique_items_dict.update({key: sorted(result)})
        print(f'Особые вещи, которые взял {key}: {sorted(result)}')
    return unique_items_dict


def friend_without_items(friend_items: dict[str, tuple]) -> dict[str]:
    without_items_dict = dict()
    for key, value in friend_items.items():
        result = set()
        count = 1
        for key_tmp, value_tmp in friend_items.items():
            if key != key_tmp:
                if count == 1:
                    result = set(value_tmp)
                else:
                    result &= set(value_tmp)
                count += 1
        for element in sorted(result):
            if element not in value:
                print(f'У друга {key} нет {element}, а у остальных есть!')
                without_items_dict.update({key: element})
    return without_items_dict


all_items(friends_items)
unique_friend_items(friends_items)
friend_without_items(friends_items)
