'''
Crea una función anidada donde la función interna acceda a una variable de la extenera
(esto ayudará a practicar el ámbito enclosing).
'''

valor = 20

def anidar():
    def acceso():
        global = valor 15
    print(acceso())

anidar()


