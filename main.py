import matplotlib.pyplot as plt
import numpy as np

import polinomial

from dataView import DataView

from parseData import parseData


def main():
    tList, dataList = parseData("matera4a-raw.txt")

    for i, v in enumerate(tList):
        if v > 5:
            tList = tList[:i]
            dataList = dataList[:i]
            break

    data = DataView(tList, dataList)

    k = 4

    A = data.matrFromData(k)
    B = data.rightSide(k)
    X = solve(A, B)




    # x = np.array([0, tList[-1]])
    # y = a * x + b
    # plt.plot(x, y, '-r', label=f'y={a}x+({b})')
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
