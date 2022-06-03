import math

from dataView import DataView

class Polynomial:
    def __init__(self, data: DataView, k: int):
        self.data = data
        self._k = k
        self.X = None
        self.solveX()

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, newK: int):
        self._k = newK
        self.solveX()

    def solveX(self):
        A = self.data.matrFromData(self._k)
        B = self.data.rightSide(self._k)
        self.X = solve(A, B)

    def getGraphData(self):

        x = list(linspace(self.data.X[0], self.data.X[-1]))

        y = [0] * len(x)

        for i in range(len(x)):
            y[i] = self.p(x[i])

        return x, y


    def p(self, x: float):
        y = 0
        for j in range(len(self.X)):
            y += self.X[j] * x ** j
        return y


def solve(A, B): # Cholesky decomposition method
    G = []
    for _ in A:
        G.append([0] * len(A))

    G[0][0] = math.sqrt(A[0][0])  # find G
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                summ = 0
                for k in range(i):
                    summ += G[k][i] ** 2

                G[i][i] = math.sqrt(A[i][i] - summ)
            elif i < j:
                summ = 0
                for k in range(i):
                    summ += G[k][i] * G[k][j]

                G[i][j] = (A[i][j] - summ) / G[i][i]

    # find y

    Y = [0] * len(A)
    X = [0] * len(A)

    Y[0] = B[0] / G[0][0]
    for i in range(1, len(Y)): # find Y
        summ = 0
        for k in range(i):
            summ += G[k][i] * Y[k]

        Y[i] = (B[i] - summ) / G[i][i]

    X[-1] = Y[-1] / G[-1][-1]
    for i in reversed(range(0,len(Y))): # find X (solution)
        summ = 0
        for k in range(i+1, len(X)):
            summ += G[i][k]*X[k]

        X[i] = (Y[i] - summ) / G[i][i]

    return X


def linspace(start, stop, num=100, endpoint=True):  # used only for drawing graph
    num = int(num)
    start = start * 1.
    stop = stop * 1.

    if num == 1:
        yield stop
        return
    if endpoint:
        step = (stop - start) / (num - 1)
    else:
        step = (stop - start) / num

    for i in range(num):
        yield start + step * i
