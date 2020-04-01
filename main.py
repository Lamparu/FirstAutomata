from genSTRfile import GENclass
from checkREG import checkFILE
from checkREG import checkREGstr
from checkSMC import SMCcheck
from checkSMC import checkSMCstr
from PLYmain import PLYcheck
from PLYmain import checkPLYstr
from TimingGraph import printGraph

ch = 1
while int(ch) != 0:
    print('1. Generate file')
    print('2. Write string from keyboard')
    print('3. Check file with RegEx')
    print('4. Check file with SMC')
    print('5. Check file with PLY')
    print('6. Show statistics')
    print('Choose option: ')
    ch = input()
    if ch.isdigit():
        if int(ch) == 1:
            gen = GENclass()
            gen.FILEgenerator()
        elif int(ch) == 2:
            print('Write: ')
            strcheck = input()
            print('RegEx: ' + checkREGstr(strcheck))
            print('SMC: ' + checkSMCstr(strcheck))
            print('PLY: ' + checkPLYstr(strcheck))
        elif int(ch) == 3:
            checkFILE()
        elif int(ch) == 4:
            SMCcheck()
        elif int(ch) == 5:
            PLYcheck()
        elif int(ch) == 6:
            printGraph()
        elif int(ch) == 0:
            break
        else:
            print('Beyond choice')
    else:
        print('Not digit')
print('END')
