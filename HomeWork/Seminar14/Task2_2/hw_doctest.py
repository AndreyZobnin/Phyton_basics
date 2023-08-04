import doctest

dict1 = {'user1': ('item_a', 'item_b'), 'user2': ('item_a', 'item_c'), 'user3': ('item_d', 'item_e')}
dict2 = dict()


def all_items(friend_items: dict[str, tuple]) -> list:
    """
    >>> all_items(dict1)
    Вещи, которые взяли все три друга вместе:
    ['item_a', 'item_b', 'item_c', 'item_d', 'item_e']
    <BLANKLINE>
    ['item_a', 'item_b', 'item_c', 'item_d', 'item_e']
    >>> all_items(dict2)
    Вещи, которые взяли все три друга вместе:
    []
    <BLANKLINE>
    []
    """
    all_items_set = set()
    for _, value in friend_items.items():
        all_items_set |= set(value)
    print(f'Вещи, которые взяли все три друга вместе:\n{sorted(all_items_set)}\n')
    return sorted(all_items_set)


def unique_friend_items(friend_items: dict[str, tuple]) -> dict[str]:
    """
        >>> unique_friend_items(dict1)
        Особые вещи, которые взял user1: ['item_b']
        Особые вещи, которые взял user2: ['item_c']
        Особые вещи, которые взял user3: ['item_d', 'item_e']
        {'user1': ['item_b'], 'user2': ['item_c'], 'user3': ['item_d', 'item_e']}
        >>> unique_friend_items(dict2)
        {}

        """
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
    """
    >>> friend_without_items(dict1)
    У друга user3 нет item_a, а у остальных есть!
    {'user3': 'item_a'}
    >>> friend_without_items(dict2)
    {}
    """
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


if __name__ == '__main__':
    doctest.testmod(verbose=True)
