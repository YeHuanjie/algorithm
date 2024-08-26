# coding=utf-8
# SingleCycleLinkList


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList:
    def __init__(self, node=None):
        self.head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        if self.is_empty():
            return 0
        else:
            count = 1
            # start with count = 1
            while cur.next != self.head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        cur = self.head
        if self.is_empty():
            return
        else:
            while cur.next != self.head:
                print(cur.elem, end=" ")
                cur = cur.next
            print(cur.elem)
            # print the last node

    def add(self, item):
        # add item on the top of linklist
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head
            self.head = node
            cur.next = node

    def append(self, item):
        # add item on the bottom of linklist
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head
            cur.next = node

    def insert(self, pos, item):
        # param pos start from 0
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.head
            count = 0
            while count < (pos - 1):
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return
        if self.length() == 1:
            self.head = None
            return
        pre = None
        cur = self.head
        while cur.next != self.head:
            if cur.elem == item:
                if cur == self.head:
                    # remove the top node
                    # find the last node first
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    self.head = cur.next
                    last.next = self.head
                else:
                    # remove the mid node
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # remove the last node
        if cur.elem == item:
            pre.next = cur.next

    def search(self, item):
        cur = self.head
        if self.is_empty():
            return False
        while cur.next != self.head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        # the last node
        return False


if __name__ == "__main__":
    NewLinkList = SingleCycleLinkList()
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
    NewLinkList.remove(100)
    print(NewLinkList.length())
    NewLinkList.travel()
