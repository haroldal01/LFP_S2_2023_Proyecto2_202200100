import graphviz 
import time 

class Diagrama:
    def __init__(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.dot = graphviz.Digraph(comment=f"Graph {timestr}")
        self.counter = 0
        self.dot.attr(
            "node",
            style = "filled",
            fillcolor = "white",
            fontcolor = "blue",
            shape = "box",
        )

    def agregarnodo(self,valor):
        nombre = f"nodo{self.counter}"
        self.dot.node(nombre,valor)
        self.counter += 1 
        return nombre
    
    def agregarArista(self, nodo1:str, nodo2:str):
        self.dot.edge(nodo1,nodo2)

    def generarGrafica(self):
        self.dot.render("Graficas/Arbol",view=True)
        self.dot.save("Graficas/Arbol.dot")

    def obtenerUltimoNodo(self):
        return f"nodo{self.counter-1}"
    
diagrama = Diagrama()