
class DataView:
    def __init__(self, x: list, y: list):
        self.X = x[:]
        self.Y = y[:]

        self.X = list(map(lambda xx: (xx - self.X[0]), self.X))  # normalise time

        self.n = len(x)
        self._avgX = sum(x) / len(x)
        self._avgY = sum(y) / len(y)

    def avgXpowKY(self, k: int) -> float:

        summ = 0
        for x, y in zip(self.X, self.Y):
            summ += (x ** k) * y

        return summ / len(self.X)

    def avgXpowK(self, k: int) -> float:
        summ = 0
        for x in self.X:
            summ += x ** k

        return summ / len(self.X)

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


        return matr

    def rightSide(self, res: int):
        right = [0] * self.n

        for i in range(res):
            right[i] = self.avgXpowKY(i)

        return right
