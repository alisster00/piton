from os import system

system("clear")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista del 1 al 10: {lista}")

pares = [numeros for numeros in lista if numeros % 2 == 0]
print(f"Números pares de la lista: {pares}")

suma = sum(pares)
print(f"Suma de los pares: {suma}")

promedio = len(pares)
print(f"Promedio de los pares:", suma / promedio)

pares.reverse()
print(f"Lista invertida: {pares}")

pares.reverse()
print(f"Lista ordenada: {pares}")

