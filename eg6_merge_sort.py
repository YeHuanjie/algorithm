# coding=utf-8
# Merge Sort
# best O(nlogn) worst O(nlogn)
# [x0] [x1] [x2] [x3] [x4] [x5]
# [x0 x1] [x2 x3] [x4 x5] -- O(n)
# [x0 x1 x2 x3] [x4 x5] -- O(n)
# [x0 x1 x2 x3 x4 x5] -- O(n)
# total logn steps


def merge_sort(inlist):
    n = len(inlist)
    if n <= 1:
        out_list = inlist
        return out_list
    mid = n // 2
    left = merge_sort(inlist[:mid])
    right = merge_sort(inlist[mid:])
    out_list = merge(left, right)
    return out_list


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result


if __name__ == '__main__':
    unsort = [9, 8, 5, 6, 7, 1, 4, 3, 2]
    sort = merge_sort(unsort)
    print(sort)
