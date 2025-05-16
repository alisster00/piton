'''
Clase Persona: define una persona con nombre y edad, y un método saludar() 
que diga "Hola, me llamo <nombre> y tengo <edad> años"
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

