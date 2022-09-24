class VrcholBinStromu:
    """třída pro reprezentaci vrcholu binárního stromu"""

    def __init__(self, info=None, levy=None, pravy=None):
        self.info = info  # data
        self.levy = levy  # levé dítě
        self.pravy = pravy  # pravé dítě


def minListy(root):
    mini = float('inf')

    def findSum(root, temp):
        if root.levy == None and root.pravy == None:
            temp.append(root.info)
        if root.levy != None:
            findSum(root.levy, temp)
        if root.pravy != None:
            findSum(root.pravy, temp)

    def DFS(root):
        nonlocal mini
        if root.levy == None and root.pravy == None:
            findSum(root, temp := [])
            if mini > sum(temp): mini = sum(temp)
        if root.levy != None:
            findSum(root, temp := [])
            if mini > sum(temp): mini = sum(temp)
            DFS(root.levy)
        if root.pravy != None:
            findSum(root, temp := [])
            if mini > sum(temp): mini = sum(temp)
            DFS(root.pravy)

    return [mini for _ in [1] if not DFS(root)][0]

root = VrcholBinStromu(0)

root.levy = VrcholBinStromu(1)
root.pravy = VrcholBinStromu(2)

root.levy.levy = VrcholBinStromu(3)
root.levy.pravy = VrcholBinStromu(5)

root.pravy.levy = VrcholBinStromu(4)
root.pravy.pravy = VrcholBinStromu(6)

root.levy.levy.levy = VrcholBinStromu(-7)
root.levy.levy.pravy = VrcholBinStromu(-9)

print(minListy(root))
