# coding=utf-8
def recursion(num):
    if num == 1:
        return 1
    else:
        ans = num * recursion(num - 1)
    return ans


print(recursion(3))


def sumarr(arr):
    if len(arr) == 0:
        return 0
    else:
        ans = arr.pop(0) + sumarr(arr)
    return ans


print(sumarr([1, 2, 3, 4, 5, 6]))
