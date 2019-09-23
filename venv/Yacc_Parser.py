# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from Lex_Analyzer import MyLexer

class MyParser:

    def p_binary_operators(self, p):
        """expression : expression PLUS term
                        | expression MINUS term
                        | term
            term :      term TIMES factor
                        | term DIVIDE factor
                        | factor
                        """
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]


    def p_expression_term(self, p):
        'expression : term'
        p[0] = p[1]

    def p_term_factor(self, p):
        'term : factor'
        p[0] = p[1]

    def p_factor_num(self, p):
        'factor : NUMBER'
        p[0] = p[1]

    def p_factor_expr(self, p):
        'factor : LPAREN expression RPAREN'
        p[0] = p[2]


    # Error rule for syntax errors
    def p_error(self, p):
        print("Syntax error in input!")

    # Build the parser
    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def test(self, data):
        while True:
            try:
                s = input('calc < ')
            except EOFError:
                break
            if not s: continue
            result = self.parser.parse(self, s)
            print(result)
