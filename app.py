from analizador import *
from pparser import Parser
from printer import *



entrad = open("C:/Users/81vv00k9gj/Downloads/prueba2.bizdata","r").read()

tokens = tokenizar_entrada(entrad)

print("="*50)
for i in tokens:
        print(i)
print("="*50)

parser = Parser(tokens)
parser.parse()

print("_______________________________________")
printer = Printer()
print(printer.get_text())
print("_______________________________________")