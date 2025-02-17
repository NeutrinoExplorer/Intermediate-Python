# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/UNI/Python Intermedio/Clase8")

# %% Herencia

# Implementemos nuestra propia clase Base (Clase Abstracta / Super Clase): Clase Persona

# Persona:
    # Tiene una fecha de nacimiento (modulo datetime): lista de tres numeros (yyyy, mm, dd)
      # Hay que tener ciertas consideraciones:
          # La primera componente de esta lista representa al año: desde 1900 hasta el presente año
          # La segunda componente de esta lista representa al mes: debe ser un numero entero de 1 a 12
          # La tercera componente de esta lista representa al día: debe ser un entero de 1 a 31
    # Posee un dni (string de 8 caracteres)
    # Posee uno o más nombres: Dato de tipo lista
    # Posee un apellido paterno: Dato de tipo lista
    # Posee un apellido materno: Dato de tipo lista
    # Tiene un sexo: string de un solo caracter (M o F)
    # Puede comunicarse (devolver una cadena de caracteres)

# %% Modulo datetime

# Carguemos el modulo datetime
import datetime

# Que compone al modulo datetime
dir(datetime)

 # 'date',
 # 'datetime',
 # 'datetime_CAPI',
 # 'sys',
 # 'time',
 # 'timedelta',
 # 'timezone',
 # 'tzinfo'

# Primera constante definida en el modulo datetime
datetime.MAXYEAR

# Segunda constante definida en el modulo datetime
datetime.MINYEAR

# %%

# Analicemos el miembro date de la lista que obtiene la funcion dir para el modulo datetime
help(datetime.date)

# De la celda anterior, aprendimos que datetime.date es una clase => que esta clase (date) puede servir para instanciar un objeto
d1= datetime.date()

# La creacion de d1 mostro fundamentalmente dos cosas:
    # Cada vez que por primera vez que comencemos a estudiar (a desarrollar) un modulo lo primero es leer la documentación
    # Forma correcta de interpretar la documentación proveida por help
    
# Instanciemos un nuevo objeto
d2 = datetime.date(1958, 6, 12)
d2

# Tipo de dato
type(d2)

# Funcion isinstance
isinstance(d2, datetime.date)

# Lista de metodos que se puede aplicar a un objeto de tipo como el de d2
dir(d2)

# 'ctime',
# 'day',
# 'fromisoformat',
# 'fromordinal',
# 'fromtimestamp',
# 'isocalendar',
# 'isoformat',
# 'isoweekday',
# 'max',
# 'min',
# 'month',
# 'replace',
# 'resolution',
# 'strftime',
# 'timetuple',
# 'today',
# 'toordinal',
# 'weekday',
# 'year'

# Documentacion del miembro year 
help(d2.year)

# De la celda anterior hemos de reconocer que el miembro year es un atributo:
# pues esta devuelve un tipo de dato int

d2.year

# Veamos la documentacion de weekday
help(d2.weekday)    

# Este si es un metodo
# Apliquemos el metodo weekday a un objeto de tipo como el de d2
d2.weekday()
# Como es un metodo sí requiere los parentésis
# Si fuese atributo no requiere parentesis

# %% Analicemos al miembro datetime.datetime de dir(datetime)
help(datetime.datetime)

# Creación de un objeto instancia de la clase datetime.datetime
f1 = datetime.datetime(1958,6,12)

# Mostremos f1 usando el metodo __repr__
f1

# Usamos el metodo __str__
print(f1)

# Tipo de dato
type(f1)

# Como cualquier objeto de python tiene una lista de metodos
dir(f1)

# Veamos la documentacion de isoweekday
help(f1.isoweekday)

# %%  Tarea: Desarrollar a profundidad, al igual que con el modulo datetime
# El modulo calendar

import calendar

# Documentacion
help(calendar)

# Miembros del modulo calendar
dir(calendar)

# Veamos la documentacion de IllegalMonthError
help(calendar.IllegalMonthError)

# %% Implementación de la clase Persona
# Persona:
    # Tiene una fecha de nacimiento (modulo datetime): lista de tres numeros (yyyy, mm, dd)
      # Hay que tener ciertas consideraciones:
          # La primera componente de esta lista representa al año: desde 1900 hasta el presente año
          # La segunda componente de esta lista representa al mes: debe ser un numero entero de 1 a 12
          # La tercera componente de esta lista representa al día: debe ser un entero de 1 a 31
    # Posee un dni (string de 8 caracteres)
    # Posee uno o más nombres: Dato de tipo lista
    # Posee un apellido paterno: Dato de tipo lista
    # Posee un apellido materno: Dato de tipo lista
    # Tiene un sexo: string de un solo caracter (M o F)
    # Puede comunicarse (devolver una cadena de caracteres)


# %% 

