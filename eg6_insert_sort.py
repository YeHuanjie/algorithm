# coding=utf-8
# Insert Sort
# best O(n) worst O(n ** 2)


def insert_sort(inlist):
    for j in range(1, len(inlist)):
        # j = 1...n-1
        for i in range(j, 0, -1):
            if inlist[i] < inlist[i-1]:
                inlist[i-1], inlist[i] = inlist[i], inlist[i-1]
            else:
                break
    return inlist


if __name__ == '__main__':
    unsort = [9, 8, 5, 6, 7, 1, 4, 3, 2]
    sort = insert_sort(unsort)
    print(sort)
