"""Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода. Например,
нельзя создавать прямоугольник со сторонами отрицательной длины."""

from scripts.Task1 import StaffInfo
from scripts.Task2 import checking_digits_count

if __name__ == '__main__':
    staff_names = ['Андрей', 'Тимофей', 'Наджат', 'Соня', 'Наташа']
    staff_salaries = [35_320, 51_180, 18_120, 55_050, 48_500]
    staff_percents = ['15.20%', '10.32%', '5.50%', '0%', '20.00%']

    staff_info_1 = StaffInfo(staff_names, staff_salaries, staff_percents)
    print(f'Бонусы сотрудников:\n{staff_info_1.calc_bonuses()}')

    print(checking_digits_count())