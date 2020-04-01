from strgen import StringGenerator
import random
import time

class GENclass:

    def __init__(self):
        self.val_dict = {}
        self.first = True
        self.amount = 10  # amount of terms in 1 string
        self.strings = 1000001  # amount of strings in file
        self.truestring = 100  # 1 in this is true

    def buildNameVar(self):
        namevar = StringGenerator('[a-zA-Z]{1}').render()
        namevar += StringGenerator('[a-zA-Z0-9]{1:15}').render()
        return namevar

    def buildStrLit(self):
        strlit = ''
        if random.randint(1, 2) % 2 == 0:
            strlit += '-'
        if random.randint(1, 2) % 2 == 0:
            strlit += str(random.randint(1, 9))
            strlit += StringGenerator('[\d]{1:3}').render()
        else:
            strlit = StringGenerator('[a-zA-Z]{1}').render()
            strlit += StringGenerator('[\w]{1:15}').render()
        return strlit

    def buildDig(self):
        strdig = ''
        if random.randint(1, 2) % 2 == 0:
            strdig += '-'
        strdig += StringGenerator('[1-9]{1}').render()
        strdig += StringGenerator('[0-9]{1:15}').render()
        return strdig

    def getNamevar(self):
        # print(self.val_dict.keys())
        # print(random.choice(self.val_dict.keys()))
        return random.choice(list(self.val_dict.keys()))

    def chooseOperator(self):
        operation_choice = random.randint(1, 4)
        if operation_choice == 1:
            ns = ' + '
        elif operation_choice == 2:
            ns = ' - '
        elif operation_choice == 3:
            ns = ' * '
        else:
            ns = ' / '
        return ns

    def buildTrueStr(self, num):
        nstr = str(num) + ' '
        namevar = self.buildNameVar()
        nstr += namevar + ' = '
        if self.first:
            nstr += self.buildDig()
            i = random.randint(0, self.amount)
            while i > 0:
                nstr += self.chooseOperator() + self.buildDig()
                i -= 1
            self.first = False
            self.val_dict[namevar] = 1
            return nstr
        i = random.randint(0, self.amount)
        if i % 2 == 0:
            nstr += self.getNamevar()
        else:
            nstr += self.buildDig()
        while i > 0:
            nstr += self.chooseOperator()
            if random.randint(1, 3) % 2 == 0:
                nstr += self.buildDig()
            else:
                nstr += self.getNamevar()
            i -= 1
        self.val_dict[namevar] = 1
        return nstr

    def buildOperLitstr(self, namevar):
        nstr = self.chooseOperator()
        if random.randint(1, 3) % 2 == 0:
            nstr += namevar
        else:
            nstr += self.buildStrLit()
        return nstr

    def digNameVar(self):
        namevar = StringGenerator('[\d]{1}').render()
        namevar += StringGenerator('[a-zA-Z0-9]{1:15}').render()
        return namevar

    def _longNameVar(self):
        if random.randint(1, 2) % 2 == 0:
            return StringGenerator('[\w]{17:18}').render()
        else:
            return StringGenerator('[\w]{1:13}').render() + StringGenerator('[\p]{1:3}').render()

    def buildFalseStr(self, num):
        choice = random.randint(1, 14)
        choice1 = random.randint(2, 14)
        # print(num, ' : ', choice, ' ', choice1)
        if choice == 12 or choice1 == 12:
            nstr = 'a'
        elif choice == 13 or choice1 == 13:
            nstr = ''
        elif choice == 14 or choice1 == 14:
            nstr = '-' + str(num) + ' '
        else:
            nstr = str(num) + ' '
        if choice == 2 or choice1 == 2:
            namevar = self.digNameVar()
        elif choice == 3 or choice1 == 3:
            namevar = self._longNameVar()
        else:
            namevar = self.buildNameVar()
        if choice == 4 or choice1 == 4:
            nstr += namevar + StringGenerator(' [\&\/\{\)] ').render()
        elif choice == 5 or choice1 == 5:
            nstr += namevar + '='
        elif choice == 6 or choice1 == 6:
            nstr += namevar + ' '
        else:
            nstr += namevar + ' = '
        if random.randint(1, 2) % 2 == 0:
            nstr += namevar
        else:
            nstr += self.buildStrLit()
        if choice == 7 or choice1 == 7:
            nstr += StringGenerator(' [\&\#\{\)] ').render()
        elif choice == 11 or choice1 == 11:
            nstr += ' '
        else:
            nstr += self.chooseOperator()
        if choice == 8 or choice1 == 8:
            nstr += self.chooseOperator()
            return nstr
        elif choice == 9 or choice1 == 9:
            strlit = '0' + StringGenerator('[\d]{1:3}').render()
        elif choice == 10 or choice1 == 10:
            strlit = StringGenerator('[\d]{1:3}').render() + '-'
        else:
            strlit = self.buildStrLit()
        nstr += strlit
        i = random.randint(0,10)
        while i > 0:
            nstr += self.buildOperLitstr(namevar)
            i -= 1
        return nstr

    def buildStr(self, num):
        if random.randint(1, self.truestring) == 2:
            # print('true: ', num)
            return self.buildTrueStr(num)
        else:
            return self.buildFalseStr(num)

    def FILEgenerator(self):
        f = open('genSTR.txt', 'w')
        ind = 1
        time_start = time.perf_counter()
        for index in [self.buildStr(i) for i in range(1, self.strings)]:
            f.write(index + '\n')
            # print(ind)
            ind += 1
        time_end = time.perf_counter()
        print('File for ', self.strings-1,  ' strings generated in ', time_end-time_start, ' seconds')
        f.close()

