import ply.yacc as yacc
from checkFLEX import LexerClass
from checkFLEX import data


class ParserClass:
    tokens = LexerClass.tokens

    def __init__(self):
        self.lexer = LexerClass()
        self.parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        self.dictstr = {}
        self.val_instr = {}
        self.strnum = ''
        self.flag = False
        self.in_dict = True

    def p_addstart(self, p):
        """addstart : NUM LITSTR EQSIGN digorlit NL
                    | NUM LITSTR EQSIGN digorlit anytail NL"""
        if len(p) == 7:
            # print('len = 7')
            p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
        elif len(p) == 6:
            # print('len = 6')
            p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        # print('addstart ' + p[0])
        self.strnum = p[1].strip()
        self.flag = True
        self.dictstr[p[2]] = self.strnum
        self.val_instr[p[2]] = 1

    # def p_digorlit(self,p):
    #     """digorlit : LITSTR
    #                 | DIGSTR """
    #     p[0] = p[1]
    #     print('digorlit ' + p[0])

    def p_digorlit_lit(self, p):
        """digorlit : LITSTR """
        p[0] = p[1]
        # print('digorlit_lit ' + p[0])
        if self.dictstr.get(p[1]) is None:
            self.in_dict = False
        else:
            self.val_instr[p[1]] = 1

    def p_digorlit_dig(self, p):
        """digorlit : DIGSTR """
        p[0] = p[1]
        # print('digorlit_dig ' + p[0])

    def p_anytail(self, p):
        """anytail : tailone
                    | anytail tailone """
        if len(p) == 2:
            p[0] = p[1]
            # print('anaytail1 ' + p[0])
        elif len(p) == 3:
            p[0] = p[1] + p[2]
            # print('anytail2 ' + p[0])

    def p_tailone_dig(self, p):
        """tailone : OPERSIGN DIGSTR """
        p[0] = p[1] + p[2]
        # print('tailone_dig ' + p[0])

    def p_tailone_lit(self, p):
        """tailone : OPERSIGN LITSTR """
        p[0] = p[1] + p[2]
        # print('taione_lit ' + p[0])
        if self.dictstr.get(p[2]) is None:
            self.in_dict = False
        else:
            self.val_instr[p[2]] = 1

    def p_addstart_zero_err_type(self, p):
        """addstart : err NL"""
        p[0] = p[1] + p[2]
        # print('err0' + p[0])

    def p_addstart_first_err_type(self, p):
        """addstart : NUM err NL"""
        p[0] = p[1] + p[2] + p[3]
        # print('err1 ' + p[0])

    def p_addstart_second_err_type(self, p):
        """addstart : NUM LITSTR err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]
        # print('err2 ' + p[0])

    def p_addstart_third_err_type(self, p):
        """addstart : NUM LITSTR EQSIGN err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        # print('err3 ' + p[0])

    def p_addstart_fourth_err_type(self, p):
        """addstart : NUM LITSTR EQSIGN digorlit err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
        # print('err4 ' + p[0])

    def p_err(self, p):
        """err : ANY"""
        p[0] = p[1]
        # print('err ' + p[0])

    def p_error(self, p):
        # print('Unexpected token: ', p)
        pass

    def checkString(self, st):
        self.in_dict = True
        self.val_instr.clear()
        self.strnum = ''
        self.flag = False
        # print(st)
        res = self.parser.parse(st)
        return res


# y = ParserClass()
# y.checkString(data)
