import AppClass
import time


def readTimeFileSMC():
    f = open('timeSMC.txt', 'r')
    print('SMC time: ' + f.read())
    f.close()


def checkSMCstr(strch, dict_valnames):
    machine = AppClass.AppClass()
    # print(machine.GetValDict())
    machine.SetValDict(dict_valnames)
    # print(machine.GetValDict())
    match = machine.CheckString(strch)
    # print(machine.GetValDict())
    if match:
        return str(machine.GetStrNum()) + ' : ' + str(machine.getNumLitstr())
    else:
        return 'Unacceptable'


def SMCcheck():
    machine = AppClass.AppClass()
    f = open('genSTR.txt', 'r')
    res = open('resSMC.txt', 'w')
    ftime = open('timeSMC.txt', 'w')
    time_start = time.perf_counter()
    numline = 0
    for line in f.readlines():
        numline += 1
        match = machine.CheckString(line)
        if match:
            # print(machine.GetStrNum() + ': ' + str(machine.getNumLitstr()))
            res.write(str(machine.GetStrNum()) + ' : ' + str(machine.getNumLitstr()) + '\n')
        if numline % 10000 == 0:
            ftime.write(str(time.perf_counter() - time_start) + '\n')
    print('***File was checked by SMC***')
    ftime.close()
    f.close()
    res.close()
