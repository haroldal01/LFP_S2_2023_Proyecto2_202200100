from collections import namedtuple


Token = namedtuple("Token",["nombre","valor","fila","columna"])
fila = 1
columna = 1 
tokens = []
errores = []
tokens_resultantes = []


palabras_reservadas = {
    "imprimir": "IMPRIMIR",
    "Claves": "CLAVES",
    "Registros":"REGISTROS",
    "imprimirln":"IMPRIMIRLN",
    "conteo":"CONTEO",
    "promedio":"PROMEDIO",
    "contarsi":"CONTARSI",
    "datos":"DATOS",
    "sumar":"SUMAR",
    "max":"MAX",
    "min":"MIN",
    "exportarReporte":"EXPORTARREPORTE",
    "(":"PARENTESISIZQ",
    ")":"PARENTESISDER",
    "[":"CORCHETEIZQ",
    "]":"CORCHETEDER",
    "{":"LLAVEIZQ",
    "}":"LLAVEDER",
    ",":"COMA",
    ";":"PUNTOYCOMA",
    ":":"DOSPUNTOS",
    "'''":"COMENTARIO_MULTILINEA",
    "#":"COMENTARIO",
    "=":"IGUAL", 
}


class Error():
    def __init__(self,character,line,column):
        self.character = character
        self.line = line
        self.column = column


def stringt(entrada,i):
    token = ""
    for char in entrada:
        if char == '"':
            return [token,i]
        token += char
        i+=1
    print("no se cerró")


def numerot(entrada,i):
    token = ""
    esdecimal = False
    for char in entrada:
        if char.isdigit():
            token += char
            i += 1
        elif char == "." and not esdecimal:
            token += char
            i += 1 
            esdecimal = True
        else:
            break
    if esdecimal:
        return [float(token),i]
    return [int(token),i]



def tokenizar_entrada(entrada):
    global fila, columna
    #tokens_resultantes = []
    i = 0
    while i < len(entrada):
        char = entrada[i]
        if char.isspace():
            if char == "\n":
                fila += 1 
                columna = 1  
            elif char == "\t":
                columna += 4
            else:
                columna += 1 
            i += 1 

        elif char == "#":
            while i < len(entrada) and entrada[i] != "\n":
                i += 1 
            fila += 1
            columna = 1  

        elif char == '"':
            string, pos = stringt(entrada[i+1:], i)
            columna += len(string) + 1
            i = pos + 2
            token = Token("STRING", string, fila, columna)
            tokens_resultantes.append(token)

        elif char.isalpha():
            j = i
            while j < len(entrada) and entrada[j].isalpha():
                j += 1
            palabra = entrada[i:j]
            if palabra in palabras_reservadas:
                columna += len(palabra)
                token = Token(palabras_reservadas[palabra],palabra, fila, columna)
                tokens_resultantes.append(token)
            i = j

        elif char.isdigit():
            numero, pos = numerot(entrada[i:], i)
            columna += pos - 1 
            i = pos
            token = Token("NUMERO", numero, fila, columna)
            tokens_resultantes.append(token)

        elif char in palabras_reservadas:
            columna += 1
            token = Token(palabras_reservadas[char], char, fila, columna)
            tokens_resultantes.append(token)
            i += 1 
        
        elif char == "'":
            i += 3  # Saltar las tres comillas iniciales
            while i < len(entrada) and entrada[i:i + 3] != "'''":
                if entrada[i] == "\n":
                    fila += 1
                    columna = 1
                i += 1
            if i < len(entrada):
                i += 3  # Saltar las tres comillas finales



        else:
            error = Error(char, fila, columna)
            errores.append(error)
            print(f"Caracter desconocido: {char}, encontrado en la fila {fila+1} y columna {columna+1}")
            i += 1
            columna += 1
    return tokens_resultantes


#falta lo de los comentarios multilinea
