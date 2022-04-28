import matplotlib.pyplot as plt
import numpy as np

from parseData import parseData


def main():
    tList, dataList = parseData("matera4a-raw.txt")

    # for i, v in enumerate(tList):
    #     if v > 5:
    #         tList = tList[:i]
    #         dataList = dataList[:i]
    #         break

    St = sum(tList) / len(tList)
    Sd = sum(dataList) / len(dataList)
    Std = sum(x*y for (x, y) in zip(tList, dataList)) / len(tList)
    Stt = sum(x*x for x in tList) / len(tList)

    a = (St * Sd - Std) / (St * St - Stt)
    b = (Std - a * Stt) / St

    x = np.array([0, tList[-1]])
    y = a * x + b
    plt.plot(x, y, '-r', label=f'y={a}x+({b})')

    plt.plot(tList, dataList, 'o', color='black');

    plt.title('Linear regression')
    plt.xlabel('t', color='#1C2833')
    plt.ylabel('data', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
