# coding=utf-8
# Selection sort


def findsmallest(arr):
    smallest_index = 0
    smallest_value = arr[smallest_index]
    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_index = i
            smallest_value = arr[i]
    return smallest_index


def sortarr(arr):
    sortedarr = []
    for i in range(len(arr)):
        sortedarr.append(arr.pop(findsmallest(arr)))
    return sortedarr


print(sortarr([1, 5, 9, 3, 2, 7]))
