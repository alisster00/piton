'''
Crea una lista de números y pide al usuario uno.
Si lo encuentra, imprimme "¡Encontrado!" 
y termina el bucle con break
'''
lista = [1, 2, 4, 6, 4, 12, 83, 49, 21, 8, 9, 5, 3]

numero = int(input("Inserta un número: "))

for numeros in lista:
    if numeros == numero:
        print(f"¡Encontrado!")
        break
