import ply.lex as lex
import re

tokens = (
    'NUM', 'LITSTR', 'TAILLITSTR', 'DIGSTR', 'SPACE', 'EQSIGN', 'OPERSIGN'
)

states = (
    ('valname', 'exclusive'),
    ('tail', 'exclusive'),
)

t_ANY_SPACE = r' +'  # TODO: мб стоит еще добавить табуляцию
t_tail_OPERSIGN = r'(\+|\-|\*|\/)'
t_tail_TAILLITSTR = r'\-?[a-zA-Z][a-zA-Z0-9]{0,15}'
t_tail_DIGSTR = r'\-?[1-9][0-9]{0,15}'
t_valname_LITSTR = r'[a-zA-Z][a-zA-Z0-9]{0,15}'

# t_tail_AFTEREQ = r' +\-?(([a-zA-Z][a-zA-Z0-9]{0,15})|[1-9][0-9]*)?( +(\+|\-|\*|\/) +\-?(([a-zA-Z][a-zA-Z0-9]{0,15})|[1-9][0-9]*))* *'

t_valname_ignore = ''
t_tail_ignore = ''
t_ignore = ''

def t_NUM(t):
    r'[1-9][0-9]*'
    if t.lexer.current_state() == 'INITIAL':
        t.lexer.begin('valname')
    return t


def t_ANY_EQSIGN(t):
    r'\='
    if t.lexer.current_state() == 'valname':
        t.lexer.begin('tail')
    else:
        t.lexer.begin('INITIAL')
    return t


#def t_tail_ANY(t):
#    r'.'
#    t.lexer.begin('INITIAL')
#    return t


def t_tail_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('INITIAL')


# Обработка ошибок
def t_error(t):
    print("Illegal character '%s' " % t.value[0])
    t.lexer.skip(1)
    t.lexer.begin('INITIAL')


def t_valname_error(t):
    print("Illegal character '%s' in VALNAME " % t.value[0])
    t.lexer.skip(1)
    t.lexer.begin('INITIAL')


def t_tail_error(t):
    print("Illegal character '%s' in TAIL " % t.value[0])
    t.lexer.skip(1)
    t.lexer.begin('INITIAL')


lexer = lex.lex(reflags=re.UNICODE | re.DOTALL)

data = '''2 a = a - -4
3 d = -d
456 b4ff = 3
-5 a = a
6 7 = a'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
