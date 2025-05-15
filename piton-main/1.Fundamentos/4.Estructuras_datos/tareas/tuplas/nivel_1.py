'''
1. Crea una tupla con datos personales (nombre, edad, país):
     - Desempaquetar sus valores en variables
     - Intentar modificar la edad (para reforzar que es inmutable)
'''

datos = ("Akari", 25, "Rusia")

datos[1] = 26
print(datos)

dados = list(datos)

print(dados)
dados[1] = 26

print(dados)
