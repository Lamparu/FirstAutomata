from genSTRfile import FILEgenerator
from checkREG import checkFILE
from checkREG import checkREGstr


ch = 1
while int(ch) != 0:
    print('1. Generate file 1 mln strings')
    print('2. Write string from keyboard')
    print('3. Check file')
    print('Choose option: ')
    ch = input()
    if ch.isdigit():
        if int(ch) == 1:
            FILEgenerator()
        elif int(ch) == 2:
            print('Write: ')
            strcheck = input()
            print(checkREGstr(strcheck))
        elif int(ch) == 3:
            checkFILE()
        elif int(ch) == 0:
            break
        else:
            print('Beyond choice')
    else:
        print('Not digit')
print('END')