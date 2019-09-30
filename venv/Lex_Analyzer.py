# calclex.py
#
# tokenizer for a simple expression evaluator
# for numbers and +,-,*,/
#

import sys
import ply.lex as lex
from ply.lex import TOKEN

class MyLexer(object):
    def __init__(self):

        self.datafile = "data.txt"

        self.reserved = {
            'IF' : 'IF',
            'FOR': 'FOR',
            'THEN' : 'THEN',
            'ELSE' : 'ELSE',
            'WHILE' : 'WHILE',
            'DECLARE': 'DECLARE',
            'IMPORT': 'IMPORT',
            'OBJECT': 'OBJECT',
            'MOVE': 'MOVE',
            'VIBRATION': 'VIBRATION',
            'INCLINATION': 'INCLINATION',
            'TEMPERATURE': 'TEMPERATURE',
            'BRIGHTNESS': 'BRIGHTNESS',
            'SOUND': 'SOUND',
            'DOW': 'DOW',
            'ENDDO': 'ENDDO',
            'FEND': 'FEND',
            'CASE': 'CASE',
            'WHEN': 'WHEN',
            'END': 'END',
            'INC': 'INC',
            'DEC': 'DEC',
            'CALL': 'CALL',
            'PROCEDURE': 'PROCEDURE',
            'BEGIN': 'BEGIN',
            'MAIN': 'MAIN'
        }
    #    'Times': 'TIMES',
    #    'THEN': 'THEN',

        # List of token name
        self.tokens = [
            'NUMBER',
            'PLUS',
            'MINUS',
            'TIMES',
            'DIVIDE',
            'LPAREN',
            'RPAREN',
            'VARIABLE',
            'IDENTIFIER',
            'OPERATOR',
            'EQUAL',
            'ASIGN',
            'COMMENT',
            'WHITE_SPACE',
            'SEMICOLON',
            'KEYWORD',
        ] + list(self.reserved.values())

        self.literals = [ '{', '}']

        # Regular expresion rules for simple tokens
        self.t_PLUS      = r'\+'
        self.t_MINUS     = r'-'
        self.t_TIMES     = r'\*'
        #t_DIVIDE    = r'/'
        self.t_LPAREN    = r'\('
        self.t_RPAREN    = r'\)'
        self.t_EQUAL = r'\='
        self.t_ASIGN = r'\=='
        self.r_OR = r'\|'

    #identifier  = r'(' + t_nondigit + r'(' + t_digit + r'|' + t_nondigit + r')*)'
    # t_ignore_COMMENT = r'\#.*'

    def t_ID(self, t):
        r"""[a-z][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!]|
        [a-z][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!]|
        [a-z][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!]|
        [a-z][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!]|
        [a-z][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!]|
        [a-z][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!]|
        [a-z][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!]|
        [a-z][a-z|A-Z|0-9|_|&|!][a-z|A-Z|0-9|_|&|!]|
        [a-z][a-z|A-Z|0-9|_|&|!]|
        [a-z]"""

        t.type = self.reserved.get(t.value, 'VARIABLE') #Check for reserved words

        # Look up symbol table information and return a tuple
        # t.value = (t.value, symbol_lookup(t.value))

        return t

    def t_KEYWORD(self, t):
        r"""IF|FOR|THEN|ELSE|WHILE|DECLARE|IMPORT|OBJECT|MOVE|VIBRATION
        |INCLINATION|TEMPERATURE|BRIGHTNESS|SOUND|DOW|ENDDO|FEND|CASE|WHEN
        |END|INC|DEC|CALL|PROCEDURE|BEGIN|MAIN"""
        t.type = self.reserved.get(t.value, 'KEYWORD')
        return t

    # Rule to match an identifier aof reserved words
    def t_COMMENT(self, t):
        r'\/\/[\/|a-z|A-Z|0-9|\!|\"|\#|\$|\%|\&|\(|\)|\=|\?|\¡|\¨|\*|\[|\]|\;|\:|\_|\,|\.|\-|\}|\{|\+|\´|\¿|\@|\·|\~|\<|\>\ t]*'
        #pass
        t.type = self.reserved.get(t.value, 'COMMENT')
        return t
        # No return value. Token discarded

    def t_SEMICOLON(self, t):
        r'\;'
        t.type = self.reserved.get(t.value, 'SEMICOLON')
        return t

    def t_DIVIDE(self, t):
        r'\/'
        t.type = self.reserved.get(t.value, 'DIVIDE')
        return t

    # A regular expression rules with some action code
    def t_NUMBER(self, t):
        r'\d+'
        t.lexer.num_count += 1  # Using the lexer attribute
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    #def t_newline(self, t):
    #    r'\n+'
    #    t.lexer.lineno += t.value.count("\n")

    # A string containing ignored characters (spaces ad tabs)
    #t_ignore = ' \t'
    def t_WHITE_SPACE(self, t):
        r'[\ ]+ | [\n]+'
        t.type = self.reserved.get(t.value, 'WHITE_SPACE')
        return t

    def t_lbrace(self, t):
        r'\{'
        t.type = '{'  # Set token type to the expected literal
        return t

    def t_rbrace(self, t):
        r'\}'
        t.type = '}'  # Set token type to the expected literal
        return t

    # EOF (end of file) handling rule
    def t_eof(self, t):
        # Get more input (Example)
        more = self.raw_input(False)
        if more:
            lexer.input(more)
            return lexer.token()
        return None

    def raw_input(self, input):
        if input:
            return input
        else:
            return False

    # Compute column
    #   input is the input text string
    #   token is a token instance
    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s' in line '%d' and column '%d'" % (
        t.value[0], t.lexer.lineno, MyLexer.find_column(self, self.lexer.lexdata, t)))
        sys.exit()
        n = 1
        m = ""
        # if t.value[0] != '':
        #   print("space") quedé en comfigurar que salte la palabra completa para que la imprima y luego corte la vara

        while t.value[n].isspace():
            n += 1
            m += t.value[n]

        # if t.value[5].isspace():
        #    print("hey")
        t.lexer.skip(n)
        print(m)

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.lexer.num_count = 0

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)
        print("Count of number: %d" % self.lexer.num_count)

    def get_tokens(self):
        return self.tokens

