import tkinter as tk
from tkinter import *

from tkinter.filedialog import askopenfilename
from tkinter import scrolledtext
from analizador import *
from pparser import Parser
import webbrowser



# Función para copiar el texto de la izquierda al cuadro de texto de la derecha
def actualizar_texto():
    texto = cuadro_texto.get("1.0", "end-1c")
    texto_a_la_derecha.configure(state='normal')  # Habilita la edición del cuadro de texto de la derecha
    texto_a_la_derecha.delete("1.0", tk.END)  # Borra el contenido actual del cuadro de texto de la derecha
    texto_a_la_derecha.insert(tk.END, "")
    texto_a_la_derecha.configure(state='disabled')

# Función para abrir un archivo
def abrir_archivo():
    filepath = askopenfilename(filetypes=[("BIZDATA Files","*.bizdata")])
    if not filepath:
        return

    try:
        archivo_nombre = filepath  
        with open(archivo_nombre, "r") as archivo:
            contenido = archivo.read()
        cuadro_texto.delete(1.0, tk.END)
        cuadro_texto.insert(tk.END, contenido)
        
    except FileNotFoundError:
        cuadro_texto.delete(1.0, tk.END)  # Borra el contenido actual del cuadro de texto
        cuadro_texto.insert(tk.END, "Archivo no encontrado")
        actualizar_texto()  # Actualiza el cuadro de texto de la derecha

# Función para analizar el texto
def analizar_texto():
    texto_a_analizar = cuadro_texto.get("1.0", "end-1c")
    tokens = tokenizar_entrada(texto_a_analizar)
    print("="*50)
    for i in tokens:
        print(i)
    print("="*50)

    parser = Parser(tokens)
    parser.parse()

  
    texto_a_mostrar = str(parser.devolver_text())
    texto_a_la_derecha.configure(state='normal')
   
    texto_a_la_derecha.insert(tk.END,texto_a_mostrar)
    

def generar_reporte_errores():
    if not errores:
        return
    nombrearchivo = "reporte_errores.html" 
    
    with open(nombrearchivo, "w") as archivo_html:
        archivo_html.write("<html>")
        archivo_html.write("<head><title>Reporte de Errores</title></head>")
        archivo_html.write("<body>")
        archivo_html.write("<h1>Reporte de Errores</h1>")
        archivo_html.write("<table border='1'>")
        archivo_html.write("<tr><th>Caracter</th><th>Línea</th><th>Columna</th></tr>")

        # Generar filas de la tabla con datos de errores
        for error in errores:
            archivo_html.write(f"<tr><td>{error.character}</td><td>{error.line}</td><td>{error.column}</td></tr>")

        archivo_html.write("</table>")
        archivo_html.write("</body>")
        archivo_html.write("</html>")
        webbrowser.open(nombrearchivo)

def generar_reporte_tokens():
    if not tokens_resultantes:
        return

    nombre_archivo = "reporte_tokens.html"

    with open(nombre_archivo, "w") as archivo_html:
        archivo_html.write("<html>")
        archivo_html.write("<head><title>Reporte de Tokens</title></head>")
        archivo_html.write("<body>")
        archivo_html.write("<h1>Reporte de Tokens</h1>")
        archivo_html.write("<table border='1'>")
        archivo_html.write("<tr><th>Nombre</th><th>Valor</th><th>Fila</th><th>Columna</th></tr>")

        for token in tokens_resultantes:
            archivo_html.write(f"<tr><td>{token.nombre}</td><td>{token.valor}</td><td>{token.fila}</td><td>{token.columna}</td></tr>")

        archivo_html.write("</table>")
        archivo_html.write("</body>")
        archivo_html.write("</html>")

        webbrowser.open(nombre_archivo)

ventana = tk.Tk()
ventana.title("Proyecto 2 - 202200100")
ventana.geometry("900x650")

frame_derecha = tk.Frame(ventana, width=400, height=400)
frame_derecha.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
frame_derecha.pack_propagate(False)

cuadro_texto = tk.Text(ventana, bg="#f8f9fa", foreground="#343a40",
            insertbackground="#3b5bdb", selectbackground="blue",
            width=50, height=30, font=("Courier New", 13))
cuadro_texto.pack(fill=tk.BOTH, expand=False)

texto_a_la_derecha = scrolledtext.ScrolledText(frame_derecha, wrap=tk.WORD, width=50, height=30, font=("Courier New", 13), bg="white", fg="black")

texto_a_la_derecha.pack(fill=tk.BOTH, expand=True)

# Crear un menú desplegable "Archivo"
barra_menu = tk.Menu(ventana)
opmenu = tk.Menu(barra_menu, tearoff=0)
opmenu.add_command(label="Reporte de Tokens",command=generar_reporte_tokens)
opmenu.add_command(label="Reporte de Errores", command=generar_reporte_errores)
opmenu.add_command(label="Ärbol de derivación")
opmenu.add_separator()
opmenu.add_command(label="Salir", command=ventana.quit)
barra_menu.add_cascade(label="Reportes", menu=opmenu)
ventana.config(menu=barra_menu)

boton_actualizar = tk.Button(ventana, text="Actualizar", command=actualizar_texto, bg="blue", fg="white", font=("Arial", 12))
boton_actualizar.place(x=145, y=610)

boton_abrir = tk.Button(ventana, text="Abrir", command=abrir_archivo, bg="blue", fg="white", font=("Arial", 12))
boton_abrir.place(x=50, y=610)

boton_analizar = tk.Button(ventana, text="Analizar", command=analizar_texto, bg="blue", fg="white", font=("Arial", 12))
boton_analizar.place(x=255, y=610)

ventana.mainloop()
