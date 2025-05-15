'''
¿Qué es el ámbito (scope=?
El ámbito determina dónde una variable puede ser accedida o usada en tu código.
En python, hay dos tipos de variables principales:
- Ambito local: dentro de una función.
- Ambito global: fuera de cualquier función (en todo el programa).
'''

# Ejemplo:
x = 10 # variable global

def mi_funcion():
    y = 5 # variable local
    print(x) # puede acceder a la global
    print(y) # puede acceder a su propia variable local

mi_funcion()

print(x) # Ok, x es global
print(y) # Error: solo existe dentro de la función

# x es global porque está fuera de la función.
# y es local a mi_función() y no se puede acceder fuera de ahí.

# REGLAS DEL AMBITO:

# 1.Las funciones pueden leer variables globales.
x= 10 # variable global 
def mostrar():
    print(x) # sí funca
mostrar()

# 2.Las funciones no pueden modificar variables globales directamente 
# (a menos que se use global)
x = 3 # global
def cambiar():
    x = 5 # esto crea una nueva 'x' local, no cambia la global
    print(x)
cambiar()
print(x) # sigue siendo 3

# si quieres modificar la global:
x = 3
def cambiar():
    global x
    x = 5 # ahora sí cambia la global
cambiar()
print(x) # ahora es 5

'''
AMBITO ANIDADO (LEGB Rule)
Python sigue esta regla para buscar variable (de más cerca a más lejos):

- Local (dentro la función)
- Enclosing (dentro de funciones anidadas)
- Global (a nivel del archivo)
- Built-in (palabras clave de Python como len, print)
'''
# Ejemplo:
x = "global"
def externa():
    x = "enclosing"
    def interna():
        x = "local"
        print(x)
    interna()
externa() # Imprime "local"

# Global: fuera de funciones. Se puede usar fuera
# Local: dentro de funciones. No se puede usar fuera



