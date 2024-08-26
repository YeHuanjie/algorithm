# coding=utf-8
# best O(1) best O(logn)


def binary_search(lists, item):
    # non recursive version
    low = 0
    high = len(lists) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = lists[mid]
        if guess == item:
            return True
        elif guess <= item:
            low = mid + 1
        else:
            high = mid - 1
    return False


def recursive_binary_search(lists, item):
    # recursive version
    if len(lists) == 0:
        return False
    else:
        mid = len(lists) // 2
        guess = lists[mid]
        if guess == item:
            return True
        elif guess <= item:
            return recursive_binary_search(lists[mid + 1:], item)
        else:
            return recursive_binary_search(lists[:mid], item)


my_list = [0, 1, 2, 3, 4, 5]
print(binary_search(my_list, 6))
print(binary_search(my_list, 1))
print(recursive_binary_search(my_list, 6))
print(recursive_binary_search(my_list, 1))
