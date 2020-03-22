import ply.yacc as yacc
from checkFLEX import tokens
from checkFLEX import data

def p_addstart(p):
    """addstart : NUM LITSTR EQSIGN digorlit anytail"""
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]


def p_digorlit(p):
    """digorlit : DIGSTR
                | TAILLITSTR"""
    p[0] = p[1]


def p_anytail(p):
    """anytail :
                | tailone
                | anytail tailone"""
    if len(p) == 0:
        p[0] = ''
    elif len(p) == 1:
        p[0] = p[1]
    elif len(p) == 2:
        p[0] = p[1] + p[2]


def p_tailone(p):
    """tailone : OPERSIGN DIGSTR
                | OPERSIGN TAILLITSTR"""
    p[0] = p[1] + p[2]


def p_error(p):
    print('Unexpected token: ', p)


parser = yacc.yacc(optimize=1, debug=False, write_tables=False)
result = parser.parse(data)

