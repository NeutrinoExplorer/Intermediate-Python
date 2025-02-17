# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/UNI/Python Intermedio/Clase7")

# %% POO

# la POO es un paradigma: Definir a los programas en términos de clases de objetos
# objeto: Son entidades que combinan,
  #estado, comportamiento e identidad
## Características:
    # Reutilización del código
    # Permite crear sistemas más complejos
    # Relacionamos el sistema que buscamos desarrollar con el mundo real.
    # El paradigma de la POO facilita la creación de software con interfaz grafica de usuario
    # (GUI): PyQT (basada en la libreria QT), WxPython (basado en WxWidgets)
    # Tkinter, Kivy, PySimpleGUI, PySide.
    # Construccion de prototipos
    # Agiliza el desarrollo de software
    # Facilita el mantenimiento (Depende del diseño)
    # Facilita el trabajo en equipo (Depende del diseño)

## Elementos de la POO
    # Clase
    # Objetos
    # Mensajes
    # Herencia
    # Polimorfismo
    
# %% Definamos la clase Circulo

class Circulo:
    """
    Una instancia de la clase Circulo modela un circulo con su respectivo radio
    y puede realizar algunas operaciones:
        * Calcular el área del circulo
        * Calcular el perímetro del círculo
    """
    
    # Metodo __init__ : Como el usuario va a instanciar en un objeto a la clase Circulo
    def __init__(self, radio= 1.0):
        """
        El constructor de la clase Circulo con radio (opcional/con valor por defecto) igual a 1.0
        """
        self.radio = radio
    # Metodo __str__
    def __str__(self):
        """
        Retorna un string que sirve para interoperar con print y str
        """
        return "Circulo de radio %.3f" %self.radio
    # Metodo __repr__
    def __repr__(self):
        """
        Retorna un string usado para recrear la instancia
        """
        return "Circulo(radio=%.3f)" %self.radio
    
    # Hasta este punto
    # Realicemos una primera prueba de la clase Circulo
    
    # Continuemos agregando metodos propios de la clase Circulo:
        # Calcular el area del circulo
        # Calcular el perimetro del circulo
    
    def calculo_area(self):
        """
        Este metodo implementa el calculo del area de una instancia de la clase Circulo
        """
        return 3.1415*(self.radio)**2
    
    def calculo_perimetro(self):
        """
        Metodo que implementa el calculo del perimetro de una instancia de la clase Circulo
        """
        return 2*3.1415*self.radio
    
# %%    Primera Prueba ( hasta la linea 30 del codigo fuente de la clase Circulo)

Cx = Circulo()

# La celda anterior ya creo al objeto Cx en memoria
Cx
# Observamos el resultado de que se apllico el metodo __repr__

print(Cx)
# Observamos el resultado de que se ejecuto el metodo __str__

# %% Una vez que agregados los metodos calcula_area y calcula_perimetro

# Definamos una instancia de la clase Circulo

c1 = Circulo()
c2 = Circulo(radio=3.72)

# Carguemos el modulo math
import math as m
c3 = Circulo(m.e**(0.333*m.pi))        

# %% Tipo de dato
type(c1) # Para ver tipo de dato
help(c1) # Para ver docstring

# Lista de metodos
dir(c1)

# dir no diferencia de metodo y atributo, sin embargo los metodos serian:
    #calculo_area
    #calculo_perimetro
    
# %% Documentacion del metodo calculo_perimetro
help(Cx.calculo_perimetro)

# El metodo __doc__
print(c1.__doc__)

# El metodo __doc__ del metodo calcula area
print(c3.calculo_area.__doc__)

# %% Funcion isinstance:

# Verifica en un momento en especifico que un objeto determinado en el primer argumento
# es instancia o no de una clase determinada en el segundo argumento 

isinstance(c1,list)











