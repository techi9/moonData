from functools import lru_cache


class DataView:
    def __init__(self, x: list, y: list):
        self.X = x
        self.Y = y
        self.n = len(x)
        self._avgX = sum(x) / len(x)
        self._avgY = sum(y) / len(y)

    @lru_cache(maxsize=None)
    def avgXpowKY(self, k: int) -> float:
        XkY = map(lambda x, y: (x ** k) * y, zip(self.X, self.Y))
        return sum(XkY) / len(self.X)

    @lru_cache(maxsize=None)
    def avgXpowK(self, k: int) -> float:
        Xk = map(lambda x: x ** k, self.X)
        return sum(Xk) / len(self.X)

    def matrFromData(self, res: int):
        matr = []
        for _ in range(res):
            matr.append([0] * res)

        prevK = 0
        k = 0
        for i in matr:
            k = prevK
            for j in range(res):
                i[j] = self.avgXpowK(k)
                k += 1
            prevK += 1

        for i in matr:
            print(i)

        return matr

    def rightSide(self, res: int):
        right = [0] * self.n

        for i in range(res):
            right[i] = self.avgXpowKY(i)

        return right
