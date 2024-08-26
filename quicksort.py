# coding=utf-8
def quicksort(lists):
    if len(lists) <= 1:
        return lists
    else:
        base = lists[0]
        less = [i for i in lists[1:] if i <= base]
        more = [i for i in lists[1:] if i > base]
        return quicksort(less) + [base] + quicksort(more)


print(quicksort([2, 3, 5, 1, 9]))
