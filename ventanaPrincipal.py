import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import scrolledtext
from analizador import *
from printer import *
from pparser import Parser



# Función para copiar el texto de la izquierda al cuadro de texto de la derecha
def actualizar_texto():
    texto = cuadro_texto.get("1.0", "end-1c")
    texto_a_la_derecha.configure(state='normal')  # Habilita la edición del cuadro de texto de la derecha
    texto_a_la_derecha.delete("1.0", tk.END)  # Borra el contenido actual del cuadro de texto de la derecha
    texto_a_la_derecha.insert(tk.END, texto)
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
        

        actualizar_texto()  # Actualiza el cuadro de texto de la derecha
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

    #texto_a_imprimir = Printer()

    texto_a_la_derecha.delete("1.0", tk.END)
    #texto_a_la_derecha.insert(tk.END,texto_a_imprimir)

   

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

texto_a_la_derecha = scrolledtext.ScrolledText(frame_derecha, wrap=tk.WORD, width=50, height=30, font=("Courier New", 13), bg="black", fg="white")

texto_a_la_derecha.pack(fill=tk.BOTH, expand=True)

# Crear un menú desplegable "Archivo"
barra_menu = tk.Menu(ventana)
opmenu = tk.Menu(barra_menu, tearoff=0)
opmenu.add_command(label="Nuevo")
opmenu.add_command(label="Abrir", command=abrir_archivo)
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
