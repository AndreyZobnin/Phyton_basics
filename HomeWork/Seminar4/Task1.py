#Напишите функцию для транспонирования матрицы
def trsnsp_matrix(*a_list: list[[int]]) -> list[()] | str:
    transparent = True
    tmp = len(a_list[0])
    for a in list(a_list):
        if len(a) != tmp:
            transparent = False
    if transparent:
        return list(zip(*a_list))
    else:
        return 'Невозможно транспониировать матрицу'

print(trsnsp_matrix([1, 4, 6], [3, 3, 7]))

