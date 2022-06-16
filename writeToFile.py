import math
from typing import List

from polynomial import Polynomial
from createNormalPoints import createNormalPoints


#  20180208.024959  58157.1180405556  -0.377 rms
#  date             date mjd          p(t)   rms


def writeToFile(sessions: List[Polynomial], filename: str):

    with open(filename, 'w') as f:
        for pol in sessions:
            tMjd, predict, rms = createNormalPoints([pol])[0]
            tMjd /= 24*60
            tMjd += pol.data.firstDate
            tJd = tMjd + 2400000.5
            year, month, day = jd_to_date(tJd)
            month = '0' + str(month) if month < 10 else month
            day = format(day, '.6f')
            day = '0' + str(day) if float(day) < 10 else day
            t = f'{year}{month}{day}'
            print(t, tMjd, predict, rms, sep='  ')
            f.write(f"{t}  {tMjd}  {predict}  {rms}\n")


def jd_to_date(jd):

    jd = jd + 0.5

    F, I = math.modf(jd)
    I = int(I)

    A = math.trunc((I - 1867216.25) / 36524.25)

    if I > 2299160:
        B = I + 1 + A - math.trunc(A / 4.)
    else:
        B = I

    C = B + 1524

    D = math.trunc((C - 122.1) / 365.25)

    E = math.trunc(365.25 * D)

    G = math.trunc((C - E) / 30.6001)

    day = C - E + F - math.trunc(30.6001 * G)

    if G < 13.5:
        month = G - 1
    else:
        month = G - 13

    if month > 2.5:
        year = D - 4716
    else:
        year = D - 4715

    return year, month, day
