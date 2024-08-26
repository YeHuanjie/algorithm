# coding=utf-8
# Stack
# LIFO: last in first out


class Stack:
    # can be coded with (1)sequential table or (2)link list
    def __init__(self):
        self.__list = []
        # private

    def push(self, item):
        # add item
        self.__list.append(item)
        # O(1) better
        # bottom for sequential table but top for linklist

        # self.__list.insert(0, item)
        # O(n)

    def pop(self):
        # get item
        return self.__list.pop()
        # O(1)

        # self.__list.pop(0)
        # O(n)

    def peek(self):
        # return the top item
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list == []
        # return not self.__list

    def size(self):
        # num of items
        return len(self.__list)


if __name__ == "__main__":
    NewStack = Stack()
    print(NewStack.is_empty())
    NewStack.push(1)
    NewStack.push(2)
    NewStack.push(3)
    NewStack.push(4)
    print(NewStack.pop())
    print(NewStack.pop())
    print(NewStack.size())
    print(NewStack.peek())
    print(NewStack.is_empty())
