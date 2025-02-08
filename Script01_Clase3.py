# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/UNI/Python Intermedio/Clase3")


# %% La funcion filter sobre diccionarios

# Consideremos un diccionario de datos
data1 = {"A":19,"B":2,"C":14,"D":1,"E":5}

dict(filter(lambda x: x[1]>12,data1.items()))

# Recuperemos de data1 aquellos valores cuya llave es "B"
dict(filter(lambda x:x[0]=="B",data1.items()))

# %% La funcion map sobre diccionarios

# Multipliquemos por un aleatorio a cada valor del diccionario data1

import random as rnd
dict(map(lambda x: (x[0]+str(rnd.randint(1,2)),x[1]*rnd.randint(0,5)), data1.items()))

# %% Reduce para diccionarios

# Calculemos la suma de todos los valores de data1
from functools import reduce
reduce(lambda x,y: x+ y[1], data1.items(),0)

# %% Funcion zip

# Sirve para reorganizar listas
# Como parametros admite un conjunto de listas
# Lo que hace es tomar el elemento i-esimo de cada lista y unirlos en una tupla,
# despues une todas las tuplas en una sola lista

# Punto de partida: dos listas
# Consideremos una lista de nombres y otra de sus correspondientes apellidos
# Vamos a usar zip

# Definamos las listas
ListaName1 = ["Adrian", "Jorge", "Alejandra", "Andrea", "Marta"]
ListaApellidosPat = ["Luna", "Torres", "Arambulo", "Cernades", "Echegarray"]

# zip usa cada nombre con su correspondiente apellido y los empaqueta en una tupla
NombreApellido = list(zip(ListaName1, ListaApellidosPat))
NombreApellido















