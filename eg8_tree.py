# coding=utf-8
# Tree
# pre order + in order can rebuild the tree
# in order + post order can rebuild the tree
# pre order + post order can not rebuild the tree
# because in oder -- left child - root - right child
# in oder -- the root discriminate the left and the right
# pre and post order -- can not discriminate the left and the right


class Node:
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree:
    # binary tree
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            queue = list()
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                else:
                    queue.append(cur.lchild)

                if cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.rchild)

    def bfs(self):
        # breadth first search
        # level traversal
        if self.root is None:
            return
        else:
            queue = list()
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                print(cur.elem, end=' ')
                if cur.lchild is not None:
                    queue.append(cur.lchild)
                if cur.rchild is not None:
                    queue.append(cur.rchild)
            print('')

    def dfs_pre(self, node):
        # depth first search -- pre order
        # root - left child - right child
        if node is None:
            return
        print(node.elem)
        self.dfs_pre(node.lchild)
        self.dfs_pre(node.rchild)

    def dfs_in(self, node):
        # depth first search -- in order
        # left child - root - right child
        if node is None:
            return
        self.dfs_in(node.lchild)
        print(node.elem)
        self.dfs_in(node.rchild)

    def dfs_post(self, node):
        # depth first search -- post order
        # left child - right child - root
        if node is None:
            return
        self.dfs_post(node.lchild)
        self.dfs_post(node.rchild)
        print(node.elem)


if __name__ == "__main__":
    New = Tree()
    New.add(0)
    New.add(1)
    New.add(2)
    New.add(3)
    New.add(4)
    New.add(5)
    New.add(6)
    New.add(7)
    New.add(8)
    New.add(9)
    #              [0]
    #      [1              2]
    #  [3      4]     [5      6]
    # [7 8]  [9]
    New.bfs()
    print('\n')
    # 0 1 2 3 4 5 6 7 8 9
    New.dfs_pre(New.root)
    print('\n')
    # 0 1 3 7 8 4 9 2 5 6
    New.dfs_in(New.root)
    print('\n')
    # 7 3 8 1 9 4 0 5 2 6
    New.dfs_post(New.root)
    print('\n')
    # 7 8 3 9 4 1 5 6 2 0
