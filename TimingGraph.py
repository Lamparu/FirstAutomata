import matplotlib.pyplot as plt
import matplotlib.ticker as plticker


def printGraph():
    plt.title('Timing of checking file for 1mln strings')
    plt.xlabel('Num of strings')
    plt.ylabel('Time')
    timeREG = open('timeREG.txt', 'r')
    timeSMC = open('timeSMC.txt', 'r')
    timePLY = open('timePLY.txt', 'r')
    x_data = [0]
    y_REG = [0]
    y_SMC = [0]
    y_PLY = [0]
    x = 0
    for y in timeREG.readlines():
        x += 10000
        x_data.append(x)
        y_REG.append(round(float(y)))
    for y in timeSMC.readlines():
        y_SMC.append(round(float(y)))
    for y in timePLY.readlines():
        y_PLY.append(round(float(y)))
    plt.plot(x_data, y_REG, label='REG')
    plt.plot(x_data, y_SMC, label='SMC')
    plt.plot(x_data, y_PLY, label='PLY')
    plt.legend()
    # ax = plt.axes()
    # loc = plticker.MultipleLocator(base=1.0)
    # ax.yaxis.set_major_locator(plticker.MultipleLocator(5))
    plt.show()
    timeREG.close()
    timeSMC.close()
    timePLY.close()
