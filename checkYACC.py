import ply.yacc as yacc
from checkFLEX import LexerClass
from checkFLEX import data


class ParserClass:
    tokens = LexerClass.tokens

    def __init__(self):
        self.lexer = LexerClass()
        self.parser = yacc.yacc(module=self, optimize=1, debug=True, write_tables=True)
        self.dictstr = dict()
        self.strnum = ''
        self.flag = False

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
        if self.dictstr.get(p[2]) is None:
            self.dictstr[p[2]] = 1
        else:
            self.dictstr[p[2]] += 1

    #def p_valuename(self, p):
     #   """valuename : LITSTR"""
      #  p[0] = p[1]
       # self.valname = p[1]
        #print('valuename')

    def p_digorlit_lit(self, p):
        """digorlit : TAILLITSTR"""
        p[0] = p[1]
        # print('digorlit_lit ' + p[0])
        if p[1][0] == '-':
            self.dictstr[p[1][1:]] = 1
        else:
            self.dictstr[p[1]] = 1

    def p_digorlit_dig(self, p):
        """digorlit : DIGSTR"""
        p[0] = p[1]
        # print('digorlit_dig ' + p[0])

    def p_anytail(self, p):
        """anytail : tailone
                    | anytail tailone"""
        if len(p) == 2:
            p[0] = p[1]
            # print('anaytail1 ' + p[0])
        elif len(p) == 3:
            p[0] = p[1] + p[2]
            # print('anytail2 ' + p[0])

    def p_tailone_dig(self, p):
        """tailone : OPERSIGN DIGSTR"""
        p[0] = p[1] + p[2]
        # print('tailone_dig ' + p[0])

    def p_tailone_lit(self, p):
        """tailone : OPERSIGN TAILLITSTR"""
        p[0] = p[1] + p[2]
        # print('taione_lit ' + p[0])
        if p[2][0] == '-':
            if self.dictstr.get(p[2][1:]) is None:
                self.dictstr[p[2][1:]] = 1
            else:
                self.dictstr[p[2][1:]] += 1
        else:
            if self.dictstr.get(p[2]) is None:
                self.dictstr[p[2]] = 1
            else:
                self.dictstr[p[2]] += 1

    def p_addstart_zero_err_type(self, p):
        """addstart : err NL"""
        p[0] = p[1] + p[2]
        #print('err0')

    def p_addstart_first_err_type(self, p):
        """addstart : NUM err NL"""
        p[0] = p[1] + p[2] + p[3]
        #print('err1')

    def p_addstart_second_err_type(self, p):
        """addstart : NUM LITSTR err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_addstart_third_err_type(self, p):
        """addstart : NUM LITSTR EQSIGN err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    def p_addstart_fourth_err_type(self, p):
        """addstart : NUM LITSTR EQSIGN digorlit err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
        # print('err4')

    # def p_tailone_first_err_type(self, p):
    #     """tailone : err_list DIGSTR"""
    #     p[0] = p[1] + p[2]
    #
    # def p_tailone_second_err_type(self, p):
    #     """tailone : err_list TAILLITSTR"""
    #     p[0] = p[1] + p[2]
    #
    # def p_tailone_third_err_type(self, p):
    #     """tailone : OPERSIGN err_list"""
    #     p[0] = p[1] + p[2]
    #
    # def p_anytail_first_err_type(self, p):
    #     """anytail : err_list"""
    #     p[0] = p[1]
    #
    # def p_anytail_second_err_type(self, p):
    #     """anytail : err_list tailone"""
    #     p[0] = p[1] + p[2]
    #
    # def p_anytail_third_err_type(self, p):
    #     """anytail : anytail err_list"""
    #     p[0] = p[1] + p[2]

    # def p_err_list_t1(self, p):
    #     """err_list : err"""
    #     p[0] = p[1]
    #
    # def p_err_list_t2(self, p):
    #     """err_list : """
    #     p[0] = ''
    #
    # def p_err_list_t3(self, p):
    #     """err_list : err_list err"""
    #     p[0] = p[1] + p[2]

    def p_err(self, p):
        """err : ANY"""
        p[0] = p[1]

    def p_error(self, p):
        #print('Unexpected token: ', p)
        pass

    def checkString(self, st):
        self.dictstr.clear()
        self.strnum = ''
        self.flag = False
        #print(st)
        res = self.parser.parse(st)
        return res


# y = ParserClass()
# y.checkString(data)
