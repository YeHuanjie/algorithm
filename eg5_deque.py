# coding=utf-8
# Deque：Double ended queue
# front can push and pop
# rear can push and pop


class Deque:
    # can be coded with (1)sequential list or (2)link list
    def __init__(self):
        self.__list = []
        # private

    def add_front(self, item):
        # add item in the front of the queue
        self.__list.insert(0, item)

    def add_rear(self, item):
        # add item in the rear of the queue
        self.__list.append(item)

    def remove_front(self):
        # get item in the front of the queue
        return self.__list.pop(0)

    def remove_rear(self):
        # get item in the rear of the queue
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []
        # return not self.__list

    def size(self):
        # num of items
        return len(self.__list)


if __name__ == "__main__":
    NewStack = Deque()
    print(NewStack.is_empty())
    NewStack.add_front(1)
    NewStack.add_front(2)
    NewStack.add_front(3)
    NewStack.add_front(4)
    NewStack.add_rear(5)
    NewStack.add_rear(6)
    NewStack.add_rear(7)
    NewStack.add_rear(8)
    print(NewStack.remove_front())
    print(NewStack.remove_front())
    print(NewStack.remove_rear())
    print(NewStack.remove_rear())
    print(NewStack.size())
    print(NewStack.is_empty())
