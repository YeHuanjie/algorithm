# coding=utf-8
# Shell Sort ==> improved insert sort
# best O(?) depends on the gap ==> O(n ** 1.3) mathematically
# worst O(n ** 2)
# unstable


def shell_sort(inlist):
    gap = len(inlist) // 2
    # gap values vary according to different situation
    while gap >= 1:
        for j in range(gap, len(inlist)):
            for i in range(j, 0, -gap):
                if inlist[i] < inlist[i - gap]:
                    inlist[i - gap], inlist[i] = inlist[i], inlist[i - gap]
                else:
                    break
        gap //= 2
    return inlist


if __name__ == '__main__':
    unsort = [9, 8, 5, 6, 7, 1, 4, 3, 2]
    sort = shell_sort(unsort)
    print(sort)
