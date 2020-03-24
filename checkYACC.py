import ply.yacc as yacc
from checkFLEX import LexerClass


class ParserClass:
    tokens = LexerClass.tokens

    def __init__(self):
        self.lexer = LexerClass()
        self.parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        self.dictstr = dict()
        self.strnum = ''
        self.flag = False

    def p_addstart(self, p):
        """addstart : NUM LITSTR EQSIGN digorlit anytail NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
        print('addstart')
        print(p[0])
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
        print('digorlit_lit' + p[0])
        if p[1][0] == '-':
            self.dictstr[p[1][1:]] = 1
        else:
            self.dictstr[p[1]] = 1

    def p_digorlit_dig(self, p):
        """digorlit : DIGSTR"""
        p[0] = p[1]
        print('digorlit_dig' + p[0])

    def p_anytail(self, p):
        """anytail :
                    | tailone
                    | anytail tailone"""
        if len(p) == 1:
            p[0] = ''
            print('anytail0')
        elif len(p) == 2:
            p[0] = p[1]
            print('anaytail1' + p[0])
        elif len(p) == 3:
            p[0] = p[1] + p[2]
            print('anytail2' + p[0])

    def p_tailone_dig(self, p):
        """tailone : OPERSIGN DIGSTR"""
        p[0] = p[1] + p[2]
        print('tailone_dig' + p[0])

    def p_tailone_lit(self, p):
        """tailone : OPERSIGN TAILLITSTR"""
        p[0] = p[1] + p[2]
        print('taione_lit' + p[0])
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
        """addstart : err_list NL"""
        p[0] = p[1] + p[2]
        #print('err0')

    def p_addstart_first_err_type(self, p):
        """addstart : NUM err_list NL"""
        p[0] = p[1] + p[2] + p[3]
        #print('err1')

    def p_addstart_second_err_type(self, p):
        """addstart : NUM LITSTR err_list NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_addstart_third_err_type(self, p):
        """addstart : NUM LITSTR EQSIGN err_list NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    def p_addstart_fourth_err_type(self, p):
        """addstart : NUM LITSTR EQSIGN digorlit err_list NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
        print('err4')

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

    def p_err_list_t1(self, p):
        """err_list : err"""
        p[0] = p[1]

    def p_err_list_t2(self, p):
        """err_list : """
        p[0] = ''

    def p_err_list_t3(self, p):
        """err_list : err_list err"""
        p[0] = p[1] + p[2]

    def p_err(self, p):
        """err : ANY"""
        p[0] = p[1]

    def p_error(self, p):
        pass
        print('Unexpected token: ', p)

    def checkString(self, st):
        self.dictstr.clear()
        self.strnum = ''
        self.flag = False
        res = self.parser.parse(st)
        return res