class Persona:
  """
  Persona :
    Tiene una fecha de nacimiento (modulo datetime) : lista te tres numeros (yyyy, mm, dd)
      Hay que tener ciertas consideraciones :
        La primera componente de esta lista representa al año : desde 1900 hasta el presente año
        La segunda componente de esta lista representa al mes : debe ser un numero entero  de 1 a 12
        La tercera componente de esta lista representa al dia : debe ser un enero de 1 a 31
    Posee un dni (string de 8 caracteres)
    Posee un o mas nombres : Dato de tipo lista
    Posee un apellido paterno : Dato de tipo lista
    Posee un apellido materno : Dato de tipo lista
    Tiene un sexo : string de un solo caracter (M o F)
    Puede comunicarse (decolver una cadena de caracteres)
  """

  # Constructor __init__
  def __init__(self,
               fechaNac = [1982,3,26],
               dni = "66666666",
               nombre = ["Jose", "Luis"],
               apellido_paterno = ["Arevalo"],
               apellido_materno = ["De la Fuente"],
               sexo = "M"):
    """
    Constructor de la clase Persona
    """
    # Primer paso es realizar algunas verificaciones con respecto al diseño de la clase
    if (isinstance(fechaNac , list)) and (isinstance(dni, str)) and (isinstance(nombre, list)) and (isinstance(apellido_paterno, list)) and \
     (isinstance(apellido_materno, list)) and (isinstance(sexo, str)):
     if (len(fechaNac) == 3) and (len(dni) == 8) and (len(sexo) == 1):
      if (isinstance(fechaNac[0], int)) and  (fechaNac[0] >= 1900) and (fechaNac[0] <= datetime.date.today().year):
        if  (isinstance(fechaNac[1] , int)) and (fechaNac[1] >= 1) and (fechaNac[1] <=12)  :
          if (isinstance(fechaNac[2] , int)) and (fechaNac[2] >= 1)  and (fechaNac[2] <= 31) :
            if (sexo == "M") or (sexo == "m") or (sexo == "F") or (sexo == "f") :
                self.fechaNac = fechaNac
                self.dni = dni
                self.nombre = nombre
                self.apellido_paterno = apellido_paterno
                self.apellido_materno = apellido_materno
                self.sexo = sexo
    else :
      # Instanciamos de manera manual una excepcion
      raise TypeError("Alguna entrada al momento de instanciar la clase Persona no es el tipo de dato correcto .")

  # Modifiquemos el metodo __repr__
  def __repr__(self):
    return "Instancia correctamente creada."

# %% Documentacion de la clase persona

help(Persona)

# Prueba1
Peruano1 = Persona()        
Peruano1

# Lista de miembros/metodos/atributos/constantes de un objeto de clase Persona
dir(Peruano1)   

#
Peruano1.fechaNac     

# En pit146 hay 4578 alumnos
ListaPIT146 = []
for participante in range(4578):
    ListaPIT146.append(Persona())
    
ListaPIT146

# Participante de indice 666
ListaPIT146[666].nombre

# Otra instancia de la clase Persona
Peruano2 = Persona([1983,5,12])
Peruano2

# Accedamos al atributo fechaNac
Peruano2.fechaNac

# Accedamos al atributo nombre
Peruano2.nombre

# Otra instancia de la clase persona
Peruano3 = Persona("m")
Peruano3

# Vemos que es necesario especificar el nombre del argumento
Peruano4 = Persona(sexo="F")
Peruano4

help(Peruano4)
Peruano5 = Persona([1988,10,12],"123456789", ["Mario"],["Sota"],["Cardenas"])
Peruano5

# %% Herencia Simple

# Bajo el supuesto que corrijieron la clase Persona, implementemos la subclase

class Supervisor(Persona):
  """
  Clase que hereda Persona y define subclase : Supervisor
  """

  # Modifiquemos el metodo __init__ de la subclase Supervisor
  # Agreguemos el campo "rol"  a los argumentos de la clase Persona
  def __init__ (self, fechaNac, dni, nombre, apellido_paterno, apellido_materno, sexo, rol):
    """
    Constructor de la clase Supervisor
    """
    # INvoquemos el constructor de la clase Persona
    Persona.__init__(self, fechaNac, dni, nombre, apellido_paterno, apellido_materno, sexo)

    # Al objeto self le agregamos el nuevo atributo rol
    self.rol = rol

    # Agreguemos atributos internos al objeto self
    import os
    self.sistema_operativo = os.uname()[0]
    import datetime
    self.datetime_creacion = datetime.datetime.now()

    # El atributo tareas
    self.tareas = ["Contratos", "Impuestos", "MedidasSeguridad"]

# %%

Super1 = Supervisor(fechaNac = [1975, 5,31],
                    dni = "12457889",
                    nombre = ["Julian"],
                    apellido_paterno = ["Zapata"],
                    apellido_materno = ["Urqueaga"],
                    sexo = "M",
                    rol = "Admin")
Super1










