'''
Crea una clase Coche con los atributos marca, modelo y año.
Agrega un método describir() que imprima esos datos.
'''

class Coche:
    def __init__(self, marca, modelo, year):
        self.marca = marca
        self.modelo = modelo
        self.year = year

    def describir(self):
        print(f"El auto {self.marca}, modelo {self.modelo}, del año {self.year}")

bmw = Coche("BMW", "NOSE", "2005")
honda = Coche("Honda", "TAMPOCOSE", "2010")

bmw.describir()
honda.describir()
