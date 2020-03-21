import ply.lex as lex
import re

tokens = (
    'STRNUM', 'VALNAME', 'LITSTR', 'OPERSIGN', 'EQSIGN', 'MINSIGN', 'SPACE'
)

t_STRNUM = r'[0-9]+'
t_VALNAME = r'[a-zA-Z][a-zA-Z0-9]{0,15}'
t_LITSTR = r'([a-zA-Z][a-zA-Z0-9]{0,15}|[1-9][0-9]{0,15})'
t_MINSIGN = r'\-'  # TODO: отдельно?
t_EQSIGN = r'\='
t_OPERSIGN = r'(\+|\-|\*|\/)'
t_SPACE = r' '  # TODO: мб стоит еще добавить табуляцию


def t_error(t):
    print("Illegal character '%s' " % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex(reflags = re.UNICODE | re.DOTALL)

data = '2 a = a + -4'

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
