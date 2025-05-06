# Software-Analisis-sintactico.

Juan Carlos Ortiz
ISIC
6to Semestre

#####Funcionamiento del codigo:#####

#Objetivo del software: 


De manera resumida lo que hace el analizador es analizar y evalúar expresiones aritméticas usando la libreria PLY. Detecta números, operadores y paréntesis, de igual manera verifica la estructura con reglas gramaticales y muestra el resultado o errores si la expresión es inválida. En este codigo se implementan diferentes operadores como if, else, while, etc, que si bien no funcionan como en un codigo, si son reconocibles por el analizador y devuelve un resultado en consecuencia.


#Como funciona (Instrucciones):

De manera mas detallada, lo primero que hace es que se encarga de dividir la cadena de entrada en unidades léxicas llamadas tokens, reconociendo operadores aritméticos (+, -, \*, /), paréntesis de agrupacion, números enteros y decimales, así como palabras clave como if, else y while, aunque como se menciono anteriormente estas no se evaluan funcionalmente. Posteriormente, el analizador sintáctico (calculadoraParser) toma la secuencia de tokens en entrada y la compara contra una gramática definida, es decir la calculadora lexica, de esta manera determinando si la expresión tiene una estructura válida. en caso de que si, el parser construye un árbol de análisis y realiza una evaluacion de la expresion ingresada, posteriormente devuelve el resultado en pantalla, es decir si se ingresa un 2 + 2, se analiza cada simbolo individualmente, valida en la jerarquia de operaciones y retorna un resultado, en este caso 4. Sumado a esto, el programa basico, reconoce cuando se introduce un caracter o simbolo no valido, arrojando un resultado fallido en consecuencia, es decir que el simbolo no se encuentra o esta mal escrito. En resumen este programa demuestra los fundamentos de un compilador simple, abarcando la identificación de tokens hasta la evaluación semántica básica.


#Ejemplos de entrada:

--Entrada: 2 + 2 → Salida: 4
--Entrada: (3 + 5) * 2 → Salida: 16
--Entrada: 10 / 0 → Salida: error o advertencia de división entre cero
--Entrada: if → Reconocido como palabra clave, pero no evaluado
--Entrada: hola + 3 → Error léxico si "hola" no está definido como token válido
