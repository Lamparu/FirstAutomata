import re
import time

refer = r'^(?P<strnum>[1-9][0-9]*) +(?P<valname>[a-zA-Z][a-zA-Z0-9]{0,15}) +\= +(([a-zA-Z][a-zA-Z0-9]{0,15})|\-?[1-9][0-9]*)( +(\+|\-|\*|\/) +(([a-zA-Z][a-zA-Z0-9]{0,15})|\-?[1-9][0-9]*))*$'
spref = r'\s[^a-zA-Z]+[^a-zA-Z0-9]*'


def readTimeFileREG():
    fl = open('timeREG.txt', 'r')
    print('RegEx time: ' + fl.read())
    fl.close()


def checkFILE():
    f = open('genSTR.txt', 'r')
    resf = open('resSTR.txt', 'w')
    ftime = open('timeREG.txt', 'w')
    time_start = time.perf_counter()
    dict_val = {}
    numline = 0
    for line in f.readlines():
        numline += 1
        here = True
        match = re.fullmatch(refer, line.rstrip())
        if match:
            # print(numline, ' ', match.group('strnum'))
            res = 0
            gr = re.split(spref, line.rstrip())
            if gr[-1] == '':
                gr = gr[:-1]
            # print(gr)
            # print(gr[1:-1])
            # print(gr[-1])
            for ind in gr[1:]:
                if dict_val.get(ind) is None:
                    here = False
                    continue
                else:
                    dict_val[ind] = numline
            if not here:
                continue
            dict_val[match.group('valname')] = numline
            # print(dict_val)
            for val in dict_val:
                if dict_val.get(val) == numline:
                    res += 1
            # print(match.group('strnum') + ':' + str(res))
            resf.write(match.group('strnum') + ' : ' + str(res) + '\n')
        if numline % 10000 == 0:
            # print(numline)
            ftime.write(str(time.perf_counter() - time_start) + '\n')
    print('***File was checked by RegExpr***')
    ftime.close()
    f.close()
    resf.close()


def checkREGstr(strch):
    res = 1
    match = re.fullmatch(refer, strch.rstrip())
    gr = re.split(spref, strch.rstrip())
    if match:
        # print(match)
        # print(gr)
        if match.group('lit1'):
            if match.group('valname') != match.group('lit1'):
                return 'Unacceptable'
        for ind in gr[1:]:
            if match.group('valname') == ind:
                res += 1
            else:
                return 'Unacceptable'
        return match.group('strnum') + ': ' + str(res)
    else:
        return 'Unacceptable'
