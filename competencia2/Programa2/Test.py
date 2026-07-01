from antlr4 import*
from ExprLexer import ExprLexer
import sys
# Pobre ingeniero solo
# leer archivos
input_stream = FileStream(sys.argv[1])

# Por terminal
lexer = ExprLexer(input_stream)

tokens = CommonTokenStream(lexer)
tokens.fill()
print(tokens)

for token in tokens.tokens:
    print("Texto :", token.text)
    print("Linea :", token.line)
    print("Columna :", token.column)
    nombre_token = lexer.symbolicNames[token.type]
    print("Tipo ", nombre_token)
    print("----------------------")