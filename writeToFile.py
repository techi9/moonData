from typing import List
import datetime
from astropy.time import Time

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
            times = [str(tMjd)]
            t = Time(times, format='mjd', scale='utc')
            t = t.to_value('iso')[0]
            t = t[:t.find('.')]
            t = t.replace(' ', '.').replace(':', '').replace('-', '')
            print(t, tMjd, predict, rms, sep='  ')
            f.write(f"{t}  {tMjd}  {predict}  {rms}\n")