'''
Crea una función que use una variable global y que además tenga una variable local.
Imprime ambas dentro de la función y muestra qué pasa si intentas imprimr la local fuera.
'''

x = 25

def edad():
#    global x
    x = 19
    print(x)

print(x)
edad()
