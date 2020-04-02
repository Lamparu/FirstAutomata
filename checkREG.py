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
        match = re.fullmatch(refer, line.rstrip())
        if match:
            here = True
            # print(numline, ' ', match.group('strnum'))
            res = 0
            gr = re.split(spref, line.rstrip())
            if gr[-1] == '':
                gr = gr[:-1]
            # print(gr)
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


def checkREGstr(strch, dict_val):
    dic = {}
    for ind in dict_val:
        dic[ind] = 0
    match = re.fullmatch(refer, strch.rstrip())
    if match:
        # print(numline, ' ', match.group('strnum'))
        res = 0
        gr = re.split(spref, strch.rstrip())
        if gr[-1] == '':
            gr = gr[:-1]
        # print(gr)
        for ind in gr[1:]:
            if dic.get(ind) is None:
                return 'Unacceptable'
            else:
                dic[ind] = 1
        dic[match.group('valname')] = 1
        # print(dict_val)
        for val in dic:
            if dic.get(val) == 1:
                res += 1
        return match.group('strnum') + ' : ' + str(res)
    else:
        return 'Unacceptable'
