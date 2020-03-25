from checkYACC import ParserClass
import time


def readTimeFilePLY():
    f = open('timePLY.txt')
    print('PLY time: ' + f.read())
    f.close()


def checkPLYstr(st):
    parser = ParserClass()
    parser.checkString(st + '\n')
    if len(parser.dictstr) == 1 and parser.flag:
        return parser.strnum + ' : ' + str(parser.dictstr.popitem()[1]) + '\n'
    else:
        return 'Unacceptable'


def PLYcheck():
    f = open('genSTR.txt', 'r')
    res = open('resPLY.txt', 'w')
    ftime = open('timePLY.txt', 'w')
    parser = ParserClass()
    time_start = time.perf_counter()
    for line in f.readlines():
        parser.checkString(line)
        if len(parser.dictstr) == 1 and parser.flag:
            res.write(parser.strnum + ' : ' + str(parser.dictstr.popitem()[1]) + '\n')
    time_end = time.perf_counter()
    ftime.write(str(time_end - time_start))
    ftime.close()
    res.close()
    f.close()

