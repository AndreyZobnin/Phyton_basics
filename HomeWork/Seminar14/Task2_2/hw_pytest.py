import pytest

from source import all_items, unique_friend_items, friend_without_items


@pytest.fixture
def dict1():
    return {'user1': ('item_a', 'item_b'), 'user2': ('item_a', 'item_c'), 'user3': ('item_d', 'item_e')}


@pytest.fixture
def dict2():
    return dict()


def test_all_items(dict1, dict2):
    assert all_items(dict1) == ['item_a', 'item_b', 'item_c', 'item_d', 'item_e']
    assert all_items(dict2) == []


def test_unique_friend_items(dict1, dict2):
    assert unique_friend_items(dict1) == {'user1': ['item_b'], 'user2': ['item_c'], 'user3': ['item_d', 'item_e']}
    assert unique_friend_items(dict2) == {}


def test_friend_without_items(dict1, dict2):
    assert friend_without_items(dict1) == {'user3': 'item_a'}
    assert friend_without_items(dict2) == {}


if __name__ == '__main__':
    pytest.main(['-vv'])
