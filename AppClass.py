import AppClass_sm


class AppClass:
    def __init__(self):
        self._fsm = AppClass_sm.AppClass_sm(self)
        self._is_acceptable = False
        self._fsm.enterStartState()
        self._valname = ''
        self._litstr = ''
        self._digstr = ''
        self._counter = 0
        self._countTerms = 0
        self._length = 0
        self._OperSign = False
        self._equal = False
        # Uncomment to see debug output.
        # self._fsm.setDebugFlag(True)

    def GetCounter(self):
        return self._counter

    def GetStrNum(self):
        return self._digstr

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def CheckString(self, string):
        self._fsm.Start()
        for c in string:
            if c == '0':
                self._fsm.Zero(c)
            elif c.isalpha():
                self._fsm.Letter(c)
            elif c.isdigit():
                self._fsm.Digital(c)    # TODO: проверить сгенерированный файл с результатом, второе слагаемое плохо читается
            elif c == '=':
                self._fsm.EqSign()
            elif c == '-':
                self._fsm.MinSign()
            elif c == ' ':
                self._fsm.SpaceSym()
            elif c == '*' or c == '/' or c == '+':
                self._fsm.OpSign()
            elif c == '\n':
                self._fsm.EOS()  # TODO: написать это отдельно через EndLine
                break
            else:
                self._fsm.Unknown()
        self._fsm.EOS()
        return self._is_acceptable

    def UseEqSign(self):
        self._equal = True

    def ClearEqSign(self):
        self._equal = False

    def UseOperSign(self):
        self._OperSign = True

    def ClearOperSign(self):
        self._OperSign = False

    def LengthInc(self):
        self._length += 1

    def LengthZero(self):
        self._length = 0

    def CounterInc(self):
        self._counter += 1

    def CounterZero(self):
        self._counter = 0

    def CountTermsInc(self):
        self._countTerms += 1

    def CountTermsZero(self):
        self._countTerms = 0

    def ClearValname(self):
        self._valname = ''

    def ClearLitstr(self):
        self._litstr = ''

    def ClearDigstr(self):
        self._digstr = ''

    def InsertValname(self, c):
        self._valname += c

    def InsertLitstr(self, c):
        self._litstr += c

    def InsertDigstr(self, c):
        self._digstr += c

    def ClearSMC(self):
        self.CounterZero()
        self.LengthZero()
        self.CountTermsZero()
        self._is_acceptable = True
        self.ClearValname()
        self.ClearLitstr()
        self.ClearDigstr()
        self.ClearEqSign()
        self.ClearOperSign()

    def isLess16(self):
        return self._length <= 16

    def CheckNames(self):
        if self._litstr != '':
            return self._valname == self._litstr
        else:
            return True

    #def isCounterMoreOne(self):
     #   return self._counter > 1

    def isCounterOne(self):
        return self._counter == 1

    def isCounterZero(self):
        return self._counter == 0

    def isCounterMoreOrOne(self):
        return self._counter >= 1

    def isCountTermsOne(self):
        return self._countTerms == 1

    def isCountTermsMoreOne(self):
        return self._countTerms > 1

    def EqSignIsNotUsed(self):
        return not self._equal

    def EqSignIsUsed(self):
        return self._equal

    def OperSignIsUsed(self):
        return self._OperSign

    def StrNumIsValid(self):
        if self._digstr != '':
            return True
        else:
            return False
