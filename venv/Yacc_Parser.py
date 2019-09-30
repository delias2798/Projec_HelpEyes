# Yacc example

import ply.yacc as yacc
import simplejson as json

# Get the token map from the lexer.  This is required.
from Lex_Analyzer import MyLexer


class MyParser(object):
    #"distance": 100,
    #"temperature": 25,
    #"brightness": 30,
    #"inclination": 40,
    #"sound": 90

    def __init__(self, lex):
        self.lexer = lex
        self.tokens = self.lexer.tokens
        self.global_variables = []
        self.local_variables = []
        self.actions = {}
        self.stack = []
        self.num_action = 0
        self.total_actions = 0
        self.distance = 0
        self.temperature = 0
        self.humidity = 0
        self.sound = 0
        self.brightness = 0
        self.inclination = 0
        self.vibration = 0
        self.speed = 0

    def p_start(self, p):
        """main_struct :    COMMENT imports Declare_var Procedure
        """
        print("start")

    def p_importer(self, p):
        """imports :     IMPORT WHITE_SPACE VARIABLE SEMICOLON imports
                        | WHITE_SPACE imports
                        | WHITE_SPACE
                        | COMMENT
        """
        print("importer")

    def p_procediment(self, p):
        """Procedure :   PROCEDURE Name_procedure Procedure
                        | WHITE_SPACE Procedure
                        | COMMENT Procedure
                        | WHITE_SPACE
                        | COMMENT
        """
        print("Procedure")

    def p_procedureName(self, p):
        """Name_procedure : MAIN WHITE_SPACE LPAREN RPAREN WHITE_SPACE BEGIN fun END SEMICOLON
                            | VARIABLE WHITE_SPACE LPAREN RPAREN WHITE_SPACE BEGIN WHITE_SPACE def_or_fun
                            | MAIN LPAREN RPAREN WHITE_SPACE BEGIN fun END SEMICOLON
                            | VARIABLE LPAREN RPAREN WHITE_SPACE BEGIN WHITE_SPACE def_or_fun
                            | WHITE_SPACE Name_procedure
                            | WHITE_SPACE
         """
        #if p[1] == "MAIN":
        print("procedure name")

    def p_procedureVar(self, p):
        """def_or_fun :    Declare_var fun END SEMICOLON
                            | fun END SEMICOLON
                            """

    def p_funtions(self, p):
        """fun :    OBJECT Close_Var fun
                    | MOVE Close_Var fun
                    | VIBRATION Close_Var fun
                    | INCLINATION Close_Var fun
                    | TEMPERATURE Close_Var fun
                    | BRIGHTNESS Close_Var fun
                    | SOUND Close_Var fun
                    | WHITE_SPACE fun
                    | WHITE_SPACE
                    | COMMENT
                    """
        ##"clientType":"Compilador/Wemos",
        if p[1] == "OBJECT":
            self.stack.append({"distance":str(p[2])})
            self.num_action += 1
            print(self.actions)
        if p[1] == "MOVE":
            self.stack.append({"speed": str(p[2])})
            self.num_action += 1
            print("MOVE %d" % p[2])
        if p[1] == "VIBRATION":
            self.stack.append({"vibration": str(p[2])})
            self.num_action += 1
            print("VIBRATION %d" % p[2])
        if p[1] == "INCLINATION":
            self.stack.append({"inclination": str(p[2])})
            self.num_action += 1
            print("INCLINATION %d" % p[2])
        if p[1] == "TEMPERATURE":
            self.stack.append({"temperature": str(p[2])})
            self.num_action += 1
            print("TEMPERATURE %d" % p[2])
        if p[1] == "BRIGHTNESS":
            self.stack.append({"brightness": str(p[2])})
            self.num_action += 1
            print("BRIGHTNESS %d" % p[2])
        if p[1] == "SOUND":
            self.stack.append({"sound": str(p[2])})
            self.num_action+=1
            print("SOUND %d" % p[2])


    def p_var_var(self, p):
        """Close_Var :   LPAREN VARIABLE RPAREN SEMICOLON
		"""
        p[0] = 5

    def p_var_num(self, p):
        """Close_Var :   LPAREN NUMBER RPAREN SEMICOLON"""
        p[0] = int(p[2])

    def p_defineN(self, p):
        """Declare_var :    DECLARE WHITE_SPACE VARIABLE EQUAL NUMBER SEMICOLON Declare_var
                        | WHITE_SPACE Declare_var
                        | WHITE_SPACE
                        | COMMENT
        """
        if(len(p) > 7):
            if(not self.find_var(p[3])):
                self.local_variables

        print("define Number")

    def p_defineV(self, p):
        """Declare_var :    DECLARE WHITE_SPACE VARIABLE SEMICOLON Declare_var

        """
        print("define variable")

    def find_var(self, new_var):
        if (len(self.local_variables) != 0):
            for n in self.local_variables:
                if n == new_var:
                    return True

        else:
            return False

    #def p_variable(self, p):
    #    """VARIABLE"""

    #def p_binary_operators(self, p):
    #    """ expression : expression PLUS term
    #                    | expression MINUS term
    #        term :      term TIMES factor
    #                   | term DIVIDE factor
    #                    """
    #    if p[2] == '+':
    #        p[0] = p[1] + p[3]
    #    elif p[2] == '-':
    #        p[0] = p[1] - p[3]
    #    elif p[2] == '*':
    #        p[0] = p[1] * p[3]
    #    elif p[2] == '/':
    #        p[0] = p[1] / p[3]

    n="""def p_binary_operators_spaces(self, p):
        "" expression : expression WHITE_SPACE PLUS WHITE_SPACE term
                        | expression WHITE_SPACE MINUS WHITE_SPACE term
            term :      term WHITE_SPACE TIMES WHITE_SPACE factor
                        | term WHITE_SPACE DIVIDE WHITE_SPACE factor
                        ""
        if p[3] == '+':
            p[0] = p[1] + p[4]
        elif p[3] == '-':
            p[0] = p[1] - p[4]
        elif p[3] == '*':
            p[0] = p[1] * p[4]
        elif p[3] == '/':
            p[0] = p[1] / p[4]


    def p_expression_term(self, p):
        'expression : term'
        p[0] = p[1]

    def p_term_factor(self, p):
        ""term : factor""
        p[0] = p[1]

    def p_factor_num(self, p):
        'factor : NUMBER'
        p[0] = p[1]

    def p_factor_expr(self, p):
        'factor : LPAREN WHITE_SPACE expression RPAREN'
        p[0] = p[3]"""


    # Error rule for syntax errors
    def p_error(self, p):
        if p == None:
            token = "end of file"
        else:
            token = f"{p.type}({p.value}) on line {p.lineno}"

        print(f"Syntax error: Unexpected {token}")

    # Build the parser
    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def create_json(self):
        counter = 1

        status_sensors = {"distance": str(self.distance),
         "temperature": str(self.temperature),
         "humidity": str(self.humidity),
         "sound": str(self.sound),
         "brightness": str(self.brightness),
         "inclination": str(self.inclination),
         "vibration": str(self.vibration),
         "speed": str(self.speed)}

        self.actions["clientType"] = "Compilador"
        while (len(self.stack) > 0):
            new_input = self.stack.pop()
            self.actions[str(counter)] = new_input
            #print(self.actions)
            #print(status_sensors)
            counter += 1

    def write_json(self):
        fff = json.dumps(self.actions)
        with open('json_Test.json', 'w') as f:
            f.write(fff)

    def test(self, data):
        while True:
            try:
                #s = input(data)
                #s = self.parser.
                if not data: break
                # if not s: continue
                result = self.parser.parse(data)
                print(result)
                break
            except EOFError:
                break
        self.create_json()
        self.write_json()
        #print(self.actions)