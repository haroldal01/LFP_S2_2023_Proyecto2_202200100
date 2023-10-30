from printer import Printer
from database import DataBase
from analizador import *
from diagrama import diagrama

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens 
        self.indice = 0
        self.printer = Printer()
        self.db = DataBase()
        self.ultimaInstruccion = None

    def consume(self):
        token = self.tokens[self.indice]
        self.indice += 1 
        return token
    
    def peek(self):
        return self.tokens[self.indice] 
    
    def parse(self):
        raiz = diagrama.agregarnodo("INICIO")
        self.ultimaInstruccion = raiz


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
            else:
                print("se esperaba una instrucción")
                error = Error(self.consume(),self.indice,self.indice)
                errores.append(error)

                return
            
            print(self.ultimaInstruccion)
            if self.indice <len(self.tokens):
                self.ultimaInstruccion = diagrama.agregarnodo("LISTA_INSTRUCCIONES")
                diagrama.agregarArista(raiz,self.ultimaInstruccion)
                raiz = self.ultimaInstruccion

        texto = self.printer.get_text()
        for linea in texto.split("\n"):
            print("\033[32m" + "" + linea + "\033[0m")

    def devolver_text(self):
        texto_devuelto = self.printer.get_text()
        return texto_devuelto 

    def imprimir(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            print("se esperaba que abriera un parentesis")
            return
    
        token = self.consume()
        if token.nombre != "STRING":
            print("se esperaba una cadena de texto")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return

        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un cierre de parentesis")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("se esperaba un punto y coma")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        raiz = diagrama.agregarnodo("INSTRUCCION")
        instruccion = diagrama.agregarnodo("IMPRIMIR")
        diagrama.agregarArista(raiz,instruccion)
        diagrama.agregarArista(instruccion,diagrama.agregarnodo("PARENTESISIZQ"))
        diagrama.agregarArista(instruccion,diagrama.agregarnodo(token.valor))
        diagrama.agregarArista(instruccion,diagrama.agregarnodo("PARENTESISDER"))
        diagrama.agregarArista(instruccion,diagrama.agregarnodo("PUNTOYCOMA"))
        diagrama.agregarArista(self.ultimaInstruccion,raiz)
        self.printer.add(token.valor)


    def imprimirln(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba que abriera un parentesis")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        token = self.consume()
        if token.nombre != "STRING":
            print("se esperaba una cadena de texto")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return

        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un cierre de parentesis")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("se esperaba un punto y coma")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        self.printer.add_line(token.valor)


    def claves(self):
        self.consume()
        if self.consume().nombre != "IGUAL":
            print("se esperaba un igual")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return

        if self.consume().nombre != "CORCHETEIZQ":
            print("se esperaba un corchete de cierre")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un valor de clave")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        valor = self.consume().valor 
        self.db.agg_clave(valor)

        while self.peek().nombre == "COMA":
            self.consume()
            if self.peek().nombre != "STRING":
                print("se esperaba un valor de clave")
                error = Error(self.consume(),self.indice,self.indice)
                errores.append(error)
                return
            valor = self.consume().valor
            self.db.agg_clave(valor)

        if self.consume().nombre != "CORCHETEDER":
            print("se esperaba un corchete de cierre")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        

    def registros(self):
        self.consume()
        if self.consume().nombre != "IGUAL":
            print("se esperaba un igual")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "CORCHETEIZQ":
            print("se esperaba un corchete izquierdo")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        while self.peek().nombre == "LLAVEIZQ":
            self.consume()
            contador = 0

            if self.peek().nombre != "STRING" and self.peek().nombre != "NUMERO":
                print("se esperaba un valor de clave")
                error = Error(self.consume(),self.indice,self.indice)
                errores.append(error)
                return

            valor = self.consume().valor 
            self.db.agg_valor(contador,valor)
            contador += 1 

            while self.peek().nombre == "COMA":
                self.consume()
                if self.peek().nombre != "STRING" and self.peek().nombre != "NUMERO":
                    print("se esperaba un valor de clave2")
                    error = Error(self.consume(),self.indice,self.indice)
                    errores.append(error)
                    return
                valor = self.consume().valor 
                self.db.agg_valor(contador,valor)
                contador += 1 

            if self.peek().nombre != "LLAVEDER":
                print("se esperaba una llave derecha")
                error = Error(self.consume(),self.indice,self.indice)
                errores.append(error)
                return
            self.consume()
        self.consume()

        self.db.imprimirreg()

    def conteo(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izquierdo")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("se esperaba un punto y coma")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        self.printer.add_line(str(self.db.conteo()))

    def contarsi(self):
        
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un paren izq")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un string")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return 
        clave = self.consume().valor
        if self.consume().nombre != "COMA":
            print("se esperaba una coma")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.peek().nombre != "STRING" and self.peek().nombre != "NUMERO":
            print("se esperaba un valor de clave")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        valor = self.consume().valor 
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("SE ESPERABA UN PUNTO Y COMA")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        self.printer.add_line(str(self.db.contarsi(clave,valor)))

    def max(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izq")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un string")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return 
        clave = self.consume().valor
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("SE ESPERABA UN PUNTO Y COMA")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        self.printer.add_line(str(self.db.max(clave)))


    def min(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izq")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un string")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return 
        clave = self.consume().valor
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("SE ESPERABA UN PUNTO Y COMA")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        self.printer.add_line(str(self.db.min(clave)))

    def promedio(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izq")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un string")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return 
        clave = self.consume().valor
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("SE ESPERABA UN PUNTO Y COMA")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        self.printer.add_line(str(self.db.promedio(clave)))


    def datos(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izq")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("se esperaba un punto y coma")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        self.printer.add_line(str(self.db.datos()))



    def sumar(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izq")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un string")
            return 
        clave = self.consume().valor
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("SE ESPERABA UN PUNTO Y COMA")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        self.printer.add_line(str(self.db.sumar(clave)))


    def exportarReporte(self):
        self.consume()
        if self.consume().nombre != "PARENTESISIZQ":
            print("se esperaba un parentesis izq")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.peek().nombre != "STRING":
            print("se esperaba un string")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return 
        titulo = self.consume().valor
        
        if self.consume().nombre != "PARENTESISDER":
            print("se esperaba un parentesis derecho")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        if self.consume().nombre != "PUNTOYCOMA":
            print("SE ESPERABA UN PUNTO Y COMA")
            error = Error(self.consume(),self.indice,self.indice)
            errores.append(error)
            return
        
        self.printer.add_line(str(self.db.exportarReporte(titulo)))










