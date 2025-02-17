# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/UNI/Python Intermedio/Clase7")

# %% Implementemos la clase Rectangulo

class Rectangulo:
    # Escribimos docstring
    """
    Clase para definir/nodelar un rectangulo
    Ademas, se implementaran algunos metodos/funciones que calculen:
        area
        perimetro
        diagonal
    
    Usaremos como atributos:
        base
        altura
    """
    
    # Modifiquemos el constructor __init__
    def __init__(self, base=1.0, altura=1.0):
        """
        Constructor para la clase Rectangulo con valores por defecto para sus dimensiones
          base= 1.0
          altura= 1.0
        """
        self.base = base
        self.altura = altura
        
        # Modifiquemos el metodo __repr__
    def __repr__(self):
        """
        Retomamos un string al ejecutar el objeto instanciado
        """
        return "Rectangulo de dimensiones: \n\tBase: %.2f \n\tAltura: %.2f" %(self.base, self.altura)
        
    # Implementacion del metodo calculo_area
    def calculo_area(self):
        """
        Calculo del area de una instancia de la clase Rectangulo
        """
        return self.base*self.altura
    
    # Implementacion del metodo calculo_perimetro
    def calculo_perimetro(self):
        """
        Calculo del perimetro de una instancia de la clase Rectangulo
        """
        return 2*(self.base + self.altura)
    
    # Implementacion del calculo de la diagonal
    def calculo_diagonal(self):
        """
        Calculo de la diagonal de una instancia de la clase Rectangulo
        """
        
        from math import sqrt
        return sqrt((self.base)**2+(self.altura**2))
    
# %% Primera Prueba de la clase Rectangulo

# Definimos una instancia

R1= Rectangulo()
R1
print(R1)
# Observamos la ejecucion del metodo __repr__

# %% Calculemos la diagonal al objeto R1
R1.calculo_diagonal()

# Otra instancia de la clase Rectangulo
R2 = Rectangulo(12,0.3)
R2

# Mostremos las caracteristicas de R2
print("""
      Area: %.3f
      Perimetro: %.3f
      Diagonal: %.3f
      """ %(R1.calculo_area(),R1.calculo_perimetro(),R1.calculo_diagonal()))
      
R1.calculo_area, R1.calculo_perimetro, R1.calculo_diagonal()

# Limitante de la clase Rectangulo
R3= Rectangulo("12", [10])
R3     

# El objeto ha sido creado, pero entre sus caracteristicas privadas (__repr__)
# no podría cumplir su funcionalidad
# ESTO ES UN PROBLEMA QUE SE DEBE CORREGIR, YA QUE NO DEBIO DE HABERLO CREADO

# %% Implementacion de la Segunda version de la clase Rectangulo

class Rectangulo_V2:
    # Escribimos docstring
    """
    Clase para definir/nodelar un rectangulo
    Ademas, se implementaran algunos metodos/funciones que calculen:
        area
        perimetro
        diagonal
    
    Usaremos como atributos:
        base
        altura
    """
    
    # Modifiquemos el constructor __init__
    # Modifiquemos este metodo buscando que los argumentos sean de naturaleza numerica
    def __init__(self, base=1.0, altura=1.0):
        """
        Constructor para la clase Rectangulo con valores por defecto para sus dimensiones
          base= 1.0
          altura= 1.0
        """
        # Para la Version 2 de la clase Rectangulo usamos una estructura de decision para
        # validar la correcta asignacion de los atributos base y altura
        if isinstance(base, (int, float)) and isinstance(altura, (int, float)):
           self.base = base
           self.altura = altura
        else:
           # Ejecutamos una excepcion con la palabra reservada raise
           raise TypeError("Los argumentos deben ser numericos!!!")
            
        
        # Modifiquemos el metodo __repr__
    def __repr__(self):
        """
        Retomamos un string al ejecutar el objeto instanciado
        """
        return "Rectangulo de dimensiones: \n\tBase: %.2f \n\tAltura: %.2f" %(self.base, self.altura)
        
    # Implementacion del metodo calculo_area
    def calculo_area(self):
        """
        Calculo del area de una instancia de la clase Rectangulo
        """
        return self.base*self.altura
    
    # Implementacion del metodo calculo_perimetro
    def calculo_perimetro(self):
        """
        Calculo del perimetro de una instancia de la clase Rectangulo
        """
        return 2*(self.base + self.altura)
    
    # Implementacion del calculo de la diagonal
    def calculo_diagonal(self):
        """
        Calculo de la diagonal de una instancia de la clase Rectangulo
        """
        
        from math import sqrt
        return sqrt((self.base)**2+(self.altura**2))
 
    
# %% Verifiquemos la nueva modificacion
R4= Rectangulo_V2(altura= "12", base=10)
R4

# Se ha corregido el error comentado :)

