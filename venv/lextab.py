# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('DIVIDE', 'ELSE', 'ID', 'IF', 'LPAREN', 'MINUS', 'NUMBER', 'PLUS', 'RPAREN', 'THEN', 'TIMES', 'WHILE'))
_lexreflags   = 64
_lexliterals  = '{}'
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_ID>(([_A-Za-z])(([0-9])|([_A-Za-z]))*))|(?P<t_COMMENT>\\#.*)|(?P<t_NUMBER>\\d+)|(?P<t_newline>\\n+)|(?P<t_lbrace>\\{)|(?P<t_rbrace>\\})|(?P<t_PLUS>\\+)|(?P<t_TIMES>\\*)|(?P<t_LPAREN>\\()|(?P<t_RPAREN>\\))|(?P<t_MINUS>-)|(?P<t_DIVIDE>/)', [None, ('t_ID', 'ID'), None, None, None, None, None, ('t_COMMENT', 'COMMENT'), ('t_NUMBER', 'NUMBER'), ('t_newline', 'newline'), ('t_lbrace', 'lbrace'), ('t_rbrace', 'rbrace'), (None, 'PLUS'), (None, 'TIMES'), (None, 'LPAREN'), (None, 'RPAREN'), (None, 'MINUS'), (None, 'DIVIDE')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {'INITIAL': 't_eof'}
