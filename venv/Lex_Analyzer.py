import ply.lex as lex

class MyLexer(object):
    datafile = "data.txt"

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
        'ID',
    ] + list(reserved.values())

    literals = [ '{', '}']

    # Regular expresion rules for simple tokens
    t_PLUS      = r'\+'
    t_MINUS     = r'-'
    t_TIMES     = r'\*'
    t_DIVIDE    = r'/'
    t_LPAREN    = r'\('
    t_RPAREN    = r'\)'
    t_digit     = r'([0-9])'
    t_nondigit  = r'([_A-Za-z])'

    identifier  = r'(' + t_nondigit + r'(' + t_digit + r'|' + t_nondigit + r')*)'
    # t_ignore_COMMENT = r'\#.*'

    # Rule to match an identifier aof reserved words
    @TOKEN(identifier)
    def t_ID(self, t):
        r'[a-z][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'ID')  # Check for reserved words

        # Look up symbol table information and return a tuple
        # t.value = (t.value, symbol_lookup(t.value))

        return t

    def t_COMMENT(self, t):
        r'\#.*'
        pass
        # No return value. Token discarded

    # A regular expression rules with some action code
    def t_NUMBER(self, t):
        r'\d+'
        t.lexer.num_count += 1  # Using the lexer attribute
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
        raise ("Illegal character '%s' in line '%d' and column '%d'" % (
        t.value[0], t.lexer.lineno, MyLexer.find_column(self, self.lexer.lexdata, t)))
        #t.lexer.skip(1)

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

