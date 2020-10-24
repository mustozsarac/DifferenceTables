import matplotlib.pyplot as plt
import numpy as np

def myTable(param):
    plt.plot(param, 'ro', color='b', marker='o', label='Original Data')  # plotting original data
    forwardTable(param)
    backwardTable(param)
    centralAndAverageTable(param)


def giveMeMaxDigit(param):#this function hepls me to get maximum digit on array. i am doing this because it helps me to write the table properly.
    max = 0.0
    a = 0
    for i in range(0, len(param)):
        for j in range(0, len(param[0])):
            if param[i][j] > max :
                max = param[i][j]

    return len(str(int(max)))


def printTable(param):#print table function for forward and backward difference.
    print("\t\t",end="")
    for x in range(0,len(param)):
        print("Y" + str(x)+ "\t", end="")
    print()
    a = str(giveMeMaxDigit(param))#this is where I take my digit,
    string = "{:0" + a + ".0f}"#creating a format string with using max digit.
    for i in range(0, len(param)):
        print("x:[" + str(i) + "] ", end="\t")
        for j in range(0, len(param)):
            print(string.format((param[i][j])), end="\t")
        print()


def printTableCenteralAndAverage(param):#this function helps me to print centeral and average tables.
    print("\t\t\t",end="")
    for x in range(0,len(param[0])):
        print("Y" + str(x)+ "\t\t", end="")
    print()

    x = 0.0
    a = str(giveMeMaxDigit(param))

    string = "{:0" + a + ".02f}"
    for i in range(0, len(param)):
        print("x:[" + str(x) + "] ", end="\t")
        for j in range(0, len(param[0])):
            print(string.format((param[i][j])), end="\t")
        print()
        x = x + 0.5

def forwardTable(param):
    counter = 0
    print("------------Forward Difference Table------------")
    forward = np.zeros([len(param), len(param)])
    forward[:, 0] = param# with this code, forwards first column becomes original array which is 1D

    a = len(param) - 1

    for i in range(1, len(param)):
        for j in range(0,a):
            forward[j][i] = forward[j+1][i-1] - forward[j][i-1]
        a = a - 1

    print()
    printTable(forward)
    forwplot = forward[:len(param) - 1, 1]  # taking elements of first step
    plt.plot(forwplot, 'ro', color='gold', marker='D', label='Forward Difference')  # plotting forward dif

def backwardTable(param):
    counter = 0
    print("------------Backward Difference Table------------")
    back = np.zeros([len(param), len(param)])
    back[:, 0] = param#copying original array into the first row of back array.

    y=1
    a = len(param)
    for i in range(1, len(param)):
        for j in range(y, a):
            back[j][i] = back[j][i-1] - back[j-1][i-1]
        y = y + 1

    print()
    printTable(back)
    backplot = back[1:, 1]  # taking elements of first step
    plt.plot(backplot, 'ro', color='g', marker='o', label='Backward Difference')  # plotting backward dif

def centralAndAverageTable(param):
    print("------------Central Difference Table--------------")
    centeral = np.zeros([2 * len(param) - 1, len(param)])
    average  = np.zeros([2 * len(param) - 1, len(param)])

    a = 1
    b = 2 * len(param) - 1
    c = len(param)

    x = 0
    for y in range(len(param)):#filling arrays with param by skipping 2
        centeral[x][0] = param[y]
        average[x][0] = param[y]
        x = x + 2

    for i in range(1, c):#calculating average and centeral diff.
        b = b - 1
        for j in range(a, b):
            centeral[j][i] = centeral[j + 1][i - 1] - centeral[j - 1][i - 1]
            average[j][i] = (average[j + 1][i - 1] + average[j - 1][i - 1])/2
        a = a + 1




    printTableCenteralAndAverage(centeral)
    cntplot = np.array(centeral[:, 1]) # taking elements of first step


    xAxis = np.zeros([len(param) - 1])  # creating a x-axis with fractions for central difference and average values
    start = 0.5
    for f in range(0, len(param) - 1):
        xAxis[f] = start
        start += 1

    plt.plot(xAxis, cntplot[1::2], 'ro', color='r', marker='^', label='Central Data')  # plotting centeral dif
    print()
    print("------------Average Difference Table--------------")
    printTableCenteralAndAverage(average)
    avgplot = np.array(average[:, 1])  # taking elements of first step
    print(avgplot)
    plt.plot(xAxis, avgplot[1::2], 'ro', color='purple', marker='o', label='Average')  # plotting average

    plt.xticks(np.arange(0, len(param) - 0.5, 0.5))
    plt.grid()
    plt.legend(loc=2)
    plt.show()
