# coding=utf-8
# Selection Sort
# best O(n ** 2) worst O(n ** 2)


def selection_sort(inlist):
    for j in range(len(inlist)-1):
        min_index = j
        for i in range(j+1, len(inlist)):
            if inlist[i] < inlist[min_index]:
                min_index = i
        inlist[j], inlist[min_index] = inlist[min_index], inlist[j]
    return inlist


if __name__ == '__main__':
    unsort = [9, 8, 5, 6, 7, 1, 4, 3, 2]
    sort = selection_sort(unsort)
    print(sort)
