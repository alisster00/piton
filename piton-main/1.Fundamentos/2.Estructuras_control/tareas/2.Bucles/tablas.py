'''
Pide un número y muestra su tabla de multiplicar del 1 al 10 usando for.
'''
numero = int(input("Inserta un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")