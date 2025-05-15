'''
3. Comprobar existencia:
    - Escribir un programa que pregunte al usuario un número y diga si está en un set predefinido.
'''

a = {1, 2, 3, 4, 5}

user = int(input("Inserta un número: "))

if user in a:
    print("Número encontrado")
else:
    print("Número no encontrado")
