import matplotlib.pyplot as plt
import sys


from parseData import parseData
from dataView import DataView
from polynomial import Polynomial
from rms import removeErrors, calcRms
from writeToFile import writeToFile


def drawRegressionGraph(pol: Polynomial, removedPoints=None, old=None):
    if removedPoints is not None:
        plt.plot(*removedPoints, 'o', color='red')
    if old is not None:
        x1, y1 = old.getGraphData()
        plt.plot(x1, y1, '-r', label=f'old')

    x, y = pol.getGraphData()


    plt.plot(x, y, '-', label=f'y= p(x), k={pol.k - 1}', color='gray', linewidth=4)


    plt.plot(pol.data.X, pol.data.Y, 'o', color='black')

    plt.title(f'Polynomial regression, rms = {calcRms(pol)}')
    plt.xlabel('t', color='#1C2833')
    plt.ylabel('data', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()


def main():
    tList, dataList = parseData("matera4a-raw.txt")
    # tList, dataList = parseData("testData")
    tList.append(tList[-1] + 10)
    sessions = []

    prevT = tList[0]  # cut data for sessions
    prevI = 0
    for i, t in enumerate(tList):
        if t - prevT > 5 / 24 / 60:  # Days to mins
            if i - prevI > 2:
                sessions.append(DataView(tList[prevI:i], dataList[prevI:i]))
            prevI = i
        prevT = t

    # plt.ion()
    print(f"found {len(sessions)} sessions")


    k = 3
    e = 3
    s = int(sys.argv[1]) - 1

    polynoms = []
    removed = []

    for session in sessions:
        pol = Polynomial(session, k)
        removed.append(removeErrors(pol, e))
        polynoms.append(Polynomial(session, k))

    writeToFile(polynoms, 'res.txt')
    polynoms[s].k = 6
    polynoms[s].solveX(1)
    drawRegressionGraph(polynoms[s], removed[s])

    # plt.plot(x, y, '-r', label=f'y= p(x)')
    #
    # plt.plot(tList, dataList, 'o', color='black')
    #
    # plt.title('Linear regression')
    # plt.xlabel('t', color='#1C2833')
    # plt.ylabel('data', color='#1C2833')
    # plt.legend(loc='upper left')
    # plt.grid()
    # plt.show()
    #
    # plt.pause(3)
    #
    # plt.clf()
    #
    # plt.pause(3)
    #
    # plt.plot(x, y, '-r', label=f'y= p(x)')
    #
    # plt.plot(tList, dataList, 'o', color='black')
    #
    # plt.title('Linear regression')
    # plt.xlabel('t', color='#1C2833')
    # plt.ylabel('data', color='#1C2833')
    # plt.legend(loc='upper left')
    # plt.grid()
    # plt.show()


if __name__ == '__main__':
    main()
