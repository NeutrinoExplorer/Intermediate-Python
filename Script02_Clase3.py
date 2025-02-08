# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/UNI/Python Intermedio/Clase3")

# %% 

# Interactuemos con el sistema de archivos de la computadora que GCE provee
# para cargar archivos de datos (texto.)

# %% Carguemos en memoria un conjunto de datos

# modificacion del directorio de trabajo
import os
# Si quiero ver los archivos de mi directorio en el que me 
# trabajando debo escribir os.listdir()
os.chdir("C:/Users/RODRIGO/Desktop/UNI/Python Intermedio/Clase3")

# Carguemos el dataset en memoria : modulo csv

# Modulo csv sirve para manipular dataset
import csv
# la 2da componente "r" indica que tiene permiso de lectura
with open("babyNamesUSYOB-mostpopular.csv","r") as file:
    lecturaCSV = csv.reader(file)

# Tipo de dato
type(lecturaCSV)

# Ejecutemos la variable lecturaCSV
lecturaCSV

# Mostremos fila a fila cada elemento de lecturaCSV
# para esto debo tener abierto el archivo y ejecutar
# las siguientes 4 lineas de golpe
with open("babyNamesUSYOB-mostpopular.csv","r") as file:
    lecturaCSV = csv.reader(file)
    for fila in lecturaCSV:
        print(fila)
# cada manipulacion que haga con mi data set siempre antes
# debo tener abierto el dataset con with open
# vamos a guardar todo nuestro dataset en una lista en blanco

# %%

# Construyamos una lista con todos los nombres

listaNombres = []

with open("babyNamesUSYOB-mostpopular.csv","r") as file:
    lecturaCSV = csv.reader(file)
    for fila in lecturaCSV:
        listaNombres.append(fila[1])
        
#
listaNombres

# Sin embargo la primera fila es Name, no contiene informacion asi que
# debemos seleccionar de la segunda fila a la ultima, por tanto

#
listaNombres = listaNombres[1:]
listaNombres

# Mostremos los primeros 10 elementos de ListaNombres
listaNombres[:9+1]

# %% Implementemos una funcion que reciba dos argumentos

# Primer argumento: lista de nombres
# Segundo argumento: un caracter/letra
# La funcion va a devolver el numero de nombres que inician con esa letra

def CuentaNombres(lista, letra):
    """
     Funcion que calcule el numero de nombres que inician con el
     caracter letra en la variable lista
     
       lista: list
       letra: str(de un unico elemento)
     
    """
    NumLetra= 0
    for nombre in lista:
        if nombre[0] == letra:
            NumLetra = NumLetra + 1
    return NumLetra

# %% Contemos los nombres que inician con la "A"

CuentaNombres(listaNombres,"A")

# Contemos los nombres que inician con la letra "W"
CuentaNombres(listaNombres,"W")

# %% Calcular cuantos nombres existen en ListaNombres para cada letra del abecedario
import string
dir(string)
string.ascii_uppercase

# Empaquetemos el resultado en un diccionario usando fromkeys
dataNombres = {}.fromkeys(string.ascii_uppercase)
dataNombres

for letra in string.ascii_uppercase:
    dataNombres[letra]= CuentaNombres(listaNombres, letra)
    
dataNombres

# %% 

CuentaNombres["A", listaNombres[666:6666+1]]

# Observamos que CuentaNombres tiene en consideracion el orden en los argumentos
# CuentaNombres es una funcion de Argumentos por posicion

CuentaNombres(listaNombres[666:6667],"A")

# %% Llamemos a la funcion utilizando los argumentos por nombres
CuentaNombres(lista= listaNombres[100:10001], letra= "P")

# Cuando especificamos los nombres de los argumentos podemos intercambiar
# el orden
CuentaNombres(letra= "Z", lista = listaNombres)

# %% Funciones con argumentos con valores por defecto

# Implementemos el calculo de la fuerza electrica entre dos cargas puntuales
# (q1,q2) separadas una distancia d(metros). Usando la ley de Coulomb

def coulomb(q1,q2,d,k=9*10**9):
    return k*q1*q2/d**2

# %% Usemos la funcion coulomb considerando argumentos por posicion

F1 = coulomb(5.6*10**(-12),3.9*10**(-11),2.8*10**(-2))
F1

# %% Usemos la funcion de coulomb usando argumentos por posicion, pero
# modificando el valor de la constante k

F2 = coulomb(5.6*10**(-12),3.9*10**(-11),2.8*10**(-2),9.81*10**9)
F2

# %% Usemos argumentos por nombre sin modificar el valor de k
F4 = coulomb(d=2.8*10**(-2),q2=3.9*10**(-11),q1=5.6*10**(-12))
F4

# %% Funciones con argumentos de longitud variable

# Consideremos implementar una funcion que sume dos numeros

def adicion(x1,x2):
    return x1+x2

