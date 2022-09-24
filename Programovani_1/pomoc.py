# Поиск мин глубины листа и остальных листьев на том же уровне

class Vertex:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def min_deep_of_leaf(root : Vertex) -> (int, int):
    ans = [232323, 1]

    def preord(root, list):
        nonlocal ans
        if root.left is None and root.right is None:
            if list < ans[0]:
                ans[0], ans[1] = list, 1
            elif list <= ans[0]:
                ans[0], ans[1] = list, ans[1] + 1
        if root.left is not None:
            preord(root.left, list+1)
        if root.right is not None:
            preord(root.right, list+1)

    preord(root, 0)
    return tuple(ans)


root = Vertex(0)

root.left = Vertex(1)
root.right = Vertex(2)

root.left.left = Vertex(3)
root.left.right = Vertex(5)

root.right.left = Vertex(4)
root.right.right = Vertex(6)

root.left.left.left = Vertex(7)
root.left.left.right = Vertex(9)


print(min_deep_of_leaf(root))
