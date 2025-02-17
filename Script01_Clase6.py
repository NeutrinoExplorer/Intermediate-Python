# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/UNI/Python Intermedio/Clase6")

# %% Programación orientada a objetos

# Clases (palabra reservada 'class')
# Herencia: Usamos la funcion 'help'

# De la introduccion mostrada en la clase5 podemos concluir que
# una clase no es mas que una plantilla que usamos para crear/instanciar
# objetos

# Todos los objetos pertenecen a una determinada clase
# En python todas las clases tienen como primer padre a la clase Object

# %%
# Definicion de una clase: De forma un poco más general

class NombreClase(NombreClasePadre1, NombreClasePadre2, NombreClasePadre3):
    # NombreClasePadre1,2,3 son el nombre de las clases padre a partir de la cual
    # mi clase creada NombreClase va a heredar
    """
    Este docstring es para escribir la documentacion de la clase imeplementada
    
    """
    def __init__(self, atrib1, atrib2, atrib3):#siempre inicia con self
        self.atrib1= atrib1 # atributo publico
        self._atrib2= atrib2 # atributo protegido
        self.__atrib3= atrib3 # atributo privado 
    
# %% Ejemplito

# Los miembros de una clase son sus métodos o atributos

# Clase Padre: Animal
  # Clase hija (I): Cuadrupedos
  # Clase hija (II): Aves
  # Clase hija (III): Mamiferos
  # Clase hija (IV): Felinos
  
# Tener en cuenta que por mas de que parezca natural la relacion entre cada una de las 
# clases hija que mostramos en esta celda. Esta relación se puede realizar de manera
# mas granular

# %% Ejemplito:
    
# Clase Padre: Empresa
  # Clase Hija (I): Dueños
  # Clase Hija (II): Gerentes
  # Clase Hija (III): Colaboradores

# Clase Hija (I)
  # Clase Hija(i): Fundadores
  # Clase Hija(ii): Intervencionistas
  
# Clase Hija(i): Inversionistas
  # clase hija (1): CompraAccionesAmistad
  # clase hija (2): FondosDeCobertura
  
# Clase Hija (II): Gerentes
  # Clase hija (1): Aministrativa
  # Clase hija (2): Comercial
  # Clase hija (3): Logistica
  # Clase hija (1): Marketing
  
# %% 

# En python todo es un objeto
# Un objeto puede tener dos tipos de abstracciones

# Funcional: Como cosas que sabemos que nuestros objetos hacen, pero
# no como las hacen

# De datos: Atributos(caracteristicas), un coche tiene un atributo Color, un atributo Asientos


# Un objeto es basicamente una forma de agrupar un conjunto de datos
# y de funcionalidades en un mismo bloque de codigo
# que luego puede ser referenciado desde otras partes
# donde dicha clase a la que pertenece el objeto, puede considerarse
# como un nuevo tipo de dato

# %% Implementación de la clase Animal

# Si es que la clase esta compuesta por una sola paralabra, la primera letra empieza con
# mayuscula

# Si es que la clase esta compuesta por varias palabras, cada letra de inicio de cada palabra
# inicia con mayuscula


class Animal:
    # si no especifico las clases padre, python interpreta que
    # automaticamente Animal es clase hija de la clase object
    def __init__(self, edad=0, nombre= "Godzilla"): #El primer atributo del constructor init es self 
    
      """
      Constructor de la clase Animal
      
      :param edad: Edad del animal : Por defecto tiene el valor de cero
      :param nombre: Nombre del animal : Por defecto tiene el valor de Godzilla
      :return : Una instancia de la clase Animal
   
      """
      # Todos los atributos de este constructor seran publicos
      self.edad = edad
      self.nombre = nombre
      # Puedo tener otros atributos locales del constructor init
      self.sexo = "F"
      self.vivo = True
      #Animal.numAnimals = numAnimals + 1 (La clase padre Object no tiene el atributo numAnimals)
    
    # Mis clases pueden tener atributos, y tambien pueden tener acciones

    # Definimos el metodo saluda
    def saluda(): #Si no especifico el objeto self dentro del parentesis este metodo
    # tendria acceso a los atributos definidos en mi constructor init
     print("Hola Mundo")
  
    # Este metodo si tiene acceso a los atributos definidos del constructor init
    def showmethename(self): 
     print("Bienvenido " + self.nombre)

    
    def showmetheage(self): 
     print("Edad" + str(self.edad))
    
# %% 

# Instancio en el objeto anm1

anm1 = Animal(edad = 12, nombre = "Firulais")    

# Ya que anm1 es un objeto de Python por lo menos deberia tener un tipo de dato

type(anm1)    

# %% Lista de miembros que puedo aplicar a una instancia anm1
dir(anm1)    

# Documentacion de showmethename
help(anm1.showmethename)    

# Aplicamos el metodo showmethename al objeto anm1
anm1.showmethename()    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
        