#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

items = { 'Консервы': 3,
                   'Вода': 5,
                   'Палатка': 1,
                   'Лодка': 5,
                   'Рыболовные принадлежности': 3,
                   'Инструмент': 3,
                   'Ноутбук': 5,
                   'Настроение': 0}
backpack_volume = 5
result = []
for elements in items:
    if backpack_volume  > items[elements]:
        result.append(elements)
        backpack_volume  = backpack_volume  - int(items[elements])
    else: break
print(result)