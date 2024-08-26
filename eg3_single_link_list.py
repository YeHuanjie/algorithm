# coding=utf-8
# SingleLinkList


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList:
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.head
        while cur:
            print(cur.elem, end=" ")
            cur = cur.next
        print('')

    def add(self, item):
        # add item on the top of linklist
        node = Node(item)
        node.next = self.head
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
        pre = None
        cur = self.head
        while cur:
            if cur.elem == item:
                # remove the top node
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self.head
        while cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    NewLinkList = SingleLinkList()
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
