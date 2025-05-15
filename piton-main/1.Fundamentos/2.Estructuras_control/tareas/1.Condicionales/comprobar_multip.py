'''
Pide un número y di si está entre 10 y 20
usando if 10 < x < 20.
'''
numero = int(input("Elige un número: "))

if numero > 10 and numero < 20:
    print(f"El número {numero} está entre 10 y 20")
elif numero < 10:
    print(f"El número {numero} es menor que 10")
else:
    print(f"El número {numero} es mayor que 20")

