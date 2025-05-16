'''
¿Qué es una clase?

Una clase es un molde o plantilla para crear objetos. Define:
- Atributos (datos o características)
- Métodos (funciones o comportamientos)

Ejemplo:
'''

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

'''
- Perro es la clase
- __init__ es el constructor, se ejecuta al crear un objeto.
- self.nombre y self.edad son atributos
- ladrar es un método
'''


'''
¿Qué es un objeto?

Un objeto es una instancia concreta de una clase.
Tiene los valores específicos de los atributos definidos por la clase.

Ejemplo:
'''

mi_perro = Perro("Fido", 3)
otro_perro = Perro("Luna", 5)

mi_perro.ladrar()   # Fido dice: ¡Guau!
otro_perro.ladrar() # Luna dice: ¡Guau!

'''
- mi_perro y otro_perro son objetos de la clase Perro
- Cada uno tiene nombre y edad propios
- Comparten el mismo comportamiento (ladrar) pero los datos son distintos
'''

'''
RESUMEN:

Clase       Plantillas para crear objetos       class Perro:
Objeto      Instancia concreta de una clase     mi_perro = Perro("Fido", 3)
Atributo    Dato que pertenece al objeto        self.nombre
Método      Acción o función del objeto         ladrar()

'''
