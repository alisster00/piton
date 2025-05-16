'''
La herencia en programación orientada a objetos (POO)
es un mecanismo que permite a una clase (llamada clase hija o subclase)
heredar a tributos y métodos de otra clase (llamada clase padre o superclase).
Esto promueve la reutilización de código y la creación de jerarquías lógicas entre clases.

En Python, la herencia se implementa de forma sencilla utilizando paréntsesis al definir la subclase.
'''

# Ejemplo Básico:

# clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido")

# clase hija
class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

# uso 
mi_perro = Perro("Fido")
mi_perro.hablar() # Salida: Fido dice: ¡Guau!

'''
¿Qué está pasando aquí?

- Perro hereda de Animal.
- La clase Perro puede usar atributos y métodos de Animal.
- Además, puedes sobreescribir métodos como hablar() (esto se llama overriding).
'''

'''
¿Por qué usar la herencia?

- Reutilización de código: no tienes que escribir funciones comunes.
- Organización jerárquica: modelas relaciones tipo "es un" (un Perro es un Animal).
- Polimorfismo: puedes usar objetos de diferentes clases con una interfaz común.
'''

# HERENCIA MULTIPLE
# Python permite que una clase herede de más de una clase:

class Mamifero:
    def amamantar(self):
        print("Amamantando cría")

class Actuatico:
    def nadar(self):
        print("Nadando")

class Delfin(Mamifero, Acuatico):
    pass

d = Delfin()
d.amamantar()   # Heredado de Mamifero
d.nadar()       # Heredado de Acuatico


# USO DE super()
# Cuando sobrescribes un método
# y quieres llamar al método original de la clase padre
# usas super():

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)    # Llama al constructor de Animal
        self.color = color

'''
El uso de super() en Python es clave cuando trabajas con herencia,
ya que te permite acceder a métodos y atributos de la clase padre
sin referenciarla directamente por su nombre.
Es especialmente útil para extender funcionalidad de clases base 
sin reescribir todo desde cero.
'''

'''
¿Qué hace exactamente super()?
super() devuelve un objeto proxy que delega llamadas al método de la superclase
según el orden de resolución de métodos (MRO Method Resolution Order).
En otras clases, buscas el método correspondientes en la jerarquía de clases,
respetando el orden de la herencia.
'''

# Uso típico: llamar al constructor de la clase padre

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)    # Llama al constructor de Persona
        self.carrera = carrera

e = Estudiante("Ana", "ingenieria")
print(e.nombre)     # Ana
print(e.carrera)    # Ingeniería


# super() con otros métodos, no solo __init__

class Vehiculo:
    def encender(self):
        print("El vehiculo está encendido")

class Auto(Vehiculo):
    def encender(self):
        super().encender() # Llma a encender() de Vehiculo
        print("El auto está listo para conducir")

a = Auto()
a.encender()
# Salida:
# El vehiculo está encendido
# El auto está listo para conducir

'''
En Herencia múltiple

Con super(), Python usa el MRO para determinar el orden en que se llaman los métodos.
'''

class A:
    def saludo(self):
        print("Hola desde A")

class B(A):
    def saludo(self):
        print("Hola desde B")
        super().saludo()

class C(A):
    def saludo(self):
        print("Hola desde C")
        super().saludo()

class D(B, C):
    def saludo(self):
        print("Hola desde D")
        super().saludo()

d = D()
d.saludo()

# Hola desde D
# Hola desde B
# Hola desde C
# Hola desde A

# El orden de llamada sigue el MRO de la clase D,
# que puedes ver con:

print(D.__mro__)

'''
Recomendaciones:

- Siempre usa super() en lugar de referenciar directamente a la clase base
(ClasePadre.metodo(self)) si estás usando herencia múltiple o planeas extender clases más adelante.

- Usa super() sin argumentos en Python3 (super().metodo()), ya que es más legible y limpio.
'''

