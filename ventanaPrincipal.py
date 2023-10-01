import tkinter as tk

def actualizar_label():
    texto = cuadro_texto.get("1.0", "end-1c")  # se obtiene todo el texto igual que en el cuadro de texto
    etiqueta.config(text=texto)


ventana = tk.Tk()
ventana.title("Proyecto 2 - 202200100")
ventana.geometry("900x650")

frame_derecha = tk.Frame(ventana, width=400, height=400)
frame_derecha.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
frame_derecha.pack_propagate(False)


cuadro_texto = tk.Text(ventana, bg="#f8f9fa",
            foreground="#343a40",
            insertbackground="#3b5bdb",
            selectbackground="blue",
            width=90,
            height=30,
            font=("Courier New", 13),)
cuadro_texto.pack(fill=tk.BOTH, expand=False)


etiqueta = tk.Label(frame_derecha, text="", justify=tk.LEFT, wraplength=350)
etiqueta.pack(fill=tk.BOTH, expand=True)

#se crea un objeto de menú
barra_menu = tk.Menu(ventana)

# Crear un menú desplegable "Archivo"
opmenu = tk.Menu(barra_menu, tearoff=0)
opmenu.add_command(label="Nuevo")
opmenu.add_command(label="Abrir")
opmenu.add_separator()
opmenu.add_command(label="Salir", command=ventana.quit)

#se agrega el menú  a la barra de menú
barra_menu.add_cascade(label="Reportes", menu=opmenu)

# Configurar la ventana para usar la barra de menú
ventana.config(menu=barra_menu)

#botones 
boton_actualizar = tk.Button(ventana, text="Actualizar", command=actualizar_label,bg="blue", fg="white", font=(15))
boton_actualizar.place(x=155,y=610)

boton_abrir = tk.Button(ventana, text="Abrir",bg="blue", fg="white", font=(15))
boton_abrir.place(x=100,y=610)

boton_analizar = tk.Button(ventana, text="Analizar",bg="blue", fg="white", font=(15))
boton_analizar.place(x=245,y=610)


ventana.mainloop()

