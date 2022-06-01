import math


def solve(A, B):
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
    for i in range(1, len(Y)):
        summ = 0
        for k in range(i):
            summ += G[k][i] * Y[k]

        Y[i] = (B[i] - summ) / G[i][i]

        #TODO: add sol for X
