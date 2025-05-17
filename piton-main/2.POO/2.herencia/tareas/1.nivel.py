'''
Ejercicio 1: Herencia básica
Objetivo: crear una clase base y una subclase que herede de ella.

- Crea una clase llamada Persona con atributos nombre y edad.
- Añade un método saludar que imprima un saludo con el nombre.
- Luego, crea una clase Estudiante que herede de Persona y tenga un atributo carrera.
- Añade un método estudiar que imprima que está estudiando su carrera.
- Instancia un Estudiante y llama a ambos métodos.
'''
# Clase padre (superclase)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre # Atributos
        self.edad = edad

    def saludar(self):      # Método
        print(f"Hola, me llamo {self.nombre}!")

# Clase hija (subclase)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera): 
        super().__init__(nombre, edad)  # llamada al constructor de Persona (clase padre)
        self.carrera = carrera
    
    def estudiar(self):     # Método
        print(f"Estoy estudiando la carrera de {self.carrera}")
        
estu = Estudiante("Hana", 21, "Ingeniería en Ciberseguridad")

estu.saludar()
estu.estudiar()

