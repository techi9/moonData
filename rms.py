import math

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
            if math.fabs(rms - (obs - pol.p(t))) > border:
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


def calcRms(pol: Polynomial):
    observations = pol.data.Y[:]
    ti = pol.data.X[:]

    n = len(ti)
    summ = 0
    for index, (t, obs) in enumerate(zip(ti, observations)):
        summ += (pol.p(t) - obs) ** 2

    return math.sqrt(summ / n)
