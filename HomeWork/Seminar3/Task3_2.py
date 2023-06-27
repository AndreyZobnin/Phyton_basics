#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Верните все возможные варианты комплектации рюкзака.

backpack_volume = int(input('Какая максимальная грузоподъемность вашего рюкзака: '))
list_equipment = { 'Консервы': 3,
                   'Вода': 5,
                   'Палатка': 1,
                   'Лодка': 5,
                   'Рыболовные принадлежности': 3,
                   'Инструмент': 3,
                   'Ноутбук': 5,
                   'Настроение': 0}

def List_sort (some_set: set):
    global global_list
    if len (some_set) == 1:
        return some_set
    else:
        for item in some_set:
            new_set = some_set.copy()
            new_set.remove(item)
            global_list.add(tuple(List_sort(new_set)))
    return some_set

list_equipment = dict(sorted(list_equipment.items(), key=lambda x: x[1]))
global_list = {tuple(list_equipment)}
List_sort(set(list_equipment))

print(f'В рюкзак грузоподъемностью {backpack_volume} кг может влезть:')

for stack in global_list:
    sum_stack = 0
    for item in stack:
        sum_stack += list_equipment.get(item)
        if sum_stack > backpack_volume:
            break
        else:
            print(*stack, 'весом', sum_stack, 'кг')