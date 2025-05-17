'''
Ejercicio 2: uso de super() en constructores
Objetivo: practicar la llamada al constructor de la clase padre.

- Define una clase Vehiculo con los atributos marca y modelo, y un método describir().
- Crea una subclase Auto que añada el atributo puertas.
- Usa super() para llamar al constructor de Vehiculo desde Auto.
- Crea un objeto Auto e imprime su descripción.
'''

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    
    def describir(self):
        super().describir() # Llamar al método describir() de Vehiculo
        print(f"Puertas: {self.puertas}")

auto = Auto("Toyota", "Corolla", 4)
auto.describir()




