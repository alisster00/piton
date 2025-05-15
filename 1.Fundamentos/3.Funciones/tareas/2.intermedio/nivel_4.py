'''
Crea una función que reciba datos como nombre y edad usando **kwargs
y los imprima en formato "Nombre: X, Edad: Y"
'''

def saludar(**kwargs):
    for nombre, edad in kwargs.items():
        print(f"{nombre} {edad}")

saludar(nombre="Akari", edad=25)
