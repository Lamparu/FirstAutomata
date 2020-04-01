import ply.lex as lex
import re


class LexerClass:
    tokens = (
        'NUM', 'LITSTR', 'DIGSTR', 'EQSIGN',
        'OPERSIGN', 'NL', 'ANY'
    )

    states = (
        ('string', 'exclusive'),
    )

    t_ignore = ''
    t_string_ignore = ''

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def input(self, smth):
        return self.lexer.input(smth)

    def token(self):
        return self.lexer.token()

    def t_string_OPERSIGN(self, t):
        r'[ ]+(\+|\-|\*|\/)[ ]+'
        return t

    def t_ANY_LITSTR(self, t):
        r'[a-zA-Z][a-zA-Z0-9]{0,15}'
        return t

    def t_NUM(self, t):
        r'[ ]*[1-9][0-9]*[ ]+'
        t.lexer.begin('string')
        return t

    def t_string_DIGSTR(self, t):
        r'\-?[1-9][0-9]{0,15}'
        return t

    def t_string_EQSIGN(self, t):
        r'[ ]+\=[ ]+'
        return t

    def t_ANY_NL(self, t):
        r'[ ]*\n'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_ANY_ANY(self, t):
        r'.+'
        t.lexer.begin('INITIAL')
        return t

    # Обработка ошибок
    def t_error(self, t):
        print("Illegal character '%s' " % t.value[0])
        t.lexer.skip(1)
        t.lexer.begin('INITIAL')
        return t

    def t_string_error(self, t):
        print("Illegal character '%s' " % t.value[0])
        t.lexer.skip(1)
        t.lexer.begin('INITIAL')
        return t


data = '''8 kS = 768768 + gjhg
'''
# l = LexerClass()
# l.input(data)
# while True:
#     tok = l.token()
#     if not tok:
#         break
#     print(tok)
