
class DataBase:
    def __init__(self):
        self.claves = {}
    
    def agg_clave(self,clave):
        self.claves[clave] = []

    def agg_valor(self, pos, valor):
        clave = list(self.claves.keys())[pos]
        self.claves[clave].append(valor)

    def conteo(self):
        clave = list(self.claves.keys())[0]
        return len(self.claves[clave])
    
    def contarsi(self,clave,valor):
        return self.claves[clave].count(valor)
    
    def max(self,clave):
        return max(self.claves[clave])
    
    def min(self,clave):
        return min(self.claves[clave])
    
    def datos(self):
        texto = ""
        claves = list(self.claves.keys())
        valores = list(self.claves.values())
    
        for clave in claves:
            texto += f"{clave} "
        texto += "\n"

        for i in range(len(valores[0])):
            for lista in valores:
                texto += f"{lista[i]} "
            texto += "\n"
    
        return texto


#"clave":[lista de elementos]

    def sumar(self,clave):
        return sum(self.claves[clave])
        

    def imprimirreg(self):
        print("="*50)
        print("valores")
        for clave in self.claves:
            print(clave,self.claves[clave])


    def promedio(self,clave):
        prom = sum(self.claves[clave])/ len(self.claves)
        return prom
  

    def datos(self):
        texto = ""
        claves = list(self.claves.keys())
        valores = list(self.claves.values())
    
        for clave in claves:
            texto += f"{clave} "
        texto += "\n"

        for i in range(len(valores[0])):
            for lista in valores:
                texto += f"{lista[i]} "
            texto += "\n"
        return texto
    
    def exportarReporte(self,titulo):
        claves = list(self.claves.keys())
        valores = list(self.claves.values())

        nombre_archivo = "reporteHTML.html"
        with open(nombre_archivo, "w") as archivo_html:
            archivo_html.write("<html>")
            archivo_html.write("<head><title>{}</title></head>".format(titulo))
            archivo_html.write("<body>")
            archivo_html.write("<h1>{}</h1>".format(titulo))
            archivo_html.write("<table border='1'>")

            # Encabezados de la tabla
            archivo_html.write("<tr>")
            for clave in claves:
                archivo_html.write("<th>{}</th>".format(clave))
            archivo_html.write("</tr>")

            # Datos de la tabla
            for i in range(len(valores[0])):
                archivo_html.write("<tr>")
                for lista in valores:
                    archivo_html.write("<td>{}</td>".format(lista[i]))
                archivo_html.write("</tr>")

            archivo_html.write("</table>")
            archivo_html.write("</body>")
            archivo_html.write("</html>")
    
        

