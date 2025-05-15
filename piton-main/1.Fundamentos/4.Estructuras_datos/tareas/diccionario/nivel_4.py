'''
4. Transformar dos listas:
    - Una lista con claves y otra con valores, y combinarlas en un diccionario usando zip()
'''

nombres = ["Ana", "Hana", "Juan", "Luis"]
edad = [20, 24, 22, 26]

comb = zip(nombres, edad)

lista = list(comb)

print(lista)