# Ejemplito de ejecucion de la funcion adicion usando argumentos por posicion
adicion(12,9.6)

# Ejemplito de ejecucion de la funcion adicion usando argumentos por nombre
adicion(x2=9.6,x1=12)

adicion(1,2,12.3,9)

# %% En vista del problema obtenido en la celda anterior: No sabemos cuantos numeros
# son los que vamos a sumar

# Una primera forma es considerar la implementacion de una funcion con un numero
# de argumentos variable. Empaquetando los input de la funcion en una lista

def adicion2(listaNumeros):
    """
     funcion que calcule la suma de todos los elementos de una lista de numeros    
    """

    sumaTotal = 0
    for elemento in listaNumeros:
        sumaTotal = sumaTotal + elemento
    return sumaTotal

# %% Ejemplito
adicion2([12,13,14])

# Otro ejemplito
adicion2([12,23,345,45,456,64,56,456,45,64,5,6])


# %% Limitante que tiene adicion2: Solo recibe un argumento
adicion2(12,9.6)

# Para definir una funcion con un numero variable de argumentos
# Hay que anteponer el caracter *¨al argumento de la funcion
def adicion3(*numeros): 
    sumaTotal= 0
    for i in numeros:
        sumaTotal= sumaTotal + i
    return sumaTotal

# ejemplito
adicion3(12)

# ejemplito
adicion3(12,34,5)

# %% La forma como esta implementada la funcion adicion3 
# nos enseña un nuevo tipo de implementacion

# Definamos una funcion con el siguiente comportamiento
# Si solo tiene dos argumentos: retorna el producto de los dos argumentos
# Si solo tiene 3 argumentos, retorna el promedio aritmetico
# Si la funcion se ejecuta con un numero distinto a 2 o 3 argumentos: retorna un mensaje de error

def Operaciones1(*argumentos):
    if len(argumentos)==2:
        return argumentos[0]*argumentos[1]
    elif len(argumentos)==3:
        return sum(argumentos)/len(argumentos)
    else:
        return "Numero de argumentos invalido  (Leer la documentacion)"
    
# %% Primera llamada/ejecucion de Operaciones1

Operaciones1()

# Segunda llamada/ejecucion de Operaciones1
Operaciones1(9.81)

# Tercera llamada/ejecucion de operaciones1
Operaciones1(12,10)

# Cuarta llamada/ejecucion de Operaciones1
Operaciones1(14,8,2)

# Al usar la estrategia anterior no podemos usar argumentos por nombres,
# Entonces debemos aprender otra forma de implementar funciones

# %% Usemos **kwargs

def Operaciones2(**kwargs):
    """
    Calcula la suma de los elementos
    """
    # Vamos a considerar a kwargs como si fuera un diccionario
    sumaTotal=0
    for llave, valor in kwargs.items():
        print(llave,valor)
        sumaTotal=sumaTotal + valor
    return sumaTotal

# ejemplito1
Operaciones2(p1=12,p2=17,p3=3)

# ejemplito2
dict_datos={"g1":9.812, "euler":2.719, "pi":3.14159}
Operaciones2(**dict_datos)

# ejemplito2
Operaciones2(g1=9.812, euler=2.719, pi=3.14159)

# %% Obliguemos a que la funcion solo trabaje con los argumentos: c1,c2

def Operaciones3(**kwargs):
    # verifiquemos que solo se tiene a c1 y c2 como argumentos
    if ( ("c1" in list(kwargs.keys())) and ("c2" in list(kwargs.keys()))):
        print("jarvice tiene los argumentos adecuados:")
        print("\t Jarvice en linea ...")
        # Puede continuar con un numero de tareas determinado
    else:
        print("ERROR DE EJECUCION. Se procede a hackear tu sistema")
        
# %% Primera prueba de Operaciones3
Operaciones3(x1=12,C1="17")

# Segunda prueba de Operaciones3
Operaciones3(c1=12,c2=3,c3="Adios mundo cruel")


# %% Actualicemos a la funcion Operaciones3

def Operaciones3_Ver2(**kwargs):
    if len(list(kwargs.keys())) ==2:
        # verifiquemos que solo se tiene a c1 y c2 como argumentos
        if ( ("c1" in list(kwargs.keys())) and ("c2" in list(kwargs.keys()))):
            print("jarvice tiene los argumentos adecuados:")
            print("\t Jarvice en linea ...")
            # Puede continuar con un numero de tareas determinado
        else:
            print("ERROR DE EJECUCION. Se procede a hackear tu sistema")
    else:
        print("Numero de argumentos invalido")
        
# %% Primera prueba de Operaciones3_Ver2
Operaciones3_Ver2(c1=12,c2=3,c3="Adios mundo cruel")

# Segunda prueba de Operaciones3_Ver2
Operaciones3_Ver2(c1=12,c2=3)

# Tercera prueba de Operaciones3_Ver2
Operaciones3_Ver2(c1=12)




























































































