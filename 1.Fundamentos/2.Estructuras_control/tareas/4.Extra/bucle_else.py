'''
Haz un programa que busque un número e una lista.
Si lo encuentra, imprime "Encontrado" y rompe el bucle.
Si no lo encuentra, usa else para imprimir "No encontrado".
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

usuario = int(input("Inserta un número: "))

for numero in lista:
    if usuario == numero:
        print("Encontrado")
        break
    else:
        print("No encontrado")
