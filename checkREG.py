import re
import time

refer = r'^(?P<strnum>\d+) +(?P<valname>[a-zA-Z][a-zA-Z0-9]{0,15}) +\= +\-?((?P<lit1>[a-zA-Z][a-zA-Z0-9]{0,15})|[1-9][0-9]*)( +(\+|\-|\*|\/) +\-?(([a-zA-Z][a-zA-Z0-9]{0,15})|[1-9][0-9]*))*$'
spref = r'\s[^a-zA-Z]+[^a-zA-Z0-9]*'

def checkFILE():
    f = open('genSTR.txt', 'r')
    resf = open('resSTR.txt', 'w')
    n1 = time.time()
    for line in f.readlines():
        res = 1
        match = re.fullmatch(refer, line.rstrip())
        gr = re.split(spref, line.rstrip())
        if match:
            #print(match)
            if match.group('lit1'):
                if match.group('valname') == match.group('lit1'):
                    res += 1
                else:
                    continue
            for ind in gr[1:]:
                if match.group('valname') == ind:
                    res += 1
                else:
                    continue
            resf.write(match.group('strnum') + ' : ' + str(res) + '\n')
            #print(match.group('strnum') + ' : ' + str(res))
            #print(match.group('valname') + ' : ' + str(res))
    n2 = time.time()
    print(n2 - n1)
    f.close()
    resf.close()


def checkREGstr(strch):
    res = 1
    match = re.fullmatch(refer, strch.rstrip())
    gr = re.split(spref, strch.rstrip())
    if match:
        print(match)
        print(gr)
        if match.group('lit1'):
            if match.group('valname') == match.group('lit1'):
                res += 1
            else:
                return 'Unacceptable1'
        for ind in gr[2:]:
            if match.group('valname') == ind:
                res += 1
            else:
                return 'Unacceptable2'
        return match.group('strnum') + ' : ' + match.group('valname') + ' ' + str(res)
    else:
        return 'Unacceptable3'
