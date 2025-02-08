# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/UNI/Python Intermedio/Clase1")

# %%

# Topicos desarrollados en el curso básico
  
  # definicion de variables / operaciones
  # Funciones: type, dir y help
  # Función input y print
  # Estructuras de decisión y de repetición
  # Definición de funciones en python
  # Listas, tuplas y diccionarios
  # Primeros pasos con numpy
  
import this

# %%

# Palabras reservadas
help("keywords")

help("None") # None es una clase

# %%
help("is") # comparaciones
# La palabra reservada is tiene que ver con and or not e in

# keywords de control de flujo: if elif else
# keywords para iteraciones: for while (else) break continue
# keywords para estructuras: def pass class as lambda
# keywords de retorno: return yield
# keywords de importacion: import from as
# keywords de manejo de excepciones: try excep raise assert finally
# keywords de variables: del global nonlocal

# %%

#Funciones Anonimas: lambda

# definamos una funcion que realiza una funcion matematica

#importamos modulos
import math as m
import random as rnd

def f1(x):
    return 0.5*x**(rnd.randint(333,666))
f1(1)

# %%

# Usemos la palabra reservada lambda para definir a f1

# Caso: lambda con un argumento w
f1_anonima= lambda w: 0.5*w**(rnd.randint(333,666))

f1_anonima(1)

# %%

# Caso: lambda con varios argumentos
suma3 = lambda x1,x2,x3 : print(x1+x2+x3)
y1 = suma3(-2,3,5)

y1

# tipo de dato para y1
type(y1)

# Puedo definir x1,x2,x3 como listas
y2 = suma3([0.5,0.2,0.9],[],[4,5])
y2

# %%

#List comprehensions

# Sintaxis
# ListaOutput = [expresion for elemento in iterable]

# Generemos una lista con los cuadrados de los numeros del 1 al 10
[i**2 for i in range(1,11)]

# Agreguemos una condicional
# Definimos una cadena

cad = "El dia de hoy inicio el curso de python intermedio en el PIT nacional"

# Construyamos una lista con todos los caracteres "a"
[c for c in cad if c=="a"]

# Creamos una lista de nombres
ListaNombres = ["Juan", "Eduardo", "Maria", "Vanessa", "Sofia"]
# Obtengamos los nombres que tengan la letra "e"
[n for n in ListaNombres if "e" in n]

# Consideremos todos los nombres excepto "Juan"
[x for x in ListaNombres if x != "Juan"]

# Contemos el numero de caracteres de cada nombre almacenado en ListaNombres
[len(x) for x in ListaNombres]


#%%

# Dict Comprehensions
{c: len(c) for c in ListaNombres}

# %% MANEJO DE ERRORES Y EXCEPCIONES

#

c = 3.12
d = -3.6

#
h = c+d
h

# Definamos un diccionario
Medallas = {"Pais1":12, "Pais2":3, "Pais3":5, "Pais4":0}

#
Medallas["Pais5"]

# %%
# Documentacion del metodo get para un dato de tipo dict
help(Medallas.get)

Medallas.get("Pais5", "Pais no encontrado en la base de datos")

# %%

# Generamos una excepcion
p = (c+d)/0

f = d**p
f

# %%

# Otra excepcion

Tesis = "12" + 9.81
Tesis

# %% Lista de excepciones integradas con python
dir(locals()["__builtins__"])

# Lista de excepciones

ListaExceptions = ['ArithmeticError',
 'AssertionError',
 'AttributeError',
 'BaseException',
 'BlockingIOError',
 'BrokenPipeError',
 'BufferError',
 'BytesWarning',
 'ChildProcessError',
 'ConnectionAbortedError',
 'ConnectionError',
 'ConnectionRefusedError',
 'ConnectionResetError',
 'DeprecationWarning',
 'EOFError',
 'Ellipsis',
 'EnvironmentError',
 'Exception',
 'FileExistsError',
 'FileNotFoundError',
 'FloatingPointError',
 'FutureWarning',
 'GeneratorExit',
 'IOError',
 'ImportError',
 'ImportWarning',
 'IndentationError',
 'IndexError',
 'InterruptedError',
 'IsADirectoryError',
 'KeyError',
 'KeyboardInterrupt',
 'LookupError',
 'MemoryError',
 'ModuleNotFoundError',
 'NameError',
 'NotADirectoryError',
 'NotImplemented',
 'NotImplementedError',
 'OSError',
 'OverflowError',
 'PendingDeprecationWarning',
 'PermissionError',
 'ProcessLookupError',
 'RecursionError',
 'ReferenceError',
 'ResourceWarning',
 'RuntimeError',
 'RuntimeWarning',
 'StopAsyncIteration',
 'StopIteration',
 'SyntaxError',
 'SyntaxWarning',
 'SystemError',
 'SystemExit',
 'TabError',
 'TimeoutError',
 'TypeError',
 'UnboundLocalError',
 'UnicodeDecodeError',
 'UnicodeEncodeError',
 'UnicodeError',
 'UnicodeTranslateError',
 'UnicodeWarning',
 'UserWarning',
 'ValueError',
 'Warning',
 'WindowsError',
 'ZeroDivisionError']

len(ListaExceptions)

# %% Veamos la documentacion de FloatingPointError

help(FloatingPointError)

# %% Veamos la documentacion de ArithmeticError

help(ArithmeticError)











