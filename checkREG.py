import re
import time

refer = r'^(?P<strnum>\d+) (?P<valname>[a-zA-Z][a-zA-Z0-9]{0,15}) \= (\-?((?P<lit1>[a-zA-Z][a-zA-Z0-9]{0,15})|[1-9][0-9]*) (\+|\-|\*|\/) \-?((?P<lit2>[a-zA-Z][a-zA-Z0-9]{0,15})|[1-9][0-9]*)|\-?((?P<lit22>[a-zA-Z][a-zA-Z0-9]{0,15})|[1-9][0-9]*))$'


def checkFILE():
    f = open('genSTR.txt', 'r')
    resf = open('resSTR.txt', 'w')
    n1 = time.time()
    for line in f.readlines():
        res = 1
        match = re.fullmatch(refer, line.rstrip())
        if match:
            # print(match[0])
            if match.group('lit1'):
                if match.group('valname') == match.group('lit1'):
                    res += 1
                else:
                    continue
            if match.group('lit2') or match.group('lit22'):
                if match.group('valname') == match.group('lit2') or match.group('valname') == match.group('lit22'):
                    res += 1
                else:
                    continue
            resf.write(match.group('strnum') + ' : ' + str(res) + '\n')
            # print(match.group('strnum') + ' : ' + str(res))
            # print(match.group('valname') + ' : ' + str(res))
    n2 = time.time()
    print(n2 - n1)
    f.close()
    resf.close()


def checkREGstr(strch):
    res = 1
    match = re.fullmatch(refer, strch.rstrip())
    if match:
        if match.group('lit1'):
            if match.group('valname') == match.group('lit1'):
                res += 1
            else:
                return 'Unacceptable'
        if match.group('lit2') or match.group('lit22'):
            if match.group('valname') == match.group('lit2') or match.group('valname') == match.group('lit22'):
                res += 1
            else:
                return 'Unacceptable'
        return match.group('strnum') + ' : ' + match.group('valname') + ' ' + str(res)
    else:
        return 'Unacceptable'
