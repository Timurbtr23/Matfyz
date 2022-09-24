class Node:
    def __init__(self, value, left, right):
        self.val = value
        self.left = left
        self.right = right


class TreeSet:

    def __init__(self):
        self.root = None
        self.size_of_tree = 0

    def contains(self, x):
        n = self.root
        while n is not None:
            if x == n.val:
                return True
            if x < n.val:
                n = n.left
            else:
                n = n.right
        return False

    def add(self, x):
        new_node = Node(x, None, None)
        n = self.root

        if n is None:
            self.root = new_node
            self.size_of_tree += 1
            return

        if self.contains(x):
            return

        while True:
            if x == n.val:
                self.size_of_tree += 1
                return
            elif x < n.val:
                if n.left is None:
                    n.left = new_node
                    self.size_of_tree += 1
                    return
                else:
                    n = n.left
            else:
                if n.right is None:
                    n.right = new_node
                    self.size_of_tree += 1
                    return
                else:
                    n = n.right

    def remove(self, x):
        if self.root is not None:
            self.size_of_tree -= 1
            self.root = self.deleteNode(self.root, x)

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def deleteNode(self, root, key, s=1):
        if root is None:
            return root

        # Find the node to be deleted
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # If the node is with only one child or no child
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # If the node has two children,
            # place the inorder successor in position of the node to be deleted
            temp = self.minValueNode(root.right)

            root.val = temp.val

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)
        return root

    def min(self):
        n = self.root

        if n is None:
            return

        while True:
            if n.left is not None:
                n = n.left
            else:
                return n.val

    def max(self):
        n = self.root

        if n is None:
            return

        while True:
            if n.right is not None:
                n = n.right
            else:
                return n.val

    def size(self):
        return self.size_of_tree

    def count(self, lo, hi):
        n = self.root
        countik = 0

        if n is None:
            return None

        while True:
            if lo == n.val:
                countik += 1
                break
            elif lo < n.val:
                if n.left is None:
                    countik += 1
                    break
                n = n.left
                countik += 1
            else:
                if n.right is None:
                    countik += 1
                    break
                n = n.right
                countik += 1

        while True:
            if hi == n.val:
                countik += 1
                break
            elif hi < n.val:
                if n.left is None:
                    countik += 1
                    break
                n = n.left
                countik += 1
            else:
                if n.right is None:
                    countik += 1
                    break
                n = n.right
                countik += 1

        return countik + 1

    def ceil(self, x):
        n = self.root

        if n is None:
            return None

        while True:
            if x == n.val:
                if n.right is None:
                    return None
                else:
                    n = n.right
                    while True:
                        if n.left is not None:
                            n = n.left
                        else:
                            return n.val
            elif x < n.val:
                if n.left is None:
                    return None
                else:
                    n = n.left
            else:
                if n.right is None:
                    return None
                else:
                    n = n.right

    def floor(self, x):
        n = self.root

        if n is None:
            return None

        while True:
            if x == n.val:
                if n.left is None:
                    return None
                else:
                    n = n.left
                    while True:
                        if n.right is not None:
                            n = n.right
                        else:
                            return n.val
            elif x < n.val:
                if n.left is None:
                    return None
                else:
                    n = n.left
            else:
                if n.right is None:
                    return None
                else:
                    n = n.right

    def avg_tree_depth(self):
        pass


def sample6():
    t = TreeSet()
    for x in [10, 3, 20, 2, 6, 15, 23, 5, 8, 18]:
        t.add(x)
    print('t.count(7, 18) =', t.count(7, 18))
    print('t.count(30, 50) =', t.count(30, 50))
    print('t.ceil(1) =', t.ceil(10))
    print('t.ceil(7) =', t.ceil(7))
    print('t.ceil(9) =', t.ceil(9))
    print('t.floor(7) =', t.floor(7))
    print('t.floor(17) =', t.floor(17))


sample6()
