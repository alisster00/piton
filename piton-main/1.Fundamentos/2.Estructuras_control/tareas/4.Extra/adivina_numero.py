'''
Genera un número aleatorio del 1 al 10.
Pide al usuario que adivine hasta acertar (usa while, if, break).
'''
import random

numero = random.randint(1, 10)

while True:
    user = int(input("Inserta un número: "))
    if user == numero:
        print("Has acertado")
        break
    else:
        print("No es el número. Sigue intentando")
    
