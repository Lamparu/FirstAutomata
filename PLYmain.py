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
    numline = 0
    for line in f.readlines():
        numline += 1
        parser.checkString(line)
        if parser.in_dict and parser.flag:
            # print(parser.strnum + ' : ' + str(len(parser.val_instr)))
            res.write(parser.strnum + ' : ' + str(len(parser.val_instr)) + '\n')
        if numline % 10000 == 0:
            ftime.write(str(time.perf_counter() - time_start) + '\n')
    print('***File was checked with PLY***')
    ftime.close()
    res.close()
    f.close()

