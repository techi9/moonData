import math
from copy import deepcopy

from polynomial import Polynomial


def removeErrors(pol: Polynomial, border: float):
    removedT, removedObs = [], []
    observations = pol.data.Y[:]
    ti = pol.data.X[:]

    while True:  # removing errors
        removedPoints = 0
        toRem = []
        rms = calcRms(pol)
        for index, (t, obs) in enumerate(zip(ti, observations)):

            if math.fabs(obs - pol.p(t)) > border*rms:
                removedT.append(t)
                removedObs.append(obs)
                toRem.append(index)
                removedPoints += 1

        for index in sorted(toRem, reverse=True):
            del pol.data.X[index]
            del pol.data.Y[index]

        if removedPoints == 0:
            break

        observations = pol.data.Y[:]
        ti = pol.data.X[:]
        pol.solveX()  # recalc polynom

    return [removedT, removedObs]


# def calcRms(rmsList: list):
#     n = len(rmsList)
#     summ = 0.
#     for r in rmsList:
#         summ += r**2
#     return math.sqrt(summ / n)

def calcRms(pol: Polynomial):
    observations = pol.data.Y
    ti = pol.data.X

    n = len(ti)
    summ = 0.
    for index, (t, obs) in enumerate(zip(ti, observations)):
        summ += (obs - pol.p(t)) ** 2

    return math.sqrt(summ / n)
