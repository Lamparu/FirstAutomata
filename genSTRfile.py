from strgen import StringGenerator
from random import randint
from checkREG import refer
import re


def buildNameVar():
    namevar = StringGenerator('[a-zA-Z]{1}').render()
    namevar += StringGenerator('[\w]{1:15}').render()
    return namevar


def buildStrLit():
    strlit = ''
    if randint(1, 2) % 2 == 0:
        strlit += '-'
    strlit += str(randint(1, 9))
    strlit += StringGenerator('[\d]{1:3}').render()
    return strlit


def chooseOperator():
    operation_choice = randint(1, 4)
    if operation_choice == 1:
        ns = ' + '
    elif operation_choice == 2:
        ns = ' - '
    elif operation_choice == 3:
        ns = ' * '
    else:
        ns = ' / '
    return ns


def buildTrueStr(num):
    nstr = str(num) + ' '
    namevar = buildNameVar()
    nstr += namevar + ' = '
    if randint(1, 2) % 2 == 0:
        nstr += namevar
    else:
        nstr += buildStrLit()
    i = randint(0, 20)
    while i > 0:
        nstr += buildOperLitstr(namevar)
        i -= 1
    return nstr


def buildOperLitstr(namevar):
    nstr = chooseOperator()
    if randint(1, 2) % 2 == 0:
        nstr += namevar
    else:
        nstr += buildStrLit()
    return nstr


def digNameVar():
    namevar = StringGenerator('[\d]{1}').render()
    namevar += StringGenerator('[a-zA-Z0-9]{1:15}').render()
    return namevar


def _longNameVar():
    if randint(1, 2) % 2 == 0:
        return StringGenerator('[\w]{17:18}').render()
    else:
        return StringGenerator('[\w\p]{1:16}').render()


def buildFalseStr(num):
    choice = randint(1, 14)
    if choice == 12:
        nstr = 'a'
    elif choice == 13:
        nstr = ''
    elif choice == 14:
        nstr = '-' + str(num) + ' '
    else:
        nstr = str(num) + ' '
    if choice == 1:
        namevar = digNameVar()
    elif choice == 2:
        namevar = _longNameVar()
    else:
        namevar = buildNameVar()
    if choice == 3:
        nstr += namevar + StringGenerator(' [\&\/\{\)] ').render()
    elif choice == 4:
        nstr += namevar + '='
    elif choice == 5:
        nstr += namevar + ' '
    else:
        nstr += namevar + ' = '
    if choice == 6:
        namevar = StringGenerator('[\w]{1:16}').render()
        nstr += namevar
    else:
        if randint(1, 2) % 2 == 0:
            nstr += namevar
        else:
            nstr += buildStrLit()
    if choice == 7:
        nstr += StringGenerator(' [\&\/\{\)] ').render()
    elif choice == 11:
        nstr += ' '
    else:
        nstr += chooseOperator()
    if choice == 8:
        return nstr
    elif choice == 9:
        strlit = '0' + StringGenerator('[\d]{1:3}').render()
    elif choice == 10:
        strlit = StringGenerator('[\d]{1:3}').render() + '-'
    else:
        strlit = buildStrLit()
    nstr += strlit
    i = randint(0, 10)
    while i > 0:
        nstr += buildOperLitstr(namevar)
        i -= 1
    return nstr


def buildstr(num):
    if randint(1, 100000) == 3:
        return buildTrueStr(num)
    else:
        return buildFalseStr(num)


def FILEgenerator():
    f = open('genSTR.txt', 'w')
    ind = 1
    for index in [buildstr(i) for i in range(1, 1000001)]:
        f.write(index + '\n')
        print(ind)
        ind += 1
    f.close()
