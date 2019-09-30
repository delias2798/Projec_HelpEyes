import Lex_Analyzer
import Yacc_Parser
import ply.lex as lex
import json

datafile = "data.txt"
f = open(datafile)
data = f.read()
f.close()

print("---------------------------------- Lexing ----------------------------------")
m = Lex_Analyzer.MyLexer()
m.build()
m.test(data)
print(m.get_tokens())
print("---------------------------------- Parsing ----------------------------------")
p = Yacc_Parser.MyParser(m)
p.build()
p.test(data)
p.create_json()

print("---------------------------------- Transfering data ----------------------------------")


#with open('json_Test.json') as f:

 #   config = json.load(f)
  #  print(config["1"])


