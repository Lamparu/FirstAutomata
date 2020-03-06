import TestSMC_sm


class TestSMC:
    def __init__(self):
        self._fsm = TestSMC_sm.TestSMC_sm(self)
        self._is_acceptable = False
        self._fsm.enterStartState()
        self._valname = ''
        self._litstr = ''
        self._counter = 0
        self._length = 0
        self._equal = False

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def CheckString(self, string):
        self._fsm.Start()
        for c in string:  # TODO: можно вместо for взять while, тогда след символ получу
            if c.isalpha():
                self._fsm.Letter()
            elif c.isdigit():
                self._fsm.Digital()
            elif c == '=':
                self._fsm.EqSign()
            elif c == '-':  # TODO: исправить состояние для минуса?
                self._fsm.MinSign()
            elif c == ' ':
                self._fsm.SpaceSym()
            elif c == '-' or c == '*' or c == '/' or c == '+':
                self._fsm.OpSign()
            elif c == '\n':
                self._fsm.EOS()
                break
            else:
                self._fsm.Unknown()
        self._fsm.EOS()
        return self._is_acceptable

    def UseEqSign(self):
        self._equal = True

    def ClearEqSign(self):
        self._equal = False

    def LengthInc(self):
        self._length += 1

    def LengthZero(self):
        self._length = 0

    def CounterInc(self):
        self._counter += 1

    def CounterZero(self):
        self._counter = 0

    def ClearValname(self):
        self._valname = ''

    def ClearLitstr(self):
        self._litstr = ''

    def ClearSMC(self):
        self.CounterZero()
        self.LengthZero()
        self._is_acceptable = True
        self.ClearValname()
        self.ClearLitstr()
        self.ClearEqSign()

    def isLess16(self):
        return self._counter <= 16

    def CheckNames(self):
        if self._litstr != '':
            return self._valname == self._litstr
        else:
            return True

    def isCounterMoreOne(self):
        return self._counter > 1

    def isNotZero(self):  # TODO: как понять, что 1ая цифра не 0?
        pass

    def EqSignIsNotUsed(self):
        return not self._equal
