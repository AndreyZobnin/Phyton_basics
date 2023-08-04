"""Задача №6 семинара 14.
На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта. Используйте фикстуры."""

import json

import pytest

from HomevorkPy.Seminar14.LecSem13.ex4 import UserData
from HomevorkPy.Seminar14.LecSem13.ex5 import Project
from HomevorkPy.Seminar14.LecSem13.ex6 import MyAccessEx, MyLevelEx

FILE = 'exit.json'


@pytest.fixture
def users_data():
    new_data = {
        UserData('Гном', 100, 1),
        UserData('Слон', 101, 2),
        UserData('Вон', 102, 2),
        UserData('Дром', 103, 3),
    }
    return new_data


@pytest.fixture
def high_level_user():
    return UserData('Гном', 100, 1)


@pytest.fixture
def new_low_level_user():
    return UserData('Слон', 105, 5)


def test_load_json(users_data):
    """Тестирование загрузки данных из файла json"""
    data = {
        1: {100: 'Гном'},
        2: {101: 'Слон', 102: 'Вон'},
        3: {103: 'Дром'}
    }
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    project1 = Project()
    test_result = project1.load_json(FILE)
    assert test_result == users_data


def test_enter_valid_user(high_level_user):
    """Тестирование входа в систему существующего пользователя"""
    new_pr = Project()
    new_pr.load_json(FILE)
    test_user = new_pr.enter('Гном', 100)
    assert test_user == high_level_user


def test_enter_invalid_user():
    """Тестирование входа в систему несуществующего пользователя"""
    new_pr = Project()
    new_pr.load_json(FILE)
    with pytest.raises(MyAccessEx, match=r'Пользователя с именем Максим и id 105 нет в системе! Доступ запрещён!'):
        new_pr.enter('Слон', 105)


def test_add_lower_level_user(new_low_level_user):
    """Тестирование добавления пользователя с более низким уровнем, чем у администратора"""
    new_pr = Project()
    new_pr.load_json(FILE)
    new_pr.enter('Гном', 100)
    new_user = new_pr.add_user('Слон', 105, 5)
    assert new_user == new_low_level_user


def test_add_higher_level_user():
    """Тестирование добавления пользователя с более высоким уровнем, чем у администратора"""
    new_pr = Project()
    new_pr.load_json(FILE)
    new_pr.enter('Вон', 103)
    with pytest.raises(MyLevelEx, match=r'Уровень доступа пользователя Иван - 1 '
                                        r'ниже уровня доступа администратора 3! Доступ запрещён!'):
        new_pr.add_user('Иван', 104, 1)


if __name__ == '__main__':
    pytest.main(['-vv'])
   