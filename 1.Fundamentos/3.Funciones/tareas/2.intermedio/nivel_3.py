'''
Crea una función que reciba cualquier cantidad de números y devuelva su suma
(usando *args).
'''

def suma(*args):
    return sum(args)

print(suma(1, 2, 3, 4, 5))
