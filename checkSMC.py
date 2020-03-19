import AppClass
import time


def readTimeFileSMC():
    f = open('timeSMC.txt', 'r')
    print('SMC time: ' + f.read())
    f.close()


def checkSMCstr(strch):
    machine = AppClass.AppClass()
    match = machine.CheckString(strch)
    # return machine.Acceptable()
    if match:
        return machine.GetStrNum() + ': ' + str(machine.GetCounter())
    else:
        return 'Unacceptable'


def SMCcheck():
    machine = AppClass.AppClass()
    f = open('genSTR.txt', 'r')
    res = open('resSMC.txt', 'w')
    ftime = open('timeSMC.txt', 'w')
    start_time = time.perf_counter()
    for line in f.readlines():
        match = machine.CheckString(line)
        if match:
            res.write(machine.GetStrNum() + ': ' + str(machine.GetCounter()) + '\n')
    end_time = time.perf_counter()
    ftime.write(str(end_time - start_time))
    ftime.close()
    f.close()
    res.close()
