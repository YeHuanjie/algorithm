# coding=utf-8
# Bubble Sort
# best O(n) worst O(n ** 2)


def bubble_sort(inlist):
    # can sort sequential table or link list
    # we take sequential table(list) as an example
    # always O(n ** 2)
    for j in range(len(inlist)-1):
        # n = len(inlist)
        # sort n-1 times
        for i in range(len(inlist)-1-j):
            # sort list once
            if inlist[i] > inlist[i+1]:
                inlist[i], inlist[i+1] = inlist[i+1], inlist[i]
    return inlist


def improved_bubble_sort(inlist):
    # can sort sequential table or link list
    # we take sequential table(list) as an example
    # worst O(n ** 2)
    # best O(n) ==> the list no need to sort
    for j in range(len(inlist)-1):
        # n = len(inlist)
        # sort n-1 times
        count = 0
        for i in range(len(inlist)-1-j):
            # sort list once
            if inlist[i] > inlist[i+1]:
                inlist[i], inlist[i+1] = inlist[i+1], inlist[i]
                count += 1
        if count == 0:
            print("no need to sort")
            return inlist
    return inlist


if __name__ == '__main__':
    unsort = [9, 8, 5, 6, 7, 1, 4, 3, 2]
    sort = bubble_sort(unsort)
    print(sort)
    sort1 = improved_bubble_sort(sort)
    print(sort1)

