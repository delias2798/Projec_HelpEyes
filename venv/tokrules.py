import calclex
import ply.lex as lex

datafile = "data.txt"
f = open(datafile)
data = f.read()
f.close()

m = calclex.MyLexer()
m.build()
m.test(data)
