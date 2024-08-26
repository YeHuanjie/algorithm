# coding=utf-8
# Queue
# FIFO: first in first out


class Queue:
    # can be coded with (1)sequential list or (2)link list
    def __init__(self):
        self.__list = []
        # private

    def enqueue(self, item):
        # add item into the queue
        self.__list.insert(0, item)
        # O(n)

        # self.__list.append(item)
        # O(1)

    def dequeue(self):
        # get item out the queue
        return self.__list.pop()
        # O(1)

        # return self.__list.pop(0)
        # O(n)

    def is_empty(self):
        return self.__list == []
        # return not self.__list

    def size(self):
        # num of items
        return len(self.__list)


if __name__ == "__main__":
    NewStack = Queue()
    print(NewStack.is_empty())
    NewStack.enqueue(1)
    NewStack.enqueue(2)
    NewStack.enqueue(3)
    NewStack.enqueue(4)
    print(NewStack.dequeue())
    print(NewStack.dequeue())
    print(NewStack.size())
    print(NewStack.is_empty())
