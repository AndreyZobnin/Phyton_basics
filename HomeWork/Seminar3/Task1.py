#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def report_list(array: list[int]) -> list[int]:
    result = set()
    for el in array:
        counter = array.count(el)
        if counter > 1:
            result.add(el)
    return list(result)
print(report_list([5, 5, 6, 6, 8, 8, 9, 1, 3,]))