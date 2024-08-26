# coding=utf-8
# SingleDoubleLinkList
from eg3_single_link_list import SingleLinkList


class Node:
    def __init__(self, elem):
        self.prev = None
        self.elem = elem
        self.next = None


class DoubleLinkList(SingleLinkList):
    # same as single link list:
    # init // is_empty // length // travel // search

    # different with single link list
    def add(self, item):
        # add item on the top of linklist
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, item):
        # add item on the bottom of linklist
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        # param pos start from 0
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self.head
            count = 0
            while count < pos:
                cur = cur.next
                count += 1
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        cur = self.head
        while cur:
            if cur.elem == item:
                # remove the top node
                if cur == self.head:
                    self.head = cur.next
                    if cur.next:
                        # if link list only has one node: pass
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        # if remove the final node: pass
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


if __name__ == "__main__":
    NewLinkList = DoubleLinkList()
    print(NewLinkList.is_empty())
    print(NewLinkList.length())

    NewLinkList.append(1)
    print(NewLinkList.is_empty())
    print(NewLinkList.length())

    NewLinkList.append(2)
    NewLinkList.append(3)
    NewLinkList.append(4)
    NewLinkList.append(5)
    NewLinkList.append(6)
    NewLinkList.add(7)
    NewLinkList.insert(-1, 100)
    NewLinkList.insert(3, 9)
    NewLinkList.insert(20, 200)
    print(NewLinkList.is_empty())
    print(NewLinkList.length())
    NewLinkList.travel()

    print(NewLinkList.search(9))

    NewLinkList.remove(5)
    print(NewLinkList.length())
    NewLinkList.travel()
