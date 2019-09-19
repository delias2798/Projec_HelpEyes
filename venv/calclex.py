# calclex.py
#
# tokenizer for a simple expression evaluator
# for numbers and +,-,*,/
#
import sys
import ply.lex as lex
from ply.lex import TOKEN

class LexerError(Exception): pass

class MyLexer(object):
    datafile = "data.txt"

    states = (
        ('foo', 'inclusive'),
    )

    reserved = {
        'if' : 'IF',
        'for': 'FOR',
        'then' : 'THEN',
        'ELSE' : 'ELSE',
        'while' : 'WHILE',
        'DECLARE': 'DECLARE',
        'IMPORT': 'IMPORT',
        'Object': 'OBJECT',
        'Move': 'MOVE',
        'Vibration': 'VIBRATION',
        'Inclination': 'INCLINATION',
        'Temperature': 'TEMPERATURE',
        'Brightness': 'BRIGHTNESS',
        'Sound': 'SOUND',
        'Dow': 'DOW',
        'Enddo': 'ENDDO',
        'FEnd': 'FEND',
        'CASE': 'CASE',
        'WHEN': 'WHEN',
        'END': 'END',
        'Inc': 'INC',
        'Dec': 'DEC',
        'Call': 'CALL',
        'Procedure': 'PROCEDURE',
        'Begin': 'BEGIN',
        'begin': 'begin',
        'end': 'end',
    }
    #    'Times': 'TIMES',
    #    'THEN': 'THEN',

    # List of token name
    tokens = [
                 'NUMBER',
                 'PLUS',
                 'MINUS',
                 'TIMES',
                 'DIVIDE',
                 'LPAREN',
                 'RPAREN',
                 'VARIABLE',
                 #'COMPLEXID',
             ] + list(reserved.values())

    literals = [ '{', '}']

    # Regular expresion rules for simple tokens
    t_PLUS      = r'\+'
    t_MINUS     = r'-'
    t_TIMES     = r'\*'
    t_DIVIDE    = r'/'
    t_LPAREN    = r'\('
    t_RPAREN    = r'\)'
    r_OR        = r'\|'
    # t_ignore_COMMENT = r'\#.*' r'([_A-Za-z]([0-9]|[_A-Za-z])*)'

    def t_begin_foo(self, t):
        r'start_foo'
        t.lexer.push_state('foo')  # Starts 'foo' state
        print("jahd")

    t_foo_ignore = ' \t'

    # Define a rule so we can track line numbers
    def t_foo_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_foo_end(self, t):
        r'end_foo'
        t.lexer.pop_state()
        print("akjbxs")

    # Error handling rule
    def t_foo_error(self, t):
        print("Illegal character '%s'" % (t.value[0]))
        t.lexer.skip(1)

    # Rule to match an identifier of reserved words
    def t_ID(self, t):
        r'[a-z][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'VARIABLE') #Check for reserved words

        # Look up symbol table information and return a tuple
        # t.value = (t.value, symbol_lookup(t.value))

        return t

    """def t_COMPLEXID(self, t):
        r'[A-Z][a-zA-Z_0-9]*'
        print("pass")
        t.type = self.reserved.get(t.value, 'COMPLEXID')

        print(t.value, t.type)"""

    def t_COMMENT(self, t):
        r'\#.*'
        pass
        # No return value. Token discarded

    # A regular expression rules with some action code
    def t_NUMBER(self, t):
        r'\d+'
        t.lexer.num_count += 1   # Using the lexer attribute
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    # A string containing ignored characters (spaces ad tabs)
    t_ignore = ' \t'

    def t_lbrace(self, t):
        r'\{'
        t.type = '{'    # Set token type to the expected literal
        return t

    def t_rbrace(self, t):
        r'\}'
        t.type = '}'    # Set token type to the expected literal
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
        print("Illegal character '%s' in line '%d' and column '%d'" % (t.value[0], t.lexer.lineno, MyLexer.find_column(self, self.lexer.lexdata, t)))
        #sys.exit()
        n = 1
        m = ""
        #if t.value[0] != '':
         #   print("space") quedé en comfigurar que salte la palabra completa para que la imprima y luego corte la vara

        while t.value[n].isspace():
            n+=1
            m+=t.value[n]

        #if t.value[5].isspace():
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

# Build the lexer
# Alternative flags: Debug=1, compile=1
#lexer = lex.lex()

n = """
#test it out
f = open(datafile)
data = f.read()
f.close()


#Give the lexer some input
#lexer.input(data)

for tok in lexer:
    print(tok)
print("hola")

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break # No more input
    print(tok, tok.type, tok.value, tok.lineno, tok.lexpos)
"""
#if __name__ == '__main__':
#    lex.runmain()

