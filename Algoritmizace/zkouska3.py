class VrcholBinStromu:
    def __init__(self, info):
        self.levy = None
        self.pravy = None
        self.info = info


def minHloubkaListu(koren : VrcholBinStromu) -> (int, int):
    ans = [232323, 1]

    def preord(koren, list):
        nonlocal ans
        if koren.levy is None and koren.pravy is None:
            if list < ans[0]:
                ans[0], ans[1] = list, 1
            elif list <= ans[0]:
                ans[0], ans[1] = list, ans[1] + 1
        if koren.levy is not None:
            preord(koren.levy, list+1)
        if koren.pravy is not None:
            preord(koren.pravy, list+1)

    preord(koren, 0)
    return tuple(ans)


koren = VrcholBinStromu(0)

koren.levy = VrcholBinStromu(1)
koren.pravy = VrcholBinStromu(2)

koren.levy.levy = VrcholBinStromu(3)
koren.levy.pravy = VrcholBinStromu(5)

koren.pravy.levy = VrcholBinStromu(4)
koren.pravy.pravy = VrcholBinStromu(6)

koren.levy.levy.levy = VrcholBinStromu(7)
koren.levy.levy.pravy = VrcholBinStromu(9)


print(minHloubkaListu(koren))
