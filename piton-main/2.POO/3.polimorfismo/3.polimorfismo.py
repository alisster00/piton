'''
El polimorfismo en programación orientada a objetos (POO)
se refiere a la capacidad que tienen diferentes clases
de responder al mismo mensaje (método) de distintas maneras.
En otras palabras, distintos objetos pueden compartir un mismo método con el mismo bombre,
pero cada una puede tener su propia implementación.

En Python, el polimorfismo se logra gracias a su naturaleza dinámica (duck typing)
y el uso de herencia o simplemente mediante interfaces comunes.
'''

# POLIMORFISMO CON HERENCIA

class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

'''
Aquí tenemos una clase base Animal con un método hablar(),
y dos clases hijas (Perro y Gato) que sobreescriben ese método.

Podemos usar los objetos de forma polimórfica así: '''

animales = [Perro(), Gato()]
for animal in animales:
    print(animal.hablar()) # salida: Guau / Miau

# Cada objeto responde al método hablar() según su propia implementación

# POLIMORFISMO SIN HERENCIA (Duck Typing)
'''
En Python no necesitas herencia estricta para tener polimorfismo.
Lo importante es que los objetos tengan los métodos esperados. '''

class Pato:
    def volar(self):
        return "El pato vuela bajo"

class Avion:
    def volar(self):
        return "El avión vuela alto"

def hacer_volar(objeto):
    print(objeto.volar())

hacer_volar(Pato())

# POLIMORFISMO CON HERENCIA
'''
Esto es el famoso "si camina como un pato y suena como un pato...".
Python no exige que ambas clases hereden de una misma superclase,
solo que tengan el método que se va a invocar. '''

# RESUMEN
'''
Tipo de Polimorfismo    Característica                          Ejemplo

Con herencia        Clases derivadas sobreescriben          Perro y Gato heredan de Animal
                    métodos de la clase base.
Duck Typing         No hay herencia explícita;              Pato y Avion tienen volar()
                    importa que tengan los mismos métodos.
'''
