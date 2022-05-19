from functools import cache


class DataView:
    def __init__(self, x: list, y: list):
        self.X = x
        self.Y = y

        self._avgX = sum(x) / len(x)
        self._avgY = sum(y) / len(y)

    @cache
    def avgXpowKY(self, k: int) -> float:
        XkY = map(lambda x, y: x ** k * y, zip(self.X, self.Y))
        return sum(XkY) / len(self.X)

    @cache
    def avgXK(self, k: int) -> float:
        Xk = map(lambda x: x ** k, self.X)
        return sum(Xk) / len(self.X)
