import ply.lex as lex
import re


class LexerClass:
    tokens = (
        'NUM', 'LITSTR', 'TAILLITSTR', 'DIGSTR', 'EQSIGN', 'OPERSIGN', 'NL', 'ANY'
    )

    states = (
        ('valname', 'exclusive'),
        ('tail', 'exclusive'),
    )

    t_tail_OPERSIGN = r'[ ]+[\+|\-|\*|\/][ ]+'
    t_tail_TAILLITSTR = r'\-?[a-zA-Z][a-zA-Z0-9]{0,15}'
    t_tail_DIGSTR = r'\-?[1-9][0-9]{0,15}'
    t_valname_LITSTR = r'[a-zA-Z][a-zA-Z0-9]{0,15}'

    t_valname_ignore = ''
    t_tail_ignore = ''
    t_ignore = ''

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def input(self, smth):
        return self.lexer.input(smth)

    def token(self):
        return self.lexer.token()

    def t_ANY_NL(self, t):
        r'[ ]*\n'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_NUM(self, t):
        r'[ ]*[1-9][0-9]*[ ]+'
        if t.lexer.current_state() == 'INITIAL':
            t.lexer.begin('valname')
        return t

    def t_ANY_EQSIGN(self, t):
        r'[ ]+\=[ ]+'
        if t.lexer.current_state() == 'valname':
            t.lexer.begin('tail')
        else:
            t.lexer.begin('INITIAL')
        return t

    def t_ANY(self, t):
        r'.+'
        t.lexer.begin('INITIAL')
        return t

    # Обработка ошибок
    def t_error(self, t):
        #print("Illegal character '%s' " % t.value[0])
        t.lexer.skip(1)
        t.lexer.begin('INITIAL')

    def t_valname_error(self, t):
        #print("Illegal character '%s' in VALNAME " % t.value[0])
        t.lexer.skip(1)
        t.lexer.begin('INITIAL')

    def t_tail_error(self, t):
        #print("Illegal character '%s' in TAIL " % t.value[0])
        t.lexer.skip(1)
        t.lexer.begin('INITIAL')


#l = LexerClass()
#data = '''2 a = a + 3-4
#'''
#l.input(data)
#while True:
#    tok = l.token()
#    if not tok:
#        break
#    print(tok)
