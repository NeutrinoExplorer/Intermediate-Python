# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/UNI/Python Intermedio/Clase5")

# %% Verificación y Validación (V&V)

# Validación: ¿Estamos construyendo el producto correcto?
# Verificación: ¿Estamos construyendo el producto correctamente?

# Consideraciones:
    # Verificación dinámica
    # Conjunto finito de casos de prueba
    # Seleccionados a partir del dominio de ejecución
    # Comportamiento esperado del software/producto
    
# %% 

# P: ID -> OD, P es un programa

# ID: Dominio de entrada del programa P
# OD: Dominio de salida del programa P

# Es bastante comun en la literatura:
    # ID == [x1: X1, x2: X2, ..., zn: Xn]
    
    # OD == [y1: Y1, y2: Y2, ..., ym: Ym] 
    
# %% Depuración durante el desarrollo usando assert

# Primer caso de uso
number = 1

assert(number<5), "El numero/input/entrada no debe ser de mayor a 5"
print("El numero es ", number)
   
# Segundo caso de uso

number = 10 
assert(number<5), "El numero/input/entrada no debe ser de mayor a 5"
print("El numero es ", number)
   


# Ejemplo mas trivial: Obtengamos un assertion error
assert(1==2)

# Si el contenido de assert es igual a False, se lanza/ejecuta/instancia la excepcion
# AssertionError

if 1==1:
    raise AssertionError()
    
    
# Podemos añadir un texto con cierta informacion relevante
assert False, "La expresion booleana assert es falsa"
    


# %% assert en testing   

# Implementemos el requerimiento de codigo x666: Funcion que calcula la media de una lista
# de numeros

def calcula_media(lista):
    return sum(lista)/len(lista)

# Pequeño caso de uso
ListaDatos= [12,13,15,19]
calcula_media(ListaDatos)

    
# Realicemos comprobaciones de manera automatica
# Historia de usuario:
    # Para el ID= [ListaDatos]
    # Resultado OD= 14.75

# Notar que si obtenemos nada, ello implica que la historia de usuario a sido replicada
assert(calcula_media(ListaDatos) == 14.75)
    
    
# Otra historia de usuario:
    # para el ID= [5,10,4.5]
    # para el OD = 7.51
assert(calcula_media([5,10,4.5]) == 7.51)

# Notemos que al lanzarse/ejecutarse una instancia de la clase AssertionError esto nos
# lleva a concluir de que la historia de usuario no a sido replicada

# %% assert dentro de funciones

# Implementemos una funcion suma (que recibe dos argumentos) que solo sume si las entradas
# son numeros enteros

def suma(arg1, arg2): 
    assert(type(arg1)==int), "El primer argumento debe ser un numero entero"
    assert(type(arg2)==int), "El segundo argumento debe ser un numero entero"
    return arg1+arg2

# assert(P), accion ; si P==false -> se ejecuta la accion

# %% Prueba de uso 1
suma("a",2)

# Prueba de uso 2
suma(1.000000,0)

# Prueba de uso 3
suma(8,9)


# %% Documentacion de AssertionError

help(AssertionError)

# Documentacion de Exception
help(Exception)

# Documentacion de BaseException
help(BaseException)

# Documntacion de object
help(object)




















    