# coding=utf-8
# Quick Sort ********** very important **********
# best O(nlogn) worst O(n ** 2)
# best -- quick_sort every mid_value -- O(n)
#      -- mid_value divides list into 2 even sub_lists every time
#      -- list obtains n items, finally each sub_list contain 1 item
#      -- need logn steps
#      -- O(nlogn)
# worst -- quick_sort every mid_value -- O(n)
#       -- mid_value divides list into sub_list1 with 1 item and sub_list2 with n-1 items
#       -- need n steps
#       -- O(n ** 2)


def quick_sort(inlist, start, end):
    if start >= end:
        return

    mid_value = inlist[start]
    low_index = start
    high_index = end

    while low_index < high_index:
        while low_index < high_index and inlist[high_index] >= mid_value:
            high_index -= 1
        inlist[low_index] = inlist[high_index]

        while low_index < high_index and inlist[low_index] < mid_value:
            low_index += 1
        inlist[high_index] = inlist[low_index]

    # low_index = high_index
    inlist[low_index] = mid_value

    quick_sort(inlist, start, low_index - 1)
    quick_sort(inlist, low_index + 1, end)
    return inlist


if __name__ == '__main__':
    unsort = [9, 8, 5, 6, 7, 1, 4, 3, 2]
    sort = quick_sort(unsort, 0, len(unsort)-1)
    print(sort)
