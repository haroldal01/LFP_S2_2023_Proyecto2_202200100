# Manual Técnico



## Estructura de la Clase `Error`

La clase `Error` se utiliza para representar errores léxicos que ocurren durante el análisis del código fuente. Cada instancia de `Error` contiene tres atributos:
- `character`: el carácter que generó el error.
- `line`: el número de línea en la que se encontró el error.
- `column`: la posición de la columna donde se encontró el error.

## Función `stringt(entrada, i)`

Esta función se utiliza para reconocer cadenas de texto (strings) dentro del código fuente. Toma como argumentos `entrada`, que es el fragmento de código a analizar, y `i`, que es la posición actual en `entrada`. La función recorre `entrada` caracter por caracter hasta encontrar una comilla doble ("). Cuando encuentra la comilla de cierre, devuelve una lista con dos elementos: el valor de la cadena y la posición actual `i`. Si no encuentra el cierre de la cadena, imprime "no se cerró".

## Función `numerot(entrada, i)`

Esta función se encarga de reconocer números (tanto enteros como decimales) en el código fuente. Al igual que `stringt`, toma `entrada` y `i` como argumentos. La función recorre `entrada` buscando dígitos y un único punto decimal. Cuando termina de reconocer el número, devuelve una lista con dos elementos: el valor del número y la posición actual `i`.

## Función `tokenizar_entrada(entrada)`

La función `tokenizar_entrada` es la parte principal del análisis léxico. Toma como argumento `entrada`, que es el código fuente completo. La función recorre el código fuente carácter por carácter, identificando diferentes tipos de tokens, como strings, palabras reservadas, números y otros caracteres.

- Si encuentra un espacio en blanco, tabulación o salto de línea, actualiza las variables `fila` y `columna` según corresponda.
- Si encuentra un comentario (línea que comienza con `#`), avanza hasta el final de la línea.
- Si encuentra una comilla doble (`"`), llama a la función `stringt` para reconocer una cadena de texto.
- Si encuentra caracteres alfabéticos (letras), identifica palabras reservadas y crea un token con la palabra y su tipo.
- Si encuentra dígitos, llama a la función `numerot` para reconocer números.
- Si encuentra cualquier otro carácter, genera un error léxico y lo muestra en la consola.

Finalmente, la función devuelve una lista de tokens resultantes, que pueden ser utilizados en etapas posteriores del proceso de compilación.

Este código es una parte esencial del análisis léxico de un compilador o intérprete y se encarga de dividir el código fuente en componentes básicos que facilitan el análisis sintáctico y semántico del programa.


# Explicación del Código del Analizador Sintáctico



## Clase `Parser`

La clase `Parser` es la principal del analizador sintáctico y contiene la lógica para procesar la secuencia de tokens generados por el analizador léxico.

- El constructor de la clase recibe una lista de tokens como entrada.
- La función `consume` avanza al siguiente token en la secuencia y lo devuelve.
- La función `peek` devuelve el siguiente token sin avanzar en la secuencia.
- La función `parse` es el punto de entrada del análisis sintáctico y recorre los tokens para construir un árbol de sintaxis abstracta.

## Análisis de Instrucciones

El analizador identifica diferentes tipos de instrucciones en el código fuente y las procesa. Algunos ejemplos de instrucciones son `IMPRIMIR`, `IMPRIMIRLN`, `CLAVES`, `REGISTROS`, `CONTEO`, `CONTARSI`, `MAX`, `MIN`, `DATOS`, `SUMAR`, `EXPORTARREPORTE` y `PROMEDIO`.

- Cada tipo de instrucción es procesado por una función específica.
- Por ejemplo, la función `imprimir` se encarga de procesar la instrucción `IMPRIMIR`.
- El código utiliza un objeto `diagrama` para construir un árbol de sintaxis abstracta y representar la estructura de las instrucciones.

## Tratamiento de Errores

El código maneja posibles errores sintácticos y léxicos. Si se encuentra una instrucción inesperada o se viola la estructura esperada, se muestra un mensaje de error en la consola.

## Uso de `Printer` y `DataBase`

El código utiliza dos clases adicionales: `Printer` y `DataBase`.
- La clase `Printer` se utiliza para construir un texto que representa el código fuente analizado y se almacena en la variable `texto`.
- La clase `DataBase` se utiliza para almacenar datos y claves durante la ejecución del programa. Puede agregar claves y valores a sus listas internas.

El proceso general consiste en analizar cada instrucción, construir el árbol de sintaxis, y generar una representación del código fuente que se almacena en `Printer`.

## Devolución de Resultados

La función `parse` finaliza generando el texto resultante del análisis sintáctico y lo almacena en la variable `texto_devuelto`. Este texto representa el código fuente procesado y se puede utilizar en etapas posteriores del proceso de compilación.

# Gramática 

INICIO -> LISTA_INSTRUCCIONES
        | EPSILON 

LISTA_INSTRUCCIONES -> INSTRUCCION LISTA_INSTRUCCIONES2

LISTA_INSTRUCCIONES2 -> INSTRUCCION LISTA_INSTRUCCIONES2
					 | Epsilon


INSTRUCCION -> INS_CLAVES
			| INS_REGISTROS
			| INS_IMPRIMIR
			| INS_IMPRIMIRLN
			| INS_CONTEO
			| INS_PROMEDIO
			| INS_CONTARSI
			| INS_DATOS
			| INS_SUMAR
			| INS_MAX
			| INS_MIN
			| INS_EXPORTARREPORTE

INS_CLAVES -> claves igual corchetea LISTA_CLAVES corchetec

LISTA_CLAVES -> cadena LISTA_CLAVES

LISTA_CLAVES -> coma  LISTA_CLAVES
                | Epsilon 

INS_REGISTROS -> registros igual corchetea LISTA_REGISTROS corchetec

LISTA_REGISTROS -> REGISTRO LISTA_REGISTROS

LISTA_REGISTROS -> REGISTRO LISTA_REGISTROS
				| Epsilon 

REGISTRO -> llavea LISTA_VAL_REG llavec

LISTA_VAL_REG -> VAL_REG LISTA_VAL_REG

LISTA_VAL_REG -> coma VAL_REG LISTA_VAL_REG
				| Epsilon 

VAL_REG -> cadena
		| entero
		| decimal

INS_IMPRIMIR -> imprimir parena cadena parenc puntoycoma

INS_IMPRIMIRLN -> imprimirln parena cadena parenc puntoycoma

INS_CONTEO -> conteo parena parenc puntoycoma

INS_PROMEDIO -> promedio parena cadena parenc puntoycoma

INS_CONTARSI -> contarsi parena cadena coma entero parenc puntoycoma

INS_DATOS -> datos parena parenc puntoycoma

INS_SUMAR -> sumar parena cadena parenc puntoycoma

INS_MAX -> max parena cadena parenc puntoycoma

INS_MIN -> min parena cadena parenc puntoycoma

INS_EXPORTARREPORTE-> exportarReporte parena cadena parenc puntoycoma