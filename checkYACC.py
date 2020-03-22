import ply.yacc as yacc
from checkFLEX import tokens
from checkFLEX import data

parser = yacc.yacc(optimize=1, debug=True, write_tables=False)
result = parser.parse(data)


def p_add_start(p):
    """addr : NUM LITSTR EQSIGN TAILLITSTR
    | NUM LITSTR EQSIGN DIGSTR"""
    print(p[1]+p[2]+p[3])
