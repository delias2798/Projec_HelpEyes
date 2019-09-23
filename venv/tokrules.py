import Lex_Analyzer
import Yacc_Parser
import ply.lex as lex

datafile = "data.txt"
f = open(datafile)
data = f.read()
f.close()

print("---------------------------------- Lexing ----------------------------------")
m = Lex_Analyzer.MyLexer()
m.build()
m.test(data)
print("---------------------------------- Parsing ----------------------------------")
p = Yacc_Parser.MyParser()
p.test(data)
