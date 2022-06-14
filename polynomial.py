import math

import numpy as np  # t

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

    def solveX(self, check=0):
        A = self.data.matrFromData(self._k)
        B = self.data.rightSide(self._k)
        self.X = solve(A, B)

        if check:

            rms = self.cRms()

            X = []
            for i in range(len(self.data.X)):
                t = []
                for j in range(len(self.X)):
                    t.append(self.data.X[i] ** j)
                X.append(t)

            X = np.array(X)

            W = []
            for i in range(len(self.data.X)):
                t = [0] * len(self.data.X)
                t[i] = (rms * rms)
                W.append(t)
            W = np.matrix(W)

            matr = np.linalg.inv(X.T @ W @ X)
            matr = np.abs(matr)
            matr = np.sqrt(matr)
            d = np.diag(matr)

            print('        param               3*sigma')
            for i in range(self._k):
                if math.fabs(self.X[i]) < 3 * d[i]:
                    print(f"{i+1}   {math.fabs(self.X[i])} < {3 * d[i]} - not needed")
                else:
                    print(f"{i + 1}   {math.fabs(self.X[i])} < {3 * d[i]} - good")


    def getGraphData(self):

        x = list(linspace(self.data.X[0], self.data.X[-1]))

        y = [0] * len(x)

        for i in range(len(x)):
            y[i] = self.p(x[i])

        return x, y

    def p(self, x: float):
        y = 0.
        for j in range(len(self.X)):
            y += self.X[j] * x ** j
        return y

    def cRms(self):
        observations = self.data.Y
        n = len(observations)
        summ = 0.
        for obs in observations:
            summ += obs ** 2

        return math.sqrt(summ / n)


def solve(A, B):  # Cholesky decomposition method
    G = []
    for _ in A:
        G.append([0] * len(A))

    G[0][0] = math.sqrt(A[0][0])  # find G
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                summ = 0.
                for k in range(i):
                    summ += G[k][i] ** 2

                G[i][i] = math.sqrt(A[i][i] - summ)
            elif i < j:
                summ = 0.
                for k in range(i):
                    summ += G[k][i] * G[k][j]

                G[i][j] = (A[i][j] - summ) / G[i][i]

    # find y

    Y = [0] * len(A)
    X = [0] * len(A)

    Y[0] = B[0] / G[0][0]
    for i in range(1, len(Y)):  # find Y
        summ = 0.
        for k in range(i):
            summ += G[k][i] * Y[k]

        Y[i] = (B[i] - summ) / G[i][i]

    X[-1] = Y[-1] / G[-1][-1]
    for i in reversed(range(0, len(Y))):  # find X (solution)
        summ = 0.
        for k in range(i + 1, len(X)):
            summ += G[i][k] * X[k]

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
