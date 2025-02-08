# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/UNI/Python Intermedio/Clase2")

# %% ERRORES Y EXCEPCIONES

# Errores estan asociados a los errores de sintaxis
while false print("Clase2"):
    
# Excepciones

x= 10*(0.2/0)
x+2

# Excepciones
4 + variable *3

# Excepciones
"12" + 12.5

#%% Lista de excepciones integradas en python
dir(locals()["__builtins__"])

#%% Estructura jerarquica entre algunas excepciones

help(FloatingPointError)

# Sin embargo, FloatingPointError es una subclase de
# ArithmeticError

#%% Accedemos a la documentacion de ArithmeticError

help(ArithmeticError)

# Es subclase de Exception
#%% Accedemos a la documentacion de Exception

help(Exception)

# Es subclase de BaseException

#%% Accedemos a la documentacion de BaseException

help(BaseException)

# Es subclase de object

# %% Accedemos a la documentacion de object

help(object)

# Ya no es subclase de nada

#%% Operaciones sencillas: Calculo del reciproco de 
# los elementos de una lista

# Lista de datos
data2 = [0.5,12,4,0.9,1.6,0,2,1]

# Mostremos la inversa de cada elemento
# ya que data2 es una lista, es decir elemento iterable

for elemento in data2:
    print(1/elemento)


# Estos errores se deben manipular de modo que
# por mas de que ocurra no se interrumpa el codigo

# %% Bloque try-except

# Con los elementos de data2 y calculemos las inversas
# de esos elementos, manipulanod las posibles excepciones

for elemento in data2:
    # Cuando no se ejecute una excepcion: try
    try:
        print("Input: ",elemento)
        print("Output: ",1/elemento)
    
    # Cuando se ejecute una excepcion
    except: 
        print("Esta operacion es ilegal !!!")
        print("Continuemos con el siguiente elemento de data2")
 
# %% Recuperemos la excepcion que se ejecuta en mi codigo
import sys

# Documentacion del modulo sys
help(sys)

for elemento in data2:
    # Cuando no se ejecute una excepcion: try
    try:
        print("Input: ",elemento)
        print("Output: ",1/elemento)
    
    # Cuando se ejecute una excepcion
    except: 
        print("Esta operacion es ilegal !!!")
        # Recuperemos la informacion de la excepcion
        print("Excepcion: ", sys.exc_info()[1])
        print("Continuemos con el siguiente elemento de data2")

#%% Redefinamos el objeto data2


data2 = ["12",0,9,-1]

# Agreguemos una funcionalidad: Contar el numero de excepciones
NumExp=0

for elemento in data2:
    # Cuando no se ejecute una excepcion: try
    try:
        print("Input: ",elemento)
        print("Output: ",1/elemento)
    
    # Cuando se ejecute una excepcion
    except:
        NumExp= NumExp + 1 
        print("Esta operacion es ilegal !!!")
        # Recuperemos la informacion de la excepcion
        print("Excepcion: ", sys.exc_info()[1])
        print("Continuemos con el siguiente elemento de data2")

print("Numero de excepciones: %d" %(NumExp))

# %%  Otra forma de manejar las excepciones: Personalicemos
# las tareas/rutinas a ejecutarse en funcion de la excepcion lanzada


# input
data2 = ["12",0,9,-1]

# Historico de cada tipo de excepcion
NumTypeErrors= 0
NumZero = 0

import sys
for elemento in data2:
    try:
        print("Input: ",elemento)
        print("Output: ",1/elemento)
    except TypeError:
        print("Esta operacion es ilegal: Tipos de datos no adecuados")
        NumTypeErrors = NumTypeErrors + 1
    except ZeroDivisionError:
        print("No puedes dividir entre cero")
        NumZero = NumZero + 1
    except:
        print("Excepcion no controlada")
        print("Exception: ", sys.exc_info()[0])
        
# %% Pidamos al usuario un maximo de 5 numeros enteros
# Almacenando los numeros enteros en una lista

# datos almacenados en una lista
ListaNum = []

for num in range(5):
    # Si todo va bien
    try:
        tmp = int(input("Ingresa un numero entero"))
        ListaNum.append(tmp)
    # Si hay una excepcion con el codigo en try
    
    except ValueError:
      print("El dato ingresado no es un numero entero")
      tmp = int(input("Ingresa un numero entero"))
      ListaNum.append(tmp)

ListaNum






















