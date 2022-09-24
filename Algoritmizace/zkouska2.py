answers = []


class VrcholBinStromu:
    """třída pro reprezentaci vrcholu binárního stromu"""
    def __init__(self, info=None, levy=None, pravy=None):
        self.info = info      # data
        self.levy = levy      # levé dítě
        self.pravy = pravy    # pravé dítě

    # Traverse postorder
    def traversePostOrder(self):
        soucet = 0  # soucet of childs
        is_vr = False  # is vrchol. If it is then write to answer soucet of subtree

        if self.levy:
            is_vr = True
            soucet += self.levy.traversePostOrder()
        else:
            if self.pravy:
                self.pravy.traversePostOrder()
            else:
                soucet += self.info
                answers.append(self.info)

        if self.pravy:
            is_vr = True
            soucet += self.pravy.traversePostOrder()
        else:
            if self.levy:
                self.levy.traversePostOrder()
            else:
                soucet += self.info

        if not is_vr:
            soucet = int(soucet // 2)
        else:
            answers.append(soucet)
        return soucet


def minListy(koren : VrcholBinStromu) -> int:
    """
    koren : kořen zadaného binárního stromu
    vrátí : minimální součet hodnot listů podstromu
    """
    koren.traversePostOrder()
    ans = min(answers[:-1])
    return ans


root = VrcholBinStromu(0)

root.levy = VrcholBinStromu(1)
root.pravy = VrcholBinStromu(2)

root.levy.levy = VrcholBinStromu(3)
root.levy.pravy = VrcholBinStromu(5)

root.pravy.levy = VrcholBinStromu(4)
root.pravy.pravy = VrcholBinStromu(6)

root.levy.levy.levy = VrcholBinStromu(7)
root.levy.levy.pravy = VrcholBinStromu(9)

print(minListy(root))
print(answers)