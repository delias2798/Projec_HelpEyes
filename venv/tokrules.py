import Lex_Analyzer
import Yacc_Parser
import ply.lex as lex
import json

class Compiler():
    #datafile = "data.txt"
    def __init__(self):
        self.m = Lex_Analyzer.MyLexer()

    def execute_file(self, datafile):
        f = open(datafile)
        self.data = f.read()
        f.close()

    def start_lexer(self):
        print("---------------------------------- Lexing ----------------------------------")
        self.m.build()
        self.m.test(self.data)
        print(self.m.get_tokens())

    def start_parser(self):
        print("---------------------------------- Parsing ----------------------------------")
        self.p = Yacc_Parser.MyParser(self.m)
        self.p.build()
        self.p.test(self.data)
        self.p.create_json()
        print("---------------------------------- Transfering data ----------------------------------")

    #with open('json_Test.json') as f:

    #   config = json.load(f)
    #  print(config["1"])

comp = Compiler()
comp.execute_file("data.txt")
comp.start_lexer()
comp.start_parser()

