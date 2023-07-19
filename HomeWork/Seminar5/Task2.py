#Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names: list[str] = ["Andrey", "Yaroslav", "Ilariya"]
salaries: list[int] = [3000, 1000, 2500]
bonuses: list[str] = ["11.5%", "2.5%", "22.5%"]

print({name: (salary * float(bonus[:-1])/100) for name, salary, bonus in zip(names, salaries, bonuses)})