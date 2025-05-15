'''
Crea una función que retorne dos valores:
la suma y la multiplicación de dos números.
'''

def valores(a, b):
    suma = a + b
    mult = a * b
    return suma, mult

s, m = valores(4, 8)

print(f"Suma: {s} | Multi: {m}")

