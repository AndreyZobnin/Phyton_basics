import unittest

from source import all_items, unique_friend_items, friend_without_items


class TestFriendsItems(unittest.TestCase):
    def setUp(self) -> None:
        self.dict1 = {'user1': ('item_a', 'item_b'), 'user2': ('item_a', 'item_c'), 'user3': ('item_d', 'item_e')}
        self.dict2 = dict()

    def test_all_items(self):
        self.assertEquals(all_items(self.dict1), ['item_a', 'item_b', 'item_c', 'item_d', 'item_e'])
        self.assertEquals(all_items(self.dict2), [])

    def test_unique_friend_items(self):
        self.assertEquals(unique_friend_items(self.dict1),
                          {'user1': ['item_b'], 'user2': ['item_c'], 'user3': ['item_d', 'item_e']})
        self.assertEquals(unique_friend_items(self.dict2), {})

    def test_friend_without_items(self):
        self.assertEquals(friend_without_items(self.dict1), {'user3': 'item_a'})
        self.assertEquals(friend_without_items(self.dict2), {})


if __name__ == '__main__':
    unittest.main(verbosity=2)
