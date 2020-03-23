import ply.yacc as yacc
from checkFLEX import tokens
from checkFLEX import data
from checkFLEX import lexer


class ParserClass:
    tokens = tokens

    def __init__(self):
        self.flag = True
        self.lexer = lexer
        self.parser = yacc.yacc(module=self, optimize=1, debug=True, write_tables=False)
        self.valname = ''
        self.count = 0

    def p_addstart(self, p):
        """addstart : NUM LITSTR EQSIGN digorlit anytail NL"""
        self.valname = p[2]
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
        #print('ok')
        #print(p[0])

    def p_digorlit_dig(self, p):
        """digorlit : DIGSTR"""
        p[0] = p[1]
        #print('digorlit')

    def p_digorlit_lit(self, p):
        """digorlit : TAILLITSTR"""
        if p[1] == self.valname or p[1] == '-'+self.valname:
            #print('equal')
            self.count += 1
        else:
            self.flag = False
        p[0] = p[1]

    def p_anytail(self, p):
        """anytail :
                    | tailone
                    | anytail tailone"""
        if len(p) == 1:
            p[0] = ''
            #print('a0')
        elif len(p) == 2:
            p[0] = p[1]
            #print('a1')
        elif len(p) == 3:
            p[0] = p[1] + p[2]
            #print('a2')

    def p_tailone_dig(self, p):
        """tailone : OPERSIGN DIGSTR"""
        p[0] = p[1] + p[2]
        #print('t1')

    def p_tailone_lit(self, p):
        """tailone : OPERSIGN TAILLITSTR"""
        if p[2] == self.valname or p[2] == '-'+self.valname:
            self.count += 1
        else:
            self.flag = False
        p[0] = p[1] + p[2]

    def p_addstart_zero_ett_type(self, p):
        """addstart : err_list NL"""
        p[0] = p[1] + p[2]
        self.flag = False
        #print(p)
        #print(p[0])

    def p_addstart_first_err_type(self, p):
        """addstart : NUM err_list NL"""
        p[0] = p[1] + p[2] + p[3]
        self.flag = False

    def p_addstart_second_err_type(self, p):
        """addstart : NUM LITSTR err_list NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]
        self.flag = False

    def p_addstart_third_err_type(self, p):
        """addstart : NUM LITSTR EQSIGN err_list NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        self.flag = False

    def p_err_list_t1(self, p):
        """err_list : err"""
        p[0] = p[1]
        self.flag = False

    def p_err_list_t2(self, p):
        """err_list : """
        p[0] = ''
        self.flag = False

    def p_err_list_t3(self, p):
        """err_list : err_list err"""
        p[0] = p[1] + p[2]
        self.flag = False

    def p_err(self, p):
        """err : ANY"""
        p[0] = p[1]
        self.flag = False

    def p_error(self, p):
        print('Unexpected token: ', p)

    def checkString(self, st):
        self.valname = ''
        self.count = 0
        self.flag = True
        res = self.parser.parse(st)
        return res



