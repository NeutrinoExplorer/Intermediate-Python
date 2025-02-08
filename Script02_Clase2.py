# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/UNI/Python Intermedio/Clase2")

# %% MANIPULACIÓN DE COLECCIONES (ITERABLES)

# Funcion map: Nos permite aplicar una funcion sobre cada
# uno de los elementos de una coleccion (lista/tupla)

# Ejemplito
# Obtener el cuadrado de todos los elementos de una lista

# Funcion
def cuadrado(elemento):
    return elemento*elemento

# Definamos una lista(iterable)
lista = [12,3,4,23,9,19]

# Resultados
# Un objeto de tipo map lo transformamos a un objeto de tipo lista
resultado = list(map(cuadrado, lista))
resultado

# Tipo de dato
type(resultado)

# Metodos del objeto de tipo map
dir(resultado)

# Metodos de un objeto de tipo lista
dir([])


# Un objeto de tipo map se puede transformar a un objeto de tipo lista

resultado = list(resultado)
resultado

# %% Reduzcamos el codigo usando una funcion lambda
resultados2 = list(map(lambda e:e*e, lista))
resultados2

# Ejemplito 2
import math as m

# Necesitamos dos listas,

#Lista para la base
ListaBase= [12,0.5,8,4,5]

#Lista para los exponentes
ListaExponentes = [3,-2,0.6,1,2]

# Cada i-esimo elemento de Listabase debe ser elevado a su correspondiente
# i-esimo elemento de ListaExponentes

resultado3 = list(map(m.pow, ListaBase, ListaExponentes))
resultado3

# %% Funcion filter

# Nos permite realizar un filtro sobre los elementos de la coleccion

# Sintaxis
# filter(funcion_a_aplicar, objeto_iterable)

# Dada una tupla busquemos obtener los elementos mayores a 5

def mayor_a_cinco(numero_escalar):
    #Retorna un valor booleano
    return numero_escalar>5

# Definamos la tupla de datos
t1 = (12,3,4,5,67,-5,3,78,0.001)

# Observemos que el resultado de aplicar filter lo podemos empaquetar
# en una tupla (constructor tuple) o en una lista(constructor list)

resultado4 = tuple(filter(mayor_a_cinco,t1))
resultado5 = list(filter(mayor_a_cinco,t1))

print(resultado4)
print(resultado5)


# Usemos una funcion lambda
resultado6 = tuple(filter(lambda num: num>5, t1))
resultado6

# %% Seleccionemos/filtremos los elementos pares de una lista

ListaNum1 = [12,23,345,45,6,7,132,988,13,17,29]
pares = list(filter(lambda x: x%2==0 , ListaNum1))
pares

# %% Funcion reduce

# Usaremos la funcion reduce cuando poseamos una coleccion de elementos y
# necesitemos generar un unico resultado

# Sintaxis: Necesito cargar el modulo fuctools
# reduce(funcion_a_aplicar, objeto iterable)

# Observacion: Esta funcion (el primer argumento de reduce) debe poseer obligatoriamente
# dos parametros:
    
# El primer parametrro hara referencia a un acumulador
# El segundo parametro hara referencia a cada elemento de la coleccion (objeto iterable)

# %% Obtener la suma de los elementos de una lista

ListaNum2 = [-1,-23,234,12,34,45,56,7,7,9,87,65]


# Primera solucion: Sin usar reduce
acumulador = 0
for elemento in ListaNum2:
    acumulador = acumulador + elemento

acumulador

# Segunda solucion: Usando reduce

def func_suma(acumulador = 0, elemento = 0):
    return acumulador + elemento

from functools import reduce
resultado7 = reduce(func_suma, ListaNum2)
resultado7

# Reemplacemos a func_suma por una funcion anonima (lambda)

resultado8 = reduce(lambda acumulador = 0, elemento = 0: acumulador + elemento, ListaNum2)
resultado8


# %% Ejemplito
# Concatenar todos los elementos de una lista

ListaLP = ["Python","C","C++","Pascal","Fortran","Cobol","Go"]
resultado9 = reduce(lambda acumulador= " ", elemento = " ": acumulador + "-" + elemento, ListaLP)
resultado9

