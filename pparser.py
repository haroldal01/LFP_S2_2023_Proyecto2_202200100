from printer import Printer
from database import DataBase
from analizador import *

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens 
        self.indice = 0
        self.printer = Printer()
        self.db = DataBase()

    def consume(self):
        token = self.tokens[self.indice]
        self.indice += 1 
        return token
    
    def peek(self):
        return self.tokens[self.indice] 
    
    def parse(self):
        while self.indice < len(self.tokens):
            if self.peek().nombre == "IMPRIMIR":
                self.imprimir()
            elif self.peek().nombre == "IMPRIMIRLN":
                self.imprimirln()
            elif self.peek().nombre == "CLAVES":
                self.claves()
            elif self.peek().nombre == "REGISTROS":
                self.registros()
            elif self.peek().nombre == "CONTEO":
                self.conteo()
            elif self.peek().nombre == "CONTARSI":
                self.contarsi()
            elif self.peek().nombre == "MAX":
                self.max()
            elif self.peek().nombre == "MIN":
                self.min()
            elif self.peek().nombre == "DATOS":
                self.datos()
            elif self.peek().nombre == "SUMAR":
                self.sumar()
            elif self.peek().nombre == "EXPORTARREPORTE":
                self.exportarReporte()
            elif self.peek().nombre == "PROMEDIO":
                self.promedio()

            


        texto = self.printer.print()
        for linea in texto.split("\n"):
            print("\033[32m" + "" + linea + "\033[0m")

    def imprimir(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba que abriera un parentesis")
            return
        
        token = self.consume()
        if token.nombre != "STRING":
            print("se esperaba una cadena de texto")
            return

        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un cierre de parentesis")
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("se esperaba un punto y coma")
            return
        
        #print(token.valor)
        self.printer.add(token.valor)


    def imprimirln(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba que abriera un parentesis")
            return
        
        token = self.consume()
        if token.nombre != "STRING":
            print("se esperaba una cadena de texto")
            return

        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un cierre de parentesis")
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("se esperaba un punto y coma")
            return
        
        self.printer.add_line(token.valor)


    def claves(self):
        self.consume()
        if self.consume().nombre != "IGUAL":
            print("se esperaba un igual")
            return

        if self.consume().nombre != "CORCHETEIZQ":
            print("se esperaba un corchete de cierre")
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un valor de clave")
            return
        
        valor = self.consume().valor 
        self.db.agg_clave(valor)

        while self.peek().nombre == "COMA":
            self.consume()
            if self.peek().nombre != "STRING":
                print("se esperaba un valor de clave")
                return
            valor = self.consume().valor
            self.db.agg_clave(valor)

        if self.consume().nombre != "CORCHETEDER":
            print("se esperaba un corchete de cierre")
            return
        

    def registros(self):
        self.consume()
        if self.consume().nombre != "IGUAL":
            print("se esperaba un igual")
            return
        
        if self.consume().nombre != "CORCHETEIZQ":
            print("se esperaba un corchete izquierdo")
            return
        
        while self.peek().nombre == "LLAVEIZQ":
            self.consume()
            contador = 0

            if self.peek().nombre != "STRING" and self.peek().nombre != "NUMERO":
                print("se esperaba un valor de clave")
                return

            valor = self.consume().valor 
            self.db.agg_valor(contador,valor)
            contador += 1 

            while self.peek().nombre == "COMA":
                self.consume()
                if self.peek().nombre != "STRING" and self.peek().nombre != "NUMERO":
                    print("se esperaba un valor de clave2")
                    return
                valor = self.consume().valor 
                self.db.agg_valor(contador,valor)
                contador += 1 

            if self.peek().nombre != "LLAVEDER":
                print("se esperaba una llave derecha")
                return
            self.consume()
        self.consume()

        self.db.imprimirreg()

    def conteo(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izquierdo")
            return
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("se esperaba un punto y coma")
            return
        self.printer.add_line(str(self.db.conteo()))

    def contarsi(self):
        
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un paren izq")
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un string")
            return 
        clave = self.consume().valor
        if self.consume().nombre != "COMA":
            print("se esperaba una coma")
            return
        
        if self.peek().nombre != "STRING" and self.peek().nombre != "NUMERO":
            print("se esperaba un valor de clave")
            return
        valor = self.consume().valor 
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("SE ESPERABA UN PUNTO Y COMA")
            return
        
        self.printer.add_line(str(self.db.contarsi(clave,valor)))

    def max(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izq")
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un string")
            return 
        clave = self.consume().valor
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("SE ESPERABA UN PUNTO Y COMA")
            return
        
        self.printer.add_line(str(self.db.max(clave)))


    def min(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izq")
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un string")
            return 
        clave = self.consume().valor
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("SE ESPERABA UN PUNTO Y COMA")
            return
        
        self.printer.add_line(str(self.db.min(clave)))

    def promedio(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izq")
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un string")
            return 
        clave = self.consume().valor
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("SE ESPERABA UN PUNTO Y COMA")
            return
        
        self.printer.add_line(str(self.db.promedio(clave)))


    def datos(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izq")
            return
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("se esperaba un punto y coma")
            return
        self.printer.add_line(str(self.db.datos()))



    def sumar(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izq")
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un string")
            return 
        clave = self.consume().valor
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("SE ESPERABA UN PUNTO Y COMA")
            return
        
        self.printer.add_line(str(self.db.sumar(clave)))

    def exportarReporte(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izq")
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un string")
            return 
        titulo = self.consume().valor
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("SE ESPERABA UN PUNTO Y COMA")
            return
        
        self.printer.add_line(self.db.exportarReporte(titulo))













