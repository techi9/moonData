from typing import List

from polynomial import Polynomial
from rms import calcRms


def createNormalPoints(sessions: List[Polynomial]) -> list:
    normalPoints = []

    for session in sessions:
        mid = round(session.data.X[-1] / 2)
        normalPoints.append((mid, session.p(mid), calcRms(session)))  # момент времени, значение полинома в нём и rms

    return normalPoints

