# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/UNI/Python Intermedio/Clase4")

# %% La palabra reservada raise

# Para que se ejecute una excepcion debemos de hacerlo mediante codigo
1/0.0

# En algun escenario especifico (o bajo alguna necesidad) puedo buscar levantar/instancias
# una excepcion: ZeroDivisionError

raise ZeroDivisionError("Se me dio la gana de instanciar una ZeroDivisionError")

# Instanciemos/levantemos/lancemos una excepcion NameError

raise NameError("No leiste bien la documentacion. Jalaste el PIT146")

# Recordar: Leer la documentacion de todas y cada una de las excepciones que
# trae python por defecto

# Asi como tambien ver la dependencia entre cada una de ellas

# %% Uso de else con el bloque try-except

# El bloque else se ejecutara cuando no ocurrio excepcion alguna

# Forcemos una excepcion

try:
    x= 3.14159/0.0
except:
    print("Usuario: Definiste la variable usando una operacion inadecuada")
    x = float(input("Ingresa el numerador: "))
    y = float(input("Ingresa el dennominador: "))               
else:
    print("Usuario: No a ocurrido ninguna excepcion")
    

#


try:
    x= 3.14159/2.0
except:
    print("Usuario: Definiste la variable usando una operacion inadecuada")
    x = float(input("Ingresa el numerador: "))
    y = float(input("Ingresa el dennominador: "))               
else:
    print("Usuario: No a ocurrido ninguna excepcion")
    
# %% La palabra reservada finally

# Asociada a un bloque try-except-else tambien le podemos
# asociar un bloque finally. Este bloque finally se ejecuta siempre
# (haya o no ocurrido excepcion alguna)

# Veamos la excepcion que se obtiene de intentar cargar un archivo de datos
# en memoria sin que este esté disponible
with open("data1.txt") as file:
    data_obtenida = file.read()


# Intentemos abrir (cargar en memoria ram) un archivo de datos de nuestro sistema
# de archivos

try:
    with open("data1.txt") as file:
        data_obtenida = file.read()
except FileNotFoundError:
    print("Se lanzo una excepcion: No se puede cargar en memoria la base de datos")
except 0SError:
    print("Este es un error del sistema operativo")
    

# Bloque try-except-else-finally

try:
    with open("data1.txt") as file:
        data_obtenida = file.read()
except FileNotFoundError:
    print("Se lanzo una excepcion: No se puede cargar en memoria la base de datos")
except OSError:
    print("Este es un error del sistema operativo")
else:
    print("No a ocurrido excepcion alguna")
finally:
    import os
    os.system("wget https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/refs/heads/master/ACS.csv")








































