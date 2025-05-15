'''
Una función es un bloque de código reutilizable que realiza una tarea específica. 
Sirve para evitar repetir código y para organizar mejor un programa.

En python se utiliza la clave def

Cosas importantes:

- def: definir una función
- parámetros van entre paréntesis
- bloque de código identado
- return: devuelve un valor (puede omitirse si no necesitas devolver nada)
'''

# Definir una función:
def nombre_de_la_funcion(parametros):
    # bloque de código
    return resultado # opcional

# Ejemplo de función:
def saludar():
    print("Hola, ¿cómo estás?")

# llamar a la función
saludar()

# Función con parámetros:
def saludar_a(nombre):
    print(f"Hola, {nombre}!")
saludar_a("Ana")

# Función que devuelve un valor
def sumar(a, b):
    return a + b
resultado = sumar(3, 5)
print(resultado) # imprime 8
